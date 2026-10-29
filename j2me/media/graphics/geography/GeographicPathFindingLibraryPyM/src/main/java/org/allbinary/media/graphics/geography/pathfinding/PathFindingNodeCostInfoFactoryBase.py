# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactoryBaseInterface import PathFindingNodeCostInfoFactoryBaseInterface


class PathFindingNodeCostInfoFactoryBase(PathFindingNodeCostInfoFactoryBaseInterface):
    NULL_PATH_FINDING_NODE_COST_INFO_FACTORY_BASE: PathFindingNodeCostInfoFactoryBase = None
    

    # throws Exception
    def create(self, geographicMapInterface: BasicGeographicMap, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition, costFromStart: int, costToEnd: int) -> None:
        raise RuntimeError()
    

    # throws Exception
    def getTotalCost(self, geographicMapInterface: BasicGeographicMap, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition) -> int:
        raise RuntimeError()
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


PathFindingNodeCostInfoFactoryBase.NULL_PATH_FINDING_NODE_COST_INFO_FACTORY_BASE = PathFindingNodeCostInfoFactoryBase()

