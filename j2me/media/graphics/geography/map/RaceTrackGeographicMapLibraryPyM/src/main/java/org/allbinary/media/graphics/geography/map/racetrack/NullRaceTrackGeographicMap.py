# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapInterface import RaceTrackGeographicMapInterface


class NullRaceTrackGeographicMap(RaceTrackGeographicMapInterface):
    NULL_RACE_TRACK_GEOGRAPHIC_MAP: NullRaceTrackGeographicMap = None
    

    def getId(self) -> int:
        raise RuntimeError()
    

    def getName(self) -> str:
        raise RuntimeError()
    

    def reset(self) -> None:
        raise RuntimeError()
    

    def getAllBinaryTiledLayer(self) -> AllBinaryTiledLayer:
        raise RuntimeError()
    

    # throws Exception
    def getCellPositionsAt(self, layer: Layer, currentCellPositionArray: list[list[GeographicMapCellPosition]], cellPositionArray: list[list[GeographicMapCellPosition]]) -> bool:
        raise RuntimeError()
    

    # throws Exception
    def getCellPositionAtXY(self, x: int, y: int) -> GeographicMapCellPosition:
        raise RuntimeError()
    

    # throws Exception
    def getCellPositionAtXYNoThrow(self, x: int, y: int) -> GeographicMapCellPosition:
        raise RuntimeError()
    

    def getCellTypeFromMapCellTypeInt(self, cellTypeId: int) -> int:
        raise RuntimeError()
    

    # throws Exception
    def getCellTypeAtXY(self, x: int, y: int) -> GeographicMapCellType:
        raise RuntimeError()
    

    # throws Exception
    def getCellTypeAt(self, geographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellType:
        raise RuntimeError()
    

    def getGeographicMapCellPositionFactory(self) -> BasicGeographicMapCellPositionFactory:
        raise RuntimeError()
    

    def getGeographicMapCellPositionFactoryInterface(self) -> GeographicMapCellPositionFactoryInterface:
        raise RuntimeError()
    

    def getForegroundBasicColor(self) -> BasicColor:
        raise RuntimeError()
    

    def getBackgroundBasicColor(self) -> BasicColor:
        raise RuntimeError()
    

    def getRaceTrackInfo(self) -> RaceTrackInfo:
        raise RuntimeError()
    

    def setRaceTrackInfo(self, aRaceTrackInfo: RaceTrackInfo) -> None:
        raise RuntimeError()
    

    def getRaceTrackData(self) -> RaceTrackData:
        raise RuntimeError()
    

    def setRaceTrackData(self, raceTrackData: RaceTrackData) -> None:
        raise RuntimeError()
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.layer.Layer import Layer
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


NullRaceTrackGeographicMap.NULL_RACE_TRACK_GEOGRAPHIC_MAP = NullRaceTrackGeographicMap()

