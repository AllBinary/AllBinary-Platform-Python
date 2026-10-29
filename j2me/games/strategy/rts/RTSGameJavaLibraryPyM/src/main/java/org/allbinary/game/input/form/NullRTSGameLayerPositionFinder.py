# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.input.form

from __future__ import annotations

from org.allbinary.game.input.LayerPositionFinderInterface import LayerPositionFinderInterface


class NullRTSGameLayerPositionFinder(LayerPositionFinderInterface):
    instance: NullRTSGameLayerPositionFinder = None
    

    @staticmethod
    def getInstance() -> NullRTSGameLayerPositionFinder:
        return NullRTSGameLayerPositionFinder.instance
    

    def __init__(self) -> None:
        pass
    

    def getLayerInterface(self, geographicMapCellPosition: GeographicMapCellPosition) -> AllBinaryLayer:
        layerInterface: AllBinaryLayer = DropCellPositionHistory.getInstance().getLayerInterface(geographicMapCellPosition)
        return layerInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory


NullRTSGameLayerPositionFinder.instance = NullRTSGameLayerPositionFinder()

