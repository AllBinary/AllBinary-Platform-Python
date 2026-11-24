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
        from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface
        self.booleanVisitorInterface: VisitorInterface = None
    

    def __init__(self, booleanVisitorInterface: VisitorInterface) -> None:
        from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface
        self._init_fields()
        self.booleanVisitorInterface = booleanVisitorInterface
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def accept_j1_1(self, file: File) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        abFile: AbFile = FileWrapperUtil.wrapFile(file)
        isFileAcceptable: bool = (self.booleanVisitorInterface.visit(abFile))
        return isFileAcceptable or file.isDirectory()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def accept_j1_2(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        isFileAcceptable: bool = (self.booleanVisitorInterface.visit(file))
        return isFileAcceptable or file.isDirectory()

    def accept(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.accept_j1_1(*args)
        if len(args) == 1:
            return self.accept_j1_2(*args)
        return getattr(self, "accept_j" + str(len(args)))(*args)
# from java.io.File import File
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
# from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


