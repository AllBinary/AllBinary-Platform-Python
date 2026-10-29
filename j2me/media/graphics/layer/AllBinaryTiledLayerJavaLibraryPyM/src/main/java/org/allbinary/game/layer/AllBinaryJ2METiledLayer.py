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

from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer


class AllBinaryJ2METiledLayer(AllBinaryTiledLayer):

    def _init_fields(self) -> None:
        self.tiledLayerP: TiledLayer = None
        self.debugColor: int = None
        self.font2: Font = Font.getFont(Font.FACE_SYSTEM, Font.STYLE_PLAIN, 4)
    

    def __init__(self, dataId: int, tiledLayer: TiledLayer, mapTwoDArray: list[list[int]], debugColor: int) -> None:
        super().__init__(dataId, tiledLayer.getWidth(), tiledLayer.getHeight(), tiledLayer.getCellWidth(), tiledLayer.getCellHeight())
        self._init_fields()
        self.tiledLayerP = tiledLayer
        self.debugColor = debugColor
        self.setCells(mapTwoDArray)
    

    def paint(self, graphics: Graphics) -> None:
        self.tiledLayerP.paint(graphics)
    

    def paintDebug(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        graphics.setFont(self.font2)
        graphics.setColor(self.debugColor)
        x: int = self.tiledLayerP.getX()
        y: int = self.tiledLayerP.getY()
        firstColumn: int = 0
        firstRow: int = 0
        totalColumns: int = self.tiledLayerP.getColumns()
        totalRows: int = self.tiledLayerP.getRows()
        x0: int = x
        tile: int = 0
        tileHeight: int = self.tiledLayerP.getCellHeight()
        tileWidth: int = self.tiledLayerP.getCellWidth()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringMaker: StringMaker = StringMaker()
        rowIndex = firstRow
        while rowIndex < totalRows:
            # continue skips the update below
            x = x0
            columnIndex = firstColumn
            while columnIndex < totalColumns:
                # continue skips the update below
                tile = self.tiledLayerP.getCell(columnIndex, rowIndex)
                if tile < 0:
                    tile = self.tiledLayerP.getAnimatedTile(tile)
                if tile == 0:
                    continue
                tile -= 1
                stringMaker.delete(0, stringMaker.length())
                graphics.drawString(str(stringMaker.appendint(columnIndex).append(commonSeps.COMMA).appendint(rowIndex).append(commonSeps.COLON).appendint(tile)), x + 5, y + 10, 0)
                columnIndex += 1
                x += tileWidth
            rowIndex += 1
            y += tileHeight
        graphics.setFont(font)
    

    def moveDXY(self, dx: int, dy: int) -> None:
        self.tiledLayerP.move(dx, dy)
        super().moveDXY(-dx, -dy)
    

    def setPosition(self, x: int, y: int, z: int) -> None:
        self.tiledLayerP.setPosition(x, y)
        super().setPosition(-x, -y, z)
    

    def getTiledLayer(self) -> TiledLayer:
        return self.tiledLayerP
    

    def getCellWidth(self) -> int:
        return self.tiledLayerP.getCellWidth()
    

    def getCellHeight(self) -> int:
        return self.tiledLayerP.getCellHeight()
    

    def getCell(self, col: int, row: int) -> int:
        return self.tiledLayerP.getCell(col, row)
    

    def getColumns(self) -> int:
        return self.tiledLayerP.getColumns()
    

    def getRows(self) -> int:
        return self.tiledLayerP.getRows()
    

    def setCell(self, col: int, row: int, index: int) -> None:
        self.tiledLayerP.setCell(col, row, index)
    

    def getAnimatedTile(self, animationTileIndex: int) -> int:
        return self.tiledLayerP.getAnimatedTile(animationTileIndex)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.game.TiledLayer import TiledLayer
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker


