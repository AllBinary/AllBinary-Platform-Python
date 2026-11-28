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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.io.file.visitor.IncludeFileExtensionsBooleanFileVisitor import IncludeFileExtensionsBooleanFileVisitor


@java_inherited_overloads
class DirectoryOrIncludeFileExtensionBooleanFileVisitor(IncludeFileExtensionsBooleanFileVisitor):
    def _java_defaults(self):
        vars(self).setdefault("includesString", None)

    def _init_fields(self) -> None:
        if "includesString" not in vars(self): self.includesString: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor1(self, filterStringBasicArrayList: BasicArrayList) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(filterStringBasicArrayList)
        __class__._init_fields(self)
        self.includesString = None
    

    def _constructor2(self, filterStringBasicArrayList: BasicArrayList, includesString: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__(filterStringBasicArrayList)
        __class__._init_fields(self)
        self.includesString = includesString
    

    def visit(self, file: AbFile) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        if java_predicate(file, "isDirectory"):
            return True
        if self.includesString is None or file.getAbsolutePath().indexOf(self.includesString) >= 0:
            return java_super_call(super(), "visit", file)
        else:
            return False
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.util.BasicArrayList import BasicArrayList


