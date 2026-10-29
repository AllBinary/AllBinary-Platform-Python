"""Compile generated Python and verify imports with local Maven dependencies.

Usage: python build.py SourceDir OutputDir ImportCheck FailOnError [DependencySourceDir...]
"""

import importlib
import py_compile
import sys
import traceback
import xml.etree.ElementTree as ElementTree
from pathlib import Path


PROJECT_ROOTS = (
    Path("G:/mnt/bc/mydev/workingpython"),
    Path("G:/mnt/bc/mydev/workpython"),
    Path("G:/mnt/bc/mydev/working_thirdpartypython"),
    Path("G:/mnt/bc/mydev/AllBinary-Platform-Integrationpython"),
)


def find_sources(source_dir):
    return sorted(path for path in source_dir.rglob("*.py") if "__pycache__" not in path.parts)


def module_name(source_dir, source):
    return ".".join(source.relative_to(source_dir).with_suffix("").parts)


def compile_sources(source_dir, output_dir, sources):
    failures = []
    for source in sources:
        compiled = output_dir / source.relative_to(source_dir).with_suffix(".pyc")
        try:
            py_compile.compile(str(source), cfile=str(compiled), doraise=True)
        except py_compile.PyCompileError as error:
            print(error.msg, file=sys.stderr)
            failures.append(f"compile {source}")
    return failures


def child_text(element, name):
    for child in element:
        if child.tag.rsplit("}", 1)[-1] == name:
            return (child.text or "").strip()
    return ""


def dependency_artifacts(pom):
    try:
        project = ElementTree.parse(pom).getroot()
    except (ElementTree.ParseError, OSError):
        return []
    artifacts = []
    for dependencies in project:
        if dependencies.tag.rsplit("}", 1)[-1] != "dependencies":
            continue
        for dependency in dependencies:
            if dependency.tag.rsplit("}", 1)[-1] != "dependency":
                continue
            artifact = child_text(dependency, "artifactId")
            scope = child_text(dependency, "scope")
            if artifact.endswith("Py") and scope != "test":
                artifacts.append(artifact)
    return artifacts


def project_index():
    index = {}
    for root in PROJECT_ROOTS:
        if not root.is_dir():
            continue
        for pom in root.rglob("pom.xml"):
            if "target" in pom.parts or "archetype-resources" in pom.parts:
                continue
            try:
                project = ElementTree.parse(pom).getroot()
            except (ElementTree.ParseError, OSError):
                continue
            artifact = child_text(project, "artifactId")
            source = pom.parent / "src" / "main" / "java"
            if artifact and source.is_dir() and artifact not in index:
                index[artifact] = (pom, source)
    return index


def local_dependency_dirs(project_dir):
    index = project_index()
    result = []
    visited = set()

    def add_dependencies(pom):
        for artifact in dependency_artifacts(pom):
            if artifact in visited:
                continue
            visited.add(artifact)
            project = index.get(artifact)
            if project is None:
                continue
            dependency_pom, source = project
            result.append(source)
            add_dependencies(dependency_pom)

    add_dependencies(project_dir / "pom.xml")
    return result


def import_modules(source_dir, dependency_dirs, sources):
    sys.dont_write_bytecode = True
    paths = [source_dir] + dependency_dirs
    sys.path[0:0] = [str(path) for index, path in enumerate(paths) if path not in paths[:index]]
    failures = []
    for source in sources:
        name = module_name(source_dir, source)
        try:
            importlib.import_module(name)
        except Exception:
            print(f"{name}: {traceback.format_exc().strip().splitlines()[-1]}", file=sys.stderr)
            failures.append(f"import {name}")
    return failures


def main(arguments):
    if len(arguments) < 4:
        print(__doc__, file=sys.stderr)
        return 2
    source_dir = Path(arguments[0]).resolve()
    output_dir = Path(arguments[1]).resolve()
    import_check = arguments[2] == "true"
    fail_on_error = arguments[3] == "true"
    dependency_dirs = []
    for dependency in arguments[4:]:
        dependency_dir = Path(dependency).resolve()
        if dependency_dir.is_dir():
            dependency_dirs.append(dependency_dir)
        else:
            print(f"Warning: Python dependency source directory does not exist: {dependency_dir}", file=sys.stderr)
    dependency_dirs.extend(local_dependency_dirs(Path(__file__).resolve().parent))

    sources = find_sources(source_dir)
    failures = compile_sources(source_dir, output_dir, sources)
    print(f"Python modules compiled: {len(sources) - len(failures)} of {len(sources)}")

    if import_check:
        import_failures = import_modules(source_dir, dependency_dirs, sources)
        print(f"Python modules imported: {len(sources) - len(import_failures)} of {len(sources)}")
        failures += import_failures

    if failures:
        print(f"Python build failures: {len(failures)}", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        if fail_on_error:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
