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
# package org.allbinary.data.generator

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.data.generator.UniqueIdGenerator import UniqueIdGenerator


@java_inherited_overloads
class ProductIdGenerator(UniqueIdGenerator):
    def _java_defaults(self):
        vars(self).setdefault("IDFILE", None)

    def _init_fields(self) -> None:
        self.IDFILE: str = "productId"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.data.generator.UniqueIdGenerator import UniqueIdGenerator
        from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.string.StringMaker import StringMaker
        super().__init__()
        __class__._init_fields(self)
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(URLGLOBALS.getMainPath())
        stringBuffer.append(PATH_GLOBALS.getInstance().INIT_PATH)
        stringBuffer.append(self.IDFILE)
        stringBuffer.append(UniqueIdGenerator.EXT)
        java_super_call(super(), "setFile", str(stringBuffer), self.IDFILE)
# from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.string.StringMaker import StringMaker


