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


class DirectoryOrIncludeFileExtensionBooleanFileVisitor(IncludeFileExtensionsBooleanFileVisitor):

    def _init_fields(self) -> None:
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
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.util.BasicArrayList import BasicArrayList


