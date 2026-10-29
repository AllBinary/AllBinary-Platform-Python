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

from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


class DirectoryBooleanFileVisitor(VisitorInterface):
    

    def __init__(self) -> None:
        pass
    

    def visit(self, anyType: object) -> object:
        return self.visit(anyType)
    

    # Java overloaded method: Python keeps the last definition
    def visit(self, file: AbFile) -> bool:
        if file.isDirectory():
            return True
        return False
from org.allbinary.logic.io.file.AbFile import AbFile


