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
# package org.allbinary.math

from __future__ import annotations



class RectangleCollisionUtil:
    instance: RectangleCollisionUtil = None
    

    @staticmethod
    def getInstance() -> RectangleCollisionUtil:
        return RectangleCollisionUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def isCollision(self, rectX1: int, rectY1: int, rectX2: int, rectY2: int, rect2X1: int, rect2Y1: int, rect2X2: int, rect2Y2: int) -> bool:
        if rect2X1 >= rectX2 or rect2Y1 >= rectY2 or rect2X2 <= rectX1 or rect2Y2 <= rectY1:
            return False
        else:
            return True
    

    def isInside(self, rectX1: int, rectY1: int, rectX2: int, rectY2: int, x: int, y: int) -> bool:
        if x >= rectX2 or y >= rectY2 or x <= rectX1 or y <= rectY1:
            return False
        else:
            return True
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor


RectangleCollisionUtil.instance = RectangleCollisionUtil()

