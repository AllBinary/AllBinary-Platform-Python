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
# package org.allbinary.media.graphics.geography.map.racetrack.drop

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.drop.BaseDropCellPositionGenerator import BaseDropCellPositionGenerator


class RaceTrackDropCellPositionGenerator(BaseDropCellPositionGenerator):

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
        self.timeDelayHelper: TimeDelayHelper = None
        self.STRAIGHTAWAY: int = 4
        self.raceTrackGeographicMap: RaceTrackGeographicMapInterface = NullRaceTrackGeographicMap.NULL_RACE_TRACK_GEOGRAPHIC_MAP
        self.raceTrackGeographicMapCellTypeFactory: GeographicMapCellTypeFactory = GeographicMapCellTypeFactory.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.timeDelayHelper = TimeDelayHelper(10000)
    

    def init(self) -> None:
        self.list_.clear()
    

    # throws Exception
    def isDropAllowedAt(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        raceTrackGeographicMapCellType: RaceTrackGeographicMapCellType = self.raceTrackGeographicMap.getCellTypeAt(geographicMapCellPosition)
        raceTrackGeographicMapCellTypeFactory: RaceTrackGeographicMapCellTypeFactory = self.raceTrackGeographicMapCellTypeFactory
        if raceTrackGeographicMapCellType == raceTrackGeographicMapCellTypeFactory.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE or raceTrackGeographicMapCellType == raceTrackGeographicMapCellTypeFactory.VERTICAL_STRAIGHT_ROAD_CELL_TYPE:
            return True
        return False
    

    # throws Exception
    def update(self, allBinaryGameLayerManager: AllBinaryGameLayerManager, geographicMapInterface: BasicGeographicMap) -> None:
        self.init()
        baseRaceTrackGeographicMap: BaseRaceTrackGeographicMap = geographicMapInterface
        self.raceTrackGeographicMap = baseRaceTrackGeographicMap
        self.raceTrackGeographicMapCellTypeFactory = baseRaceTrackGeographicMap.getGeographicMapCellTypeFactory()
        roadGeographicMapCellHistory: GeographicMapCellHistory = RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance()
        trackedList: BasicArrayList = roadGeographicMapCellHistory.getTracked()
        geographicMapCellPosition: GeographicMapCellPosition = None
        lastIndex: int = trackedList.size() - 1
        total: int = 0
        ahead: int = 0
        for index in range(lastIndex, 0, -1):
            geographicMapCellPosition = trackedList.get(index)
            total = 0
            ahead = index
            while self.isDropAllowedAt(trackedList.get(ahead)):
                total += 1
                if total > self.STRAIGHTAWAY:
                    self.list_.add(geographicMapCellPosition)
                    break
                ahead += 1
                if ahead > lastIndex:
                    break
        size: int = self.list_.size()
        for index in range(size - 1, 0 - 1, -1):
            self.drop(allBinaryGameLayerManager, index)
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            index: int = self.basicArrayListUtil.getRandomIndex(self.list_)
            self.drop(allBinaryLayerManager, index)
    

    # throws Exception
    def drop(self, allBinaryLayerManager: AllBinaryLayerManager, index: int) -> None:
        raise Exception(CommonStrings.getInstance().NOT_IMPLEMENTED)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.racetrack.BaseRaceTrackGeographicMap import BaseRaceTrackGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.NullRaceTrackGeographicMap import NullRaceTrackGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypeFactory import RaceTrackGeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapInterface import RaceTrackGeographicMapInterface
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


