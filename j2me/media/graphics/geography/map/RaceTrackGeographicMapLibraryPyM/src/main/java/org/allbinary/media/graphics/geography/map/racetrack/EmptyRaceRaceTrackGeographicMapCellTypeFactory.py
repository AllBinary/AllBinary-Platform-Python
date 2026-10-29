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

from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypeFactory import RaceTrackGeographicMapCellTypeFactory


class EmptyRaceRaceTrackGeographicMapCellTypeFactory(RaceTrackGeographicMapCellTypeFactory):
    instanceC: EmptyRaceRaceTrackGeographicMapCellTypeFactory = None
    

    @staticmethod
    def getInstance() -> EmptyRaceRaceTrackGeographicMapCellTypeFactory:
        return EmptyRaceRaceTrackGeographicMapCellTypeFactory.instanceC
    

    def __init__(self) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        super().__init__()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.EMPTY_CELL_TYPE = RaceTrackGeographicMapCellType(commonStrings.EMPTY, 0, PathFindingNodeCostInfoData.getInstance().MAX_NODE_COST, 1)
        self.EASY_CELL_TYPE = RaceTrackGeographicMapCellType("Easy", 19, 1, 0)
        self.FINISH_LINE_ROAD_CELL_TYPE = self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoData import PathFindingNodeCostInfoData


EmptyRaceRaceTrackGeographicMapCellTypeFactory.instanceC = EmptyRaceRaceTrackGeographicMapCellTypeFactory()

