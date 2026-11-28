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
# package org.allbinary.collision

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate


class RectangleCollisionUtil:
    

    def __init__(self) -> None:
        pass
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def isCollision_j2_1(rectangle: Rectangle, point: GPoint) -> bool:
        from org.allbinary.graphics.GPoint import GPoint
        if point.getX() > (int(rectangle.x) + rectangle.getWidth()) or point.getY() > (int(rectangle.y) + rectangle.getHeight()) or point.getX() < rectangle.x or point.getY() < rectangle.y:
            return False
        else:
            return True
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def isCollision_j2_2(rectangle1: Rectangle, rectangle2: Rectangle) -> bool:
        return RectangleCollisionUtil.isCollision(rectangle1.x, rectangle1.y, rectangle1.x + rectangle1.width, rectangle1.y + rectangle1.height, rectangle2.x, rectangle2.y, rectangle2.x + rectangle2.width, rectangle2.y + rectangle2.height)
    

    @staticmethod
    def isCollision_j8(rectX1: int, rectY1: int, rectX2: int, rectY2: int, rect2X1: int, rect2Y1: int, rect2X2: int, rect2Y2: int) -> bool:
        if rect2X1 >= rectX2 or rect2Y1 >= rectY2 or rect2X2 <= rectX1 or rect2Y2 <= rectY1:
            return False
        else:
            return True

    @staticmethod
    def isCollision(*args):
        if len(args) == 2 and True and (args[0] is None or any(base.__name__ == "Rectangle" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "GPoint" for base in type(args[1]).__mro__)):
            return RectangleCollisionUtil.isCollision_j2_1(*args)
        if len(args) == 2:
            return RectangleCollisionUtil.isCollision_j2_2(*args)
        return getattr(RectangleCollisionUtil, "isCollision_j" + str(len(args)))(*args)
# from java.awt.Rectangle import Rectangle
# from org.allbinary.graphics.GPoint import GPoint


