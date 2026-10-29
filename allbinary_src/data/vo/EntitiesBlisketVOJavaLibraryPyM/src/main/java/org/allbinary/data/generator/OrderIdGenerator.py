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

from org.allbinary.data.generator.UniqueIdGenerator import UniqueIdGenerator


class OrderIdGenerator(UniqueIdGenerator):

    def _init_fields(self) -> None:
        self.IDFILE: str = "orderId"
    

    def __init__(self) -> None:
        from org.allbinary.data.generator.UniqueIdGenerator import UniqueIdGenerator
        super().__init__()
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.PATH_GLOBALS.getInstance().INIT_PATH)
        stringBuffer.append(self.IDFILE)
        stringBuffer.append(UniqueIdGenerator.EXT)
        super().setFile(str(stringBuffer), self.IDFILE)
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.string.StringMaker import StringMaker


