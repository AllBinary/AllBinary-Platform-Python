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


#1.4.2
class PathFindingInfoFactory(BasePathFindingInfoFactory):
    instance: PathFindingInfoFactory = None
    MAX: int = 32768

    def _init_fields(self) -> None:
        self.pathFindingInfo: PathFindingInfo = None
        self.pathFinder: PathFinder = None
    

    @staticmethod
    def getInstance() -> PathFindingInfoFactory:
        return PathFindingInfoFactory.instance
    

    @staticmethod
    def initMax(max: int) -> None:
        PathFindingInfoFactory.MAX = max
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.pathFindingInfo = PathFindingInfo(PathFindingNodeCostInfoFactory(PathFindingInfoFactory.MAX), BasicArrayListS(1), BasicArrayListS(1))
        self.pathFinder = PathFinder()
    

    # throws Exception
    def getInstancePathFindingInfo(self, geographicMapInterface: BasicGeographicMap, mapArray: list[list[int]]) -> PathFindingInfo:
        pathFindingInfo: PathFindingInfo = PathFindingInfo(self.pathFindingInfo.getPathFindingNodeCostInfoFactoryInterface(), BasicArrayListS(1), BasicArrayListS(1))
        RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance().init()
        self.init(geographicMapInterface, pathFindingInfo, mapArray)
        self.pathFinder.init(geographicMapInterface)
        pathFindingInfo.setPathFinder(self.pathFinder)
        return pathFindingInfo
    

    # throws Exception
    def init(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
        super().init(geographicMapInterface, pathFindingInfo, mapArray)
        self.buildPathFindingNodes(geographicMapInterface, pathFindingInfo, mapArray)
    

    # throws Exception
    def buildPathFindingNodesForCellPosition(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]], cellPosition: GeographicMapCellPosition) -> None:
        pass
    

    # throws Exception
    def buildPathFindingNodes(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        totalColumns: int = allBinaryTiledLayer.getColumns()
        totalRows: int = allBinaryTiledLayer.getRows()
        for column in range(0, totalColumns):
            for row in range(0, totalRows):
                self.buildPathFindingNodesForCellPosition(geographicMapInterface, pathFindingInfo, mapArray, geographicMapCellPositionFactory.getAt(column, row))
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
from org.allbinary.media.graphics.geography.pathfinding.PathFinder import PathFinder
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactory import PathFindingNodeCostInfoFactory
from org.allbinary.util.BasicArrayListS import BasicArrayListS


PathFindingInfoFactory.instance = PathFindingInfoFactory()

