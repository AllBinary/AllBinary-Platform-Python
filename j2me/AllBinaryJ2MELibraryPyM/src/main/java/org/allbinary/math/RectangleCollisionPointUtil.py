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



class RectangleCollisionPointUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def allPointsInside(rectX1: int, rectY1: int, rectX2: int, rectY2: int, list_: BasicArrayList) -> bool:
        from org.allbinary.math.RectangleCollisionUtil import RectangleCollisionUtil
        rectangleCollisionUtil: RectangleCollisionUtil = RectangleCollisionUtil.getInstance()
        point: GPoint = None
        index = list_.size()
        while (index := index - 1) >= 0:
            point = list_.objectArray[index]
            if not rectangleCollisionUtil.isInside(rectX1, rectY1, rectX2, rectY2, point.getX(), point.getY()):
                return False
        return True
    

    @staticmethod
    def allPointsInsideCell(rectX1: int, rectY1: int, rectX2: int, rectY2: int, list_: BasicArrayList, xCellSize: int, yCellSize: int) -> bool:
        from org.allbinary.math.RectangleCollisionUtil import RectangleCollisionUtil
        rectangleCollisionUtil: RectangleCollisionUtil = RectangleCollisionUtil.getInstance()
        point: GPoint = None
        index = list_.size()
        while (index := index - 1) >= 0:
            point = list_.objectArray[index]
            if not rectangleCollisionUtil.isInside(rectX1, rectY1, rectX2, rectY2, point.getX() * xCellSize, point.getY() * yCellSize):
                return False
        return True
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.util.BasicArrayList import BasicArrayList


