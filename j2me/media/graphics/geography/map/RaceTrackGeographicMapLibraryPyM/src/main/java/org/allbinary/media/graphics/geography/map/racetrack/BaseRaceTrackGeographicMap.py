#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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

from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapInterface import RaceTrackGeographicMapInterface


class BaseRaceTrackGeographicMap(BasicGeographicMap, RaceTrackGeographicMapInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.raceTrackInfo: RaceTrackInfo = None
        self.raceTrackData: RaceTrackData = None
        self.miniGeographicMap: BasicGeographicMap = None
    

    def __init__(self, raceTrackInfo: RaceTrackInfo, raceTrackData: RaceTrackData, tiledLayer: AllBinaryTiledLayer, miniGeographicMap: BasicGeographicMap, geographicMapCellPositionFactoryInterface: GeographicMapCellPositionFactoryInterface, geographicMapCellPositionBaseFactory: GeographicMapCellPositionBaseFactory, geographicMapCellTypeFactory: GeographicMapCellTypeFactory) -> None:
        super().__init__(raceTrackInfo.getId(), raceTrackInfo.getName(), raceTrackData.getCellTypeIdToGeographicMapCellTypeArray(), tiledLayer, raceTrackInfo.getForegroundBasicColor(), raceTrackInfo.getBackgroundBasicColor(), geographicMapCellPositionFactoryInterface, geographicMapCellPositionBaseFactory, geographicMapCellTypeFactory)
        self._init_fields()
        self.raceTrackInfo = raceTrackInfo
        self.raceTrackData = raceTrackData
        self.miniGeographicMap = miniGeographicMap
        miniTiledLayer: AllBinaryTiledLayer = self.miniGeographicMap.getAllBinaryTiledLayer()
        if miniTiledLayer.getColumns() != self.getGeographicMapCellPositionFactory().getColumns():
            error: str = str(StringMaker().append("RaceTrackMap has incorrect Mini Map columns: ").appendint(int(miniTiledLayer.getColumns())).append(" != ").appendint(int(self.getGeographicMapCellPositionFactory().getColumns())))
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR)
            raise Exception(error)
        if miniTiledLayer.getRows() != self.getGeographicMapCellPositionFactory().getRows():
            error: str = "RaceTrackMap has incorrect Mini Map rows"
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR)
            raise Exception(error)
    

    def getRaceTrackInfo(self) -> RaceTrackInfo:
        return self.raceTrackInfo
    

    def setRaceTrackInfo(self, aRaceTrackInfo: RaceTrackInfo) -> None:
        self.raceTrackInfo = aRaceTrackInfo
    

    def setMiniBasicGeographicMap(self, miniBasicGeographicMap: BasicGeographicMap) -> None:
        self.miniGeographicMap = miniBasicGeographicMap
    

    def getMiniBasicGeographicMap(self) -> BasicGeographicMap:
        return self.miniGeographicMap
    

    def getRaceTrackData(self) -> RaceTrackData:
        return self.raceTrackData
    

    def setRaceTrackData(self, raceTrackData: RaceTrackData) -> None:
        self.raceTrackData = raceTrackData
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionBaseFactory import GeographicMapCellPositionBaseFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


