# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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

# from java.io.FileFilter import FileFilter
from org.allbinary.logic.util.visitor.VisitorInterface import VisitorInterface


class DirectoryFileVisitor(VisitorInterface, FileFilter):
    

    def __init__(self) -> None:
        pass
    

    def accept(self, arg0: File) -> bool:
        return (self.visit(arg0))
    

    def visit(self, anyType: object) -> object:
        file: File = anyType
        index: int = 1
        aFile: File = file.getParentFile()
        while ((aFile := aFile.getParentFile())) is not None:
            index += 1
        if file.isDirectory() and index < 5:
            return True
        return False
# from java.io.File import File


