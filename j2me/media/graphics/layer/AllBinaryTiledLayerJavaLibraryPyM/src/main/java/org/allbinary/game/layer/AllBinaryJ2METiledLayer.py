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
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer


@java_inherited_overloads
class AllBinaryJ2METiledLayer(AllBinaryTiledLayer):
    def _java_defaults(self):
        vars(self).setdefault("tiledLayerP", None)
        vars(self).setdefault("debugColor", 0)
        vars(self).setdefault("font2", None)

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Font import Font
        if "tiledLayerP" not in vars(self): self.tiledLayerP: TiledLayer = None
        if "debugColor" not in vars(self): self.debugColor: int = 0
        self.font2: Font = Font.getFont(Font.FACE_SYSTEM, Font.STYLE_PLAIN, 4)
    

    def __init__(self, dataId: int, tiledLayer: TiledLayer, mapTwoDArray: list[list[int]], debugColor: int) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.game.TiledLayer import TiledLayer
        super().__init__(dataId, tiledLayer.getWidth(), tiledLayer.getHeight(), tiledLayer.getCellWidth(), tiledLayer.getCellHeight())
        __class__._init_fields(self)
        self.tiledLayerP = tiledLayer
        self.debugColor = debugColor
        self.setCells(mapTwoDArray)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.tiledLayerP.paint(graphics)
    

    def paintDebug(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.string.StringMaker import StringMaker
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
        java_super_call(super(), "moveDXY", -dx, -dy)
    

    def setPosition(self, x: int, y: int, z: int) -> None:
        self.tiledLayerP.setPosition(x, y)
        java_super_call(super(), "setPosition", -x, -y, z)
    

    def getTiledLayer(self) -> TiledLayer:
        from javax.microedition.lcdui.game.TiledLayer import TiledLayer
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
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.string.StringMaker import StringMaker


