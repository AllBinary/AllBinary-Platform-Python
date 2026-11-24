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

from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactoryBaseInterface import PathFindingNodeCostInfoFactoryBaseInterface


# Java interface
class PathFindingNodeCostInfoFactoryInterface(PathFindingNodeCostInfoFactoryBaseInterface):
    

    # throws Exception
    def getInstance_j4(self, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition, costFromStart: int, costToEnd: int) -> PathFindingNodeCostInfo:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
    

    def getInstance_j2(self, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition) -> PathFindingNodeCostInfo:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
    

    def getTotalCost(self, comingFromGeographicMapCellPosition: GeographicMapCellPosition, geographicMapCellPosition: GeographicMapCellPosition) -> int:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


