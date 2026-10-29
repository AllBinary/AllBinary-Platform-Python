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
# package org.allbinary.game.view

from __future__ import annotations

from org.allbinary.view.ViewPosition import ViewPosition


class TileLayerPositionIntoViewPosition(ViewPosition):

    def _init_fields(self) -> None:
        self.tiledLayer: Layer = NullLayer.getInstance()
    

    def __init__(self) -> None:
        super().__init__(0, 0, 0)
        self._init_fields()
    

    def getX(self) -> int:
        return super().getX() - self.tiledLayer.getXP()
    

    def getY(self) -> int:
        return super().getY() - self.tiledLayer.getYP()
    

    def getZ(self) -> int:
        return super().getZ() - self.tiledLayer.getZP()
    

    def setTiledLayer(self, tiledLayer: AllBinaryTiledLayer) -> None:
        self.tiledLayer = tiledLayer
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.layer.Layer import Layer
from org.allbinary.layer.NullLayer import NullLayer


