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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.CellPosition import CellPosition


@java_inherited_overloads
class GeographicMapCellPosition(CellPosition):
    def _java_defaults(self):
        vars(self).setdefault("point", None)
        vars(self).setdefault("midPoint", None)

    def _init_fields(self) -> None:
        if "point" not in vars(self): self.point: GPoint = None
        if "midPoint" not in vars(self): self.midPoint: GPoint = None
    

    def __init__(self, column: int, row: int, columns: int, rows: int, width: int, height: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.PointFactory import PointFactory
        super().__init__(column, row, columns, rows)
        __class__._init_fields(self)
        x: int = self.getColumn() * width
        y: int = self.getRow() * height
        pointFactory: PointFactory = PointFactory.getInstance()
        self.point = pointFactory.createXY(x, y)
        self.midPoint = pointFactory.createXY(x + (int(width) >> (int(1) & 31)), y + (int(height) >> (int(1) & 31)))
    

    def getPoint(self) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        return self.point
    

    def getMidPoint(self) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        return self.midPoint
    

    def setMidPoint(self, midPoint: GPoint) -> None:
        from org.allbinary.graphics.GPoint import GPoint
        self.midPoint = midPoint
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.PointFactory import PointFactory


