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
# package org.allbinary.logic.math.vector

from __future__ import annotations



class Vertex:

    def _init_fields(self) -> None:
        self.x: BasicDecimal = BasicDecimal(0)
        self.y: BasicDecimal = BasicDecimal(0)
        self.z: BasicDecimal = BasicDecimal(0)
    

    def __init__(self) -> None:
        self._init_fields()
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        positionStrings: PositionStrings = PositionStrings.getInstance()
        stringBuffer.append(positionStrings.X_LABEL)
        stringBuffer.append(str(self.x))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(positionStrings.Y_LABEL)
        stringBuffer.append(str(self.y))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(positionStrings.Z_LABEL)
        stringBuffer.append(str(self.z))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonSeps import CommonSeps


