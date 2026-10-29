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
# package org.allbinary.graphics

from __future__ import annotations



class GPoint:
    POINT_LABEL: str = "Point: "

    def _init_fields(self) -> None:
        self.x: int = None
        self.y: int = None
        self.z: int = None
    

    @staticmethod
    def getInstance(point: GPoint) -> GPoint:
        return GPoint(point.getX(), point.getY(), point.getZ())
    

    def __init__(self, x: int, y: int, z: int) -> None:
        self._init_fields()
        self.x = x
        self.y = y
        self.z = z
    

    def getX(self) -> int:
        return self.x
    

    def getY(self) -> int:
        return self.y
    

    def getZ(self) -> int:
        return self.z
    

    def getRawX(self) -> int:
        return self.x
    

    def getRawY(self) -> int:
        return self.y
    

    def getRawZ(self) -> int:
        return self.z
    

    def toString(self) -> str:
        return GPoint.toStringStatic(self.getX(), self.getY(), self.getZ())

    def __str__(self) -> str:
        return self.toString()
    

    @staticmethod
    def toStringStatic(x: int, y: int, z: int) -> str:
        stringBuffer: StringMaker = StringMaker()
        positionStrings: PositionStrings = PositionStrings.getInstance()
        stringBuffer.append(GPoint.POINT_LABEL)
        stringBuffer.append(positionStrings.X_LABEL)
        stringBuffer.appendint(x)
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(positionStrings.Y_LABEL)
        stringBuffer.appendint(y)
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(positionStrings.Z_LABEL)
        stringBuffer.appendint(z)
        return str(stringBuffer)
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonSeps import CommonSeps


