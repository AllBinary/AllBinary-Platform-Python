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

from java.lang.JavaRuntimeStatic import java_predicate
# from java.io.FileFilter import FileFilter


class VisitorFileFilter(FileFilter):

    def _init_fields(self) -> None:
        if "booleanVisitorInterface" not in vars(self): self.booleanVisitorInterface: VisitorInterface = None
    

    def __init__(self, booleanVisitorInterface: VisitorInterface) -> None:
        from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface
        __class__._init_fields(self)
        self.booleanVisitorInterface = booleanVisitorInterface
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def accept_j1_1(self, file: File) -> bool:
        from java.io.File import File
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        abFile: AbFile = FileWrapperUtil.wrapFile(file)
        isFileAcceptable: bool = (self.booleanVisitorInterface.visit(abFile))
        return isFileAcceptable or java_predicate(file, "isDirectory")
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def accept_j1_2(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        isFileAcceptable: bool = (self.booleanVisitorInterface.visit(file))
        return isFileAcceptable or java_predicate(file, "isDirectory")

    def accept(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "File" for base in type(args[0]).__mro__)):
            return __class__.__dict__["accept_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["accept_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("accept_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().accept(*args)
# from java.io.File import File
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
# from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


