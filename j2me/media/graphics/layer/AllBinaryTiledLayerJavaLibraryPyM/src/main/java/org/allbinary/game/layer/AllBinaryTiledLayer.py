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

from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.layer.Layer import Layer
from org.allbinary.layer.NamedInterface import NamedInterface


class AllBinaryTiledLayer(Layer, NamedInterface, PaintableInterface):

    def _init_fields(self) -> None:
        self.cellWidth: int = None
        self.cellHeight: int = None
        self.halfWidth: int = None
        self.halfHeight: int = None
        self.halfCellWidth: int = None
        self.halfCellHeight: int = None
        self.dataId: int = None
    

    def __init__(self, dataId: int, width: int, height: int, cellWidth: int, cellHeight: int) -> None:
        super().__init__(0, 0)
        self._init_fields()
        self.dataId = dataId
        self.setLayerWidth(width)
        self.setLayerHeight(height)
        super().setPosition(0, 0, 0)
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.halfWidth = (self.getWidth() >> 1)
        self.halfHeight = (self.getHeight() >> 1)
        self.halfCellWidth = (cellWidth >> 1)
        self.halfCellHeight = (cellHeight >> 1)
    

    def setCells(self, mapTwoDArray: list[list[int]]) -> None:
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
        return type(self).__module__ + "." + type(self).__qualname__
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
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
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


