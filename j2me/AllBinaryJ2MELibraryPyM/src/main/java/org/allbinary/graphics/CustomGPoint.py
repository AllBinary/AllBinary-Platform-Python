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

from org.allbinary.graphics.GPoint import GPoint


class CustomGPoint(GPoint):
    NULL_CUSTOM_POINT: CustomGPoint = None

    def _init_fields(self) -> None:
        self.cx: int = 0
        self.cy: int = 0
        self.cz: int = 0
    

    @staticmethod
    def getInstance(point: GPoint) -> CustomGPoint:
        return CustomGPoint(point.getX(), point.getY(), point.getZ())
    

    @staticmethod
    def getInstance3(x: int, y: int) -> CustomGPoint:
        return CustomGPoint(x, y, 3)
    

    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y, z)
        self._init_fields()
    

    def setX(self, x: int) -> None:
        self.cx = x
    

    def getX(self) -> int:
        return self.cx
    

    def setY(self, y: int) -> None:
        self.cy = y
    

    def getY(self) -> int:
        return self.cy
    

    def setZ(self, z: int) -> None:
        self.cz = z
    

    def getZ(self) -> int:
        return self.cz


CustomGPoint.NULL_CUSTOM_POINT = CustomGPoint(0, 0, 0)

