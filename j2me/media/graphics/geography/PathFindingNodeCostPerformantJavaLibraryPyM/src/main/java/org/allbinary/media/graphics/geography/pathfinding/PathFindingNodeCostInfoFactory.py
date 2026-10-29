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
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations

from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactoryBase import PathFindingNodeCostInfoFactoryBase


class PathFindingNodeCostInfoFactory(PathFindingNodeCostInfoFactoryBase):
    

    def __init__(self, max: int) -> None:
        super().__init__()
    

    # throws Exception
    def create(self, geographicMapInterface: BasicGeographicMap, goingToGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition, costFromStart: int, costToEnd: int) -> None:
        pass
    

    # throws Exception
    def getTotalCost(self, geographicMapInterface: BasicGeographicMap, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition) -> int:
        geographicMapCellType: GeographicMapCellType = geographicMapInterface.getCellTypeAt(comingFromGeographicMapCellPosition)
        geographicMapCellType2: GeographicMapCellType = geographicMapInterface.getCellTypeAt(geographicMapCellPosition)
        raceTrackGeographicMapCellType: RaceTrackGeographicMapCellType = geographicMapCellType
        raceTrackGeographicMapCellType2: RaceTrackGeographicMapCellType = geographicMapCellType2
        return int(raceTrackGeographicMapCellType.getTravelCost()) + raceTrackGeographicMapCellType2.getTravelCost()
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType


