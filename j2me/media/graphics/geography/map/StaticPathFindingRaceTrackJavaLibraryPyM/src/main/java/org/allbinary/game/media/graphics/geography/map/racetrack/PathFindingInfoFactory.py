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

from org.allbinary.media.graphics.geography.map.racetrack.BasePathFindingInfoFactory import BasePathFindingInfoFactory


class PathFindingInfoFactory(BasePathFindingInfoFactory):
    instance: PathFindingInfoFactory = None
    

    @staticmethod
    def getInstance() -> PathFindingInfoFactory:
        return PathFindingInfoFactory.instance
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def getInstancePathFindingInfo(self, geographicMapInterface: BasicGeographicMap, graphArray: list[list[int]]) -> PathFindingInfo:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        PreLogUtil.put(commonStrings.START, self, commonStrings.GET_INSTANCE)
        pathFindingInfo: PathFindingInfo = PathFindingInfo(PathFindingNodeCostInfoFactoryBase(), BasicArrayListS(1), BasicArrayListS(1))
        RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance().init()
        self.init(geographicMapInterface, pathFindingInfo, graphArray)
        return pathFindingInfo
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactoryBase import PathFindingNodeCostInfoFactoryBase
from org.allbinary.util.BasicArrayListS import BasicArrayListS


PathFindingInfoFactory.instance = PathFindingInfoFactory()

