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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.io.file.visitor.BooleanFileVisitor import BooleanFileVisitor


@java_inherited_overloads
class ExcludeFileExtensionsBooleanFileVisitor(BooleanFileVisitor):
    

    def __init__(self, filterStringBasicArrayList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(filterStringBasicArrayList)
    

    def visit_j1(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        if self.getFilterStringBasicArrayList().size() == 0:
            return True
        return java_super_call(super(), "visit", file)
    

    def visit_j2(self, file: AbFile, fileNameString: str) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        fileNameAndExtension: str = file.getPath()
        if len(fileNameAndExtension) > len(fileNameString):
            startIndex: int = len(fileNameAndExtension) - len(fileNameString)
            fileName: str = fileNameAndExtension[startIndex:]
            if ((fileName > fileNameString) - (fileName < fileNameString)) == 0:
                return False
        return True

    def visit(self, *args):
        implementation = __class__.__dict__.get("visit_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().visit(*args)
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.util.BasicArrayList import BasicArrayList


