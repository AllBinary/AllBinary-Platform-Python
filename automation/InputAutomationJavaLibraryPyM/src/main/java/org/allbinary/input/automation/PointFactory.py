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
# package org.allbinary.input.automation

from __future__ import annotations



class PointFactory:
    pointArray: list[list[Point]] = [[None] * (3000) for _ in range(3000)]
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(x: int, y: int) -> Point:
        from org.allbinary.input.automation.Point import Point
        point: Point = PointFactory.pointArray[x][y]
        if point is None:
            PointFactory.pointArray[x][y] = Point(x, y)
            point = PointFactory.pointArray[x][y]
        return point
# from java.awt import *


