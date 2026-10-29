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

from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.form.item.ABCustomItemInterface import ABCustomItemInterface


class TileLayerItem(ABCustomItem, ABCustomItemInterface):

    def _init_fields(self) -> None:
        self.tiledLayer: AllBinaryTiledLayer = None
    

    def __init__(self, label: str, tiledLayer: AllBinaryTiledLayer, layout: int, altText: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(label, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.tiledLayer = tiledLayer
    

    def setOwner(self, owner: Screen) -> None:
        pass
    

    def getMinimumWidth(self) -> int:
        return self.tiledLayer.getWidth()
    

    def getMinimumHeight(self) -> int:
        return self.tiledLayer.getHeight()
    

    def getMinContentHeight(self) -> int:
        return self.tiledLayer.getHeight()
    

    def getMinContentWidth(self) -> int:
        return self.tiledLayer.getWidth()
    

    def getPrefContentHeight(self, width: int) -> int:
        return self.tiledLayer.getHeight()
    

    def getPrefContentWidth(self, height: int) -> int:
        return self.tiledLayer.getWidth()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.tiledLayer.setPosition(x, y, self.tiledLayer.getZP())
        self.tiledLayer.paint(graphics)
    

    def paintUnselected(self, graphics: Graphics, x: int, y: int) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Screen import Screen
from org.allbinary.graphics.color.BasicColor import BasicColor


