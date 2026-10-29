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
# package org.allbinary.logic.io.file.filter

from __future__ import annotations

# from java.io.FileFilter import FileFilter


class VisitorFileFilter(FileFilter):

    def _init_fields(self) -> None:
        self.booleanVisitorInterface: VisitorInterface = None
    

    def __init__(self, booleanVisitorInterface: VisitorInterface) -> None:
        self._init_fields()
        self.booleanVisitorInterface = booleanVisitorInterface
    

    def accept(self, file: File) -> bool:
        abFile: AbFile = FileWrapperUtil.wrapFile(file)
        isFileAcceptable: bool = (self.booleanVisitorInterface.visit(abFile))
        return isFileAcceptable or file.isDirectory()
    

    # Java overloaded method: Python keeps the last definition
    def accept(self, file: AbFile) -> bool:
        isFileAcceptable: bool = (self.booleanVisitorInterface.visit(file))
        return isFileAcceptable or file.isDirectory()
# from java.io.File import File
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


