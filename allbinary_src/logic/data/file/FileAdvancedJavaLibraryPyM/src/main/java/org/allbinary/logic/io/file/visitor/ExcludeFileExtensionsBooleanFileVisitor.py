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
# package org.allbinary.logic.io.file.visitor

from __future__ import annotations

from org.allbinary.logic.io.file.visitor.BooleanFileVisitor import BooleanFileVisitor


class ExcludeFileExtensionsBooleanFileVisitor(BooleanFileVisitor):
    

    def __init__(self, filterStringBasicArrayList: BasicArrayList) -> None:
        super().__init__(filterStringBasicArrayList)
    

    def visit(self, file: AbFile) -> bool:
        if self.getFilterStringBasicArrayList().size() == 0:
            return True
        return super().visit(file)
    

    # Java overloaded method: Python keeps the last definition
    def visit(self, file: AbFile, fileNameString: str) -> bool:
        fileNameAndExtension: str = file.getPath()
        if len(fileNameAndExtension) > len(fileNameString):
            startIndex: int = len(fileNameAndExtension) - len(fileNameString)
            fileName: str = fileNameAndExtension[startIndex:]
            if ((fileName > fileNameString) - (fileName < fileNameString)) == 0:
                return False
        return True
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.util.BasicArrayList import BasicArrayList


