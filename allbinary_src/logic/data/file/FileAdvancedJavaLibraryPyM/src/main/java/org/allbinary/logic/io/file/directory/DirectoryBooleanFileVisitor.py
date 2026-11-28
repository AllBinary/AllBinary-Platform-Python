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

from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


class DirectoryBooleanFileVisitor(VisitorInterface):
    

    def __init__(self) -> None:
        pass
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_1(self, anyType: object) -> object:
        from org.allbinary.logic.io.file.AbFile import AbFile
        return self.visit(anyType)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_2(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        if java_predicate(file, "isDirectory"):
            return True
        return False

    def visit(self, *args):
        if len(args) == 1 and True:
            return __class__.__dict__["visit_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["visit_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("visit_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().visit(*args)
# from org.allbinary.logic.io.file.AbFile import AbFile


