#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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
# package org.allbinary.logic.io.file.directory

from __future__ import annotations

from java.lang.System import System
from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.io.file.visitor.IncludeFileExtensionsBooleanFileVisitor import IncludeFileExtensionsBooleanFileVisitor


@java_inherited_overloads
class DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor(IncludeFileExtensionsBooleanFileVisitor):
    def _java_defaults(self):
        vars(self).setdefault("trackedStrings", None)
        vars(self).setdefault("gitProcessHelper", None)
        vars(self).setdefault("includesString", None)

    def _init_fields(self) -> None:
        from org.allbinary.java.runtime.process.git.GitProcessHelper import GitProcessHelper
        self.trackedStrings: TrackedStrings = TrackedStrings.getInstance()
        self.gitProcessHelper: GitProcessHelper = GitProcessHelper.getInstance()
        if "includesString" not in vars(self): self.includesString: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor1(self, filterStringBasicArrayList: BasicArrayList) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(filterStringBasicArrayList)
        __class__._init_fields(self)
        self.includesString = None
    

    def _constructor2(self, filterStringBasicArrayList: BasicArrayList, includesString: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(filterStringBasicArrayList)
        __class__._init_fields(self)
        self.includesString = includesString
    

    def visit_j1(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        if java_predicate(file, "isDirectory"):
            return True
        if self.includesString is None or file.getAbsolutePath().indexOf(self.includesString) >= 0:
            return java_super_call(super(), "visit", file)
        else:
            return False
    

    def visit_j2(self, file: AbFile, fileNameString: str) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        filePath: str = file.getPath()
        if java_super_call(super(), "visit", file, fileNameString):
            if not ((self.trackedStrings.APPLICATION in filePath) or (self.trackedStrings.APP in filePath) or (self.trackedStrings.HTML_TEMP in filePath)):
                if not ((self.trackedStrings.TARGET_PATH_WINDOWS in filePath) or (self.trackedStrings.TARGET_PATH_UNIX in filePath)):
                    if self.gitProcessHelper.isTracked(file):
                        return True
                    else:
                        pass
                else:
                    pass
            else:
                pass
        return False

    def visit(self, *args):
        implementation = __class__.__dict__.get("visit_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().visit(*args)
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        commonFileStrings: CommonDataFileStrings = CommonDataFileStrings.getInstance()
        list_: BasicArrayList = BasicArrayListD()
        list_.add(commonFileStrings.JAVA)
        filePath: str = "G:\\mnt\\bc\\mydev\\games\\ZeptoRacer\\platform\\j2se\\ZeptoRacerStaticPathsJ2SEM\\target\\dependency\\org\\allbinary\\logic\\system\\security\\licensing\\ZeptoRacerPCClientInformation.java"
        result: bool = DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor(list_).visit(AbFile.createAbFileFromRawPath(filePath))
        print(filePath + " is Tracked: " + str(result))
# from org.allbinary.java.runtime.process.git.GitProcessHelper import GitProcessHelper
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.io.file.directory.TrackedStrings import TrackedStrings


