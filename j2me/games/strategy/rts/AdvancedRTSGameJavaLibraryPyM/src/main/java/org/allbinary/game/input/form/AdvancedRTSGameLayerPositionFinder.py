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
# package org.allbinary.game.input.form

from __future__ import annotations

from org.allbinary.game.input.LayerPositionFinderInterface import LayerPositionFinderInterface


class AdvancedRTSGameLayerPositionFinder(LayerPositionFinderInterface):
    instance: AdvancedRTSGameLayerPositionFinder = None
    

    @staticmethod
    def getInstance() -> AdvancedRTSGameLayerPositionFinder:
        return AdvancedRTSGameLayerPositionFinder.instance
    

    def __init__(self) -> None:
        pass
    

    def getLayerInterface(self, geographicMapCellPosition: GeographicMapCellPosition) -> AllBinaryLayer:
        layerInterface: AllBinaryLayer = DropCellPositionHistory.getInstance().getLayerInterface(geographicMapCellPosition)
        if layerInterface == AllBinaryLayer.NULL_ALLBINARY_LAYER:
            layerInterface = WaypointCellPositionHistory.getInstance().getLayerInterface(geographicMapCellPosition)
        return layerInterface
from org.allbinary.game.layer.waypoint.WaypointCellPositionHistory import WaypointCellPositionHistory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory


AdvancedRTSGameLayerPositionFinder.instance = AdvancedRTSGameLayerPositionFinder()

