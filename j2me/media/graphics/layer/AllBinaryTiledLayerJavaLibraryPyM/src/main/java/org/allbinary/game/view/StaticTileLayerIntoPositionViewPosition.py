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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.view.ViewPosition import ViewPosition


class StaticTileLayerIntoPositionViewPosition(ViewPosition):
    tiledLayer: Layer = None
    layer: AllBinaryLayer = None
    

    def __init__(self) -> None:
        super().__init__(0, 0, 0)
    

    def getX(self) -> int:
        return super().getX() - StaticTileLayerIntoPositionViewPosition.tiledLayer.getXP()
    

    def getY(self) -> int:
        return super().getY() - StaticTileLayerIntoPositionViewPosition.tiledLayer.getYP()
    

    def getZ(self) -> int:
        return super().getZ() - StaticTileLayerIntoPositionViewPosition.tiledLayer.getZP()
    

    @staticmethod
    def setTiledLayer(tiledLayer: AllBinaryTiledLayer) -> None:
        from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
        StaticTileLayerIntoPositionViewPosition.tiledLayer = tiledLayer
# from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.Layer import Layer
# from org.allbinary.layer.NullLayer import NullLayer


def _StaticTileLayerIntoPositionViewPosition_tiledLayer() -> object:
    from org.allbinary.layer.Layer import Layer
    from org.allbinary.layer.NullLayer import NullLayer
    return NullLayer.getInstance()

lazy_static(StaticTileLayerIntoPositionViewPosition, "tiledLayer", _StaticTileLayerIntoPositionViewPosition_tiledLayer)

def _StaticTileLayerIntoPositionViewPosition_layer() -> object:
    from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
    return AllBinaryLayer.NULL_ALLBINARY_LAYER

lazy_static(StaticTileLayerIntoPositionViewPosition, "layer", _StaticTileLayerIntoPositionViewPosition_layer)

