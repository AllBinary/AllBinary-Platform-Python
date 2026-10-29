# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot 
#   
# Generated Code Do Not Modify
# package org.allbinary.java.runtime.process.git

from __future__ import annotations



#Do not use this instead just skip target, build, Application paths.
class GitProcessHelper:
    instance: GitProcessHelper = None

    def _init_fields(self) -> None:
        self.trackedStrings: TrackedStrings = TrackedStrings.getInstance()
    

    @staticmethod
    def getInstance() -> GitProcessHelper:
        return GitProcessHelper.instance
    

    def __init__(self) -> None:
        self._init_fields()
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        THIS_IS_SLOW: str = "This is slow consider path exclusion instead"
        logUtil.putF(THIS_IS_SLOW, self, commonStrings.CONSTRUCTOR)
    

    # throws IOException, InterruptedException
    def trackedFiles(self, rootAsString: str, pathspec: str) -> List[str]:
        return self.trackedFiles(rootAsString, pathspec, ".java")
    

    # throws IOException, InterruptedException
    # Java overloaded method: Python keeps the last definition
    def trackedFiles(self, rootAsString: str, pathspec: str, suffix: str) -> List[str]:
        from org.allbinary.java.runtime.process.git.ProcessBuilder import ProcessBuilder
        from org.allbinary.java.runtime.process.git.ProcessBuilder import ProcessBuilder
        process: Process = ProcessBuilder(self.trackedStrings.GIT_COMMAND, self.trackedStrings.CHANGE_DIRECTORY_OPTION, rootAsString, self.trackedStrings.LIST_FILES_COMMAND, self.trackedStrings.SEP_BY_NULL_CHAR_INSTEAD_OF_NEW_LINE, self.trackedStrings.PATHSPEC_SEPARATOR, pathspec).redirectError(ProcessBuilder.Redirect.INHERIT).start()
        output: list[int] = process.getInputStream().readAllBytes()
        exitCode: int = process.waitFor()
        if exitCode != 0:
            raise RuntimeError(str(StringMaker().append("git ls-files failed for ").append(rootAsString).append(" with exit code ").appendint(exitCode)))
        files: List[str] = ArrayList()
        start: int = 0
        relativePath: str = None
        for index in range(0, len(output)):
            if output[index] == 0:
                relativePath = bytes(output, start, index - start, StandardCharsets.UTF_8).decode()
                if relativePath.endswith(suffix):
                    files.add(relativePath)
                start = index + 1
        return files
    

    def isTracked(self, file: AbFile) -> bool:
        from org.allbinary.java.runtime.process.git.ProcessBuilder import ProcessBuilder
        try:
            nativeFile: File = AbFileNativeUtil.get(file)
            parentFile: File = nativeFile.getParentFile()
            process: Process = ProcessBuilder(self.trackedStrings.GIT_COMMAND, self.trackedStrings.CHANGE_DIRECTORY_OPTION, parentFile.getPath(), self.trackedStrings.LIST_FILES_COMMAND, self.trackedStrings.ERROR_UNMATCH_OPTION, self.trackedStrings.PATHSPEC_SEPARATOR, nativeFile.getName()).redirectErrorStream(True).start()
            process.getInputStream().readAllBytes()
            return process.waitFor() == 0
        except Exception as e:
            return False
# from java.io.File import File
# from java.io.IOException import IOException
# from java.nio.charset.StandardCharsets import StandardCharsets
# from java.util.ArrayList import ArrayList
# from java.util.List import List
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
from org.allbinary.logic.io.file.directory.TrackedStrings import TrackedStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


GitProcessHelper.instance = GitProcessHelper()

