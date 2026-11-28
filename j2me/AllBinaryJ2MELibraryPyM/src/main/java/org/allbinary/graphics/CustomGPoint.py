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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.GPoint import GPoint


@java_inherited_overloads
class CustomGPoint(GPoint):
    NULL_CUSTOM_POINT: CustomGPoint = None
    def _java_defaults(self):
        vars(self).setdefault("cx", 0)
        vars(self).setdefault("cy", 0)
        vars(self).setdefault("cz", 0)

    def _init_fields(self) -> None:
        if "cx" not in vars(self): self.cx: int = 0
        if "cy" not in vars(self): self.cy: int = 0
        if "cz" not in vars(self): self.cz: int = 0
    

    @staticmethod
    def getInstance(point: GPoint) -> CustomGPoint:
        return CustomGPoint(point.getX(), point.getY(), point.getZ())
    

    @staticmethod
    def getInstance3(x: int, y: int) -> CustomGPoint:
        return CustomGPoint(x, y, 3)
    

    def __init__(self, x: int, y: int, z: int) -> None:
        __class__._java_defaults(self)
        super().__init__(x, y, z)
        __class__._init_fields(self)
    

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


def _CustomGPoint_NULL_CUSTOM_POINT() -> object:
    return CustomGPoint(0, 0, 0)

lazy_static(CustomGPoint, "NULL_CUSTOM_POINT", _CustomGPoint_NULL_CUSTOM_POINT)

