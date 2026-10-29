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

from org.allbinary.logic.io.file.visitor.IncludeFileExtensionsBooleanFileVisitor import IncludeFileExtensionsBooleanFileVisitor


class DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor(IncludeFileExtensionsBooleanFileVisitor):

    def _init_fields(self) -> None:
        self.trackedStrings: TrackedStrings = TrackedStrings.getInstance()
        self.gitProcessHelper: GitProcessHelper = GitProcessHelper.getInstance()
        self.includesString: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, filterStringBasicArrayList: BasicArrayList) -> None:
        super().__init__(filterStringBasicArrayList)
        self._init_fields()
        self.includesString = None
    

    def _constructor2(self, filterStringBasicArrayList: BasicArrayList, includesString: str) -> None:
        super().__init__(filterStringBasicArrayList)
        self._init_fields()
        self.includesString = includesString
    

    def visit(self, file: AbFile) -> bool:
        if file.isDirectory():
            return True
        if self.includesString is None or file.getAbsolutePath().indexOf(self.includesString) >= 0:
            return super().visit(file)
        else:
            return False
    

    # Java overloaded method: Python keeps the last definition
    def visit(self, file: AbFile, fileNameString: str) -> bool:
        filePath: str = file.getPath()
        if super().visit(file, fileNameString):
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
    

    @staticmethod
    def main(args: list[str]) -> None:
        commonFileStrings: CommonDataFileStrings = CommonDataFileStrings.getInstance()
        list_: BasicArrayList = BasicArrayListD()
        list_.add(commonFileStrings.JAVA)
        filePath: str = "G:\\mnt\\bc\\mydev\\games\\ZeptoRacer\\platform\\j2se\\ZeptoRacerStaticPathsJ2SEM\\target\\dependency\\org\\allbinary\\logic\\system\\security\\licensing\\ZeptoRacerPCClientInformation.java"
        result: bool = DirectoryOrIncludeFileExtensionAndTrackedBooleanFileVisitor(list_).visit(AbFile.createAbFileFromRawPath(filePath))
        print(filePath + " is Tracked: " + str(result))
from org.allbinary.java.runtime.process.git.GitProcessHelper import GitProcessHelper
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.io.file.directory.TrackedStrings import TrackedStrings


