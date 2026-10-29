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
# package org.allbinary.media.graphics.geography.map.racetrack

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGeneratorBase import CustomMapGeneratorBase


class CustomMapGenerator(CustomMapGeneratorBase):

    def _init_fields(self) -> None:
        self.customMapArray: list[list[int]] = None
        self.raceTrackGeographicMap: RaceTrackGeographicMap = None
        self.geographicMapCellTypeFactory: GeographicMapCellTypeFactory = None
        self.dropCellPositionHistory: DropCellPositionHistory = DropCellPositionHistory.getInstance()
    

    def __init__(self, raceTrackGeographicMap: RaceTrackGeographicMap) -> None:
        super().__init__()
        self._init_fields()
        self.raceTrackGeographicMap = raceTrackGeographicMap
        self.geographicMapCellTypeFactory = self.raceTrackGeographicMap.getGeographicMapCellTypeFactory()
        mapArray: list[list[int]] = raceTrackGeographicMap.getRaceTrackData().getMapArray()
        size2: int = len(mapArray[0])
        self.customMapArray = [[0] * (size2) for _ in range(len(mapArray))]
        if len(mapArray) != len(self.customMapArray) or len(mapArray[0]) != len(self.customMapArray[0]):
            raise Exception("Array Incorrect")
    

    # throws Exception
    def copyMapIntoCustomMap(self) -> None:
        mapArray: list[list[int]] = self.raceTrackGeographicMap.getRaceTrackData().getMapArray()
        startIndex2: int = len(mapArray[0]) - 1
        for index in range(len(mapArray) - 1, 0 - 1, -1):
            for index2 in range(startIndex2, 0 - 1, -1):
                self.customMapArray[index][index2] = self.getCustomType(index2, index, mapArray[index][index2])
    

    # throws Exception
    def getCustomType(self, column: int, row: int, currentType: int) -> int:
        emptyType: int = self.geographicMapCellTypeFactory.getEmptyType()
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = self.raceTrackGeographicMap.getGeographicMapCellPositionFactory()
        cellPosition: CellPosition = geographicMapCellPositionFactory.getAt(column, row)
        if self.dropCellPositionHistory.isCellPositionWithDrop(cellPosition):
            layer: AllBinaryLayer = self.dropCellPositionHistory.getLayerInterface(cellPosition)
            if layer == AllBinaryLayer.NULL_ALLBINARY_LAYER:
                return emptyType
            rtsLayer: AdvancedRTSGameLayer = layer
            if not (rtsLayer.getType() == WaypointLayer.getStaticType()):
                return emptyType
        return currentType
    

    def getCustomMapArray(self) -> list[list[int]]:
        return self.customMapArray
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.waypoint.WaypointLayer import WaypointLayer
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory


