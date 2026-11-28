# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.layer.Layer import Layer
from org.allbinary.layer.NamedInterface import NamedInterface


@java_inherited_overloads
class AllBinaryTiledLayer(*java_bases(Layer, NamedInterface, PaintableInterface)):
    def _java_defaults(self):
        vars(self).setdefault("cellWidth", 0)
        vars(self).setdefault("cellHeight", 0)
        vars(self).setdefault("halfWidth", 0)
        vars(self).setdefault("halfHeight", 0)
        vars(self).setdefault("halfCellWidth", 0)
        vars(self).setdefault("halfCellHeight", 0)
        vars(self).setdefault("dataId", None)

    def _init_fields(self) -> None:
        if "cellWidth" not in vars(self): self.cellWidth: int = 0
        if "cellHeight" not in vars(self): self.cellHeight: int = 0
        if "halfWidth" not in vars(self): self.halfWidth: int = 0
        if "halfHeight" not in vars(self): self.halfHeight: int = 0
        if "halfCellWidth" not in vars(self): self.halfCellWidth: int = 0
        if "halfCellHeight" not in vars(self): self.halfCellHeight: int = 0
        if "dataId" not in vars(self): self.dataId: int = None
    

    def __init__(self, dataId: int, width: int, height: int, cellWidth: int, cellHeight: int) -> None:
        __class__._java_defaults(self)
        super().__init__(0, 0)
        __class__._init_fields(self)
        self.dataId = dataId
        self.setLayerWidth(width)
        self.setLayerHeight(height)
        java_super_call(super(), "setPosition", 0, 0, 0)
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.halfWidth = (self.getWidth() >> 1)
        self.halfHeight = (self.getHeight() >> 1)
        self.halfCellWidth = (int(cellWidth) >> (int(1) & 31))
        self.halfCellHeight = (int(cellHeight) >> (int(1) & 31))
    

    def setCells(self, mapTwoDArray: list[list[int]]) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Start: r: ")
        stringBuffer.appendint(len(mapTwoDArray))
        stringBuffer.append(" c: ")
        stringBuffer.appendint(len(mapTwoDArray[0]))
        stringBuffer.append(" rows: ")
        stringBuffer.appendint(self.getRows())
        stringBuffer.append(" columns: ")
        stringBuffer.appendint(self.getColumns())
        self.logUtil.putF(str(stringBuffer), self, "setCells")
        rows: int = self.getRows()
        columns: int = self.getColumns()
        for col in range(0, columns):
            for row in range(0, rows):
                self.setCell(col, row, mapTwoDArray[row][col])
    

    def updateCells(self, mapTwoDArray: list[list[int]], fromTileId: int, toTileId: int) -> None:
        rows: int = self.getRows()
        columns: int = self.getColumns()
        for col in range(0, columns):
            for row in range(0, rows):
                if fromTileId == mapTwoDArray[row][col]:
                    mapTwoDArray[row][col] = toTileId
                    self.setCell(col, row, mapTwoDArray[row][col])
    

    def getName(self) -> str:
        return __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self))
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def getX2(self) -> int:
        return self.x + self.getWidth()
    

    def getY2(self) -> int:
        return self.y + self.getHeight()
    

    def getZ2(self) -> int:
        return int((self.z + self.getDepth()))
    

    def getCellWidth(self) -> int:
        return self.cellWidth
    

    def getCellHeight(self) -> int:
        return self.cellHeight
    

    def getCell(self, col: int, row: int) -> int:
        return -1
    

    def getColumns(self) -> int:
        return -1
    

    def getRows(self) -> int:
        return -1
    

    def setCell(self, col: int, row: int, tileIndex: int) -> None:
        pass
    

    def getHalfWidth(self) -> int:
        return self.halfWidth
    

    def getHalfHeight(self) -> int:
        return self.halfHeight
    

    def getDataId(self) -> int:
        return self.dataId
    

    def getHalfCellWidth(self) -> int:
        return self.halfCellWidth
    

    def getHalfCellHeight(self) -> int:
        return self.halfCellHeight
    

    def isOnTileLayer(self, column: int, row: int) -> bool:
        if self.getColumns() > column and self.getRows() > row and row >= 0 and column >= 0:
            return True
        else:
            return False
    

    def getAnimatedTile(self, animationTileIndex: int) -> int:
        return animationTileIndex
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


