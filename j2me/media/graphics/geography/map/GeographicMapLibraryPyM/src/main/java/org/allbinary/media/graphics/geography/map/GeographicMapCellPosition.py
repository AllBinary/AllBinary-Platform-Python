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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations

from org.allbinary.graphics.CellPosition import CellPosition


class GeographicMapCellPosition(CellPosition):

    def _init_fields(self) -> None:
        self.point: GPoint = None
        self.midPoint: GPoint = None
    

    def __init__(self, column: int, row: int, columns: int, rows: int, width: int, height: int) -> None:
        super().__init__(column, row, columns, rows)
        self._init_fields()
        x: int = self.getColumn() * width
        y: int = self.getRow() * height
        pointFactory: PointFactory = PointFactory.getInstance()
        self.point = pointFactory.createXY(x, y)
        self.midPoint = pointFactory.createXY(x + (width >> 1), y + (height >> 1))
    

    def getPoint(self) -> GPoint:
        return self.point
    

    def getMidPoint(self) -> GPoint:
        return self.midPoint
    

    def setMidPoint(self, midPoint: GPoint) -> None:
        self.midPoint = midPoint
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory


