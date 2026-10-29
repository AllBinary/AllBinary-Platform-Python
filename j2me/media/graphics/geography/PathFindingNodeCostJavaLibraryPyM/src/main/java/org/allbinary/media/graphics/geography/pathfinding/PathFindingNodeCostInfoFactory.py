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

    def _init_fields(self) -> None:
        self.pathFindingNodeCostInfoAdjacencyList: list[list[PathFindingNodeCostInfo]] = None
    

    def __init__(self, max: int) -> None:
        super().__init__()
        self._init_fields()
        self.pathFindingNodeCostInfoAdjacencyList = [[None] * (max) for _ in range(max)]
    

    # throws Exception
    def create(self, geographicMapInterface: BasicGeographicMap, goingToGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition, costFromStart: int, costToEnd: int) -> None:
        self.getInstance(goingToGeographicMapCellPosition, geographicMapCellPosition, costFromStart, costToEnd)
    

    # throws Exception
    def getInstance(self, goingToGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition, costFromStart: int, costToEnd: int) -> PathFindingNodeCostInfo:
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfo import PathFindingNodeCostInfo
        pathFindingNodeCostInfo: PathFindingNodeCostInfo = self.getInstance(goingToGeographicMapCellPosition, geographicMapCellPosition)
        if pathFindingNodeCostInfo is None:
            pathFindingNodeCostInfo = PathFindingNodeCostInfo(costFromStart, costToEnd)
            pathFindingNodeCostInfo.setCalculatedTotalCost()
            self.pathFindingNodeCostInfoAdjacencyList[geographicMapCellPosition.getId()][goingToGeographicMapCellPosition.getId()] = pathFindingNodeCostInfo
        else:
            pathFindingNodeCostInfo.setCostFromStart(costFromStart)
            pathFindingNodeCostInfo.setCostToEnd(costToEnd)
            pathFindingNodeCostInfo.setCalculatedTotalCost()
        return pathFindingNodeCostInfo
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, goingToFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition) -> PathFindingNodeCostInfo:
        return self.pathFindingNodeCostInfoAdjacencyList[geographicMapCellPosition.getId()][goingToFromGeographicMapCellPosition.getId()]
    

    def getTotalCost(self, geographicMapInterface: BasicGeographicMap, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition) -> int:
        return self.getInstance(comingFromGeographicMapCellPosition, geographicMapCellPosition).totalCostP
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


