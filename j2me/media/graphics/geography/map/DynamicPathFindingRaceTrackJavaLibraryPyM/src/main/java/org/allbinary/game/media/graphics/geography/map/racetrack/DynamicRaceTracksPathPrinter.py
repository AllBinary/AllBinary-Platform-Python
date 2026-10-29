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
# package org.allbinary.game.media.graphics.geography.map.racetrack

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.racetrack.RaceTracksPathPrinter import RaceTracksPathPrinter


class DynamicRaceTracksPathPrinter(RaceTracksPathPrinter):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def printAllPaths(self, raceTrackGeographicMapInterfaceFactoryInterface: RaceTrackGeographicMapInterfaceFactoryInterface, pathFindingInfo: PathFindingInfo, size: int) -> None:
        try:
            for index in range(0, size):
                geographicMapInterface: BasicGeographicMap = raceTrackGeographicMapInterfaceFactoryInterface.getTrackInstance(SmallIntegerSingletonFactory.getInstance().getAt(index))
                list_: BasicArrayList = PathGenerator.getInstance().createList(geographicMapInterface, RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance(), pathFindingInfo, 10)
                print("Track " + str(index))
                self.printPaths(list_)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.PROCESS, e)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapInterfaceFactoryInterface import RaceTrackGeographicMapInterfaceFactoryInterface
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathGenerator import PathGenerator


