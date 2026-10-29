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

    def _init_fields(self) -> None:
        self.MAX_DIRECTIONS: int = 4
        self.pathFindingInfo: PathFindingInfo = None
        self.basicGeographicMapGraph: BasicGeographicMapGraph = None
        self.basicGeographicMapPathFinder: BasicGeographicMapPathFinder = None
        self.pathFinderGraphVisitorFactoryInterface: PathFinderGraphVisitorFactoryBase = None
    

    @staticmethod
    def getInstance() -> PathFindingInfoFactory:
        return PathFindingInfoFactory.instance
    

    @staticmethod
    def initMax(max: int) -> None:
        from org.allbinary.game.media.graphics.geography.map.racetrack.SimplePathFinderGraphVisitorFactory import SimplePathFinderGraphVisitorFactory
        PathFindingInfoFactory.instance = PathFindingInfoFactory(SimplePathFinderGraphVisitorFactory(1, 1, 2147483647), max)
    

    def __init__(self, pathFinderGraphVisitorFactoryInterface: PathFinderGraphVisitorFactoryBase, max: int) -> None:
        super().__init__()
        self._init_fields()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        PreLogUtil.put("Using Dynamic Path Finding", self, commonStrings.GET_INSTANCE)
        self.basicGeographicMapPathFinder = BasicGeographicMapPathFinder(max)
        self.pathFindingInfo = PathFindingInfo(PathFindingNodeCostInfoFactory(max), BasicArrayListS(1), BasicArrayListS(1))
        self.basicGeographicMapGraph = BasicGeographicMapGraph(self.pathFindingInfo.getPathFindingNodeCostInfoFactoryInterface())
        self.pathFinderGraphVisitorFactoryInterface = pathFinderGraphVisitorFactoryInterface
    

    # throws Exception
    def getInstancePathFindingInfo(self, geographicMapInterface: BasicGeographicMap, mapArray: list[list[int]]) -> PathFindingInfo:
        pathFindingInfo: PathFindingInfo = PathFindingInfo(self.pathFindingInfo.getPathFindingNodeCostInfoFactoryInterface(), BasicArrayListS(1), BasicArrayListS(1))
        RaceTrackRoadsGeographicMapCellHistoryFactory.getInstance().init()
        self.init(geographicMapInterface, pathFindingInfo, mapArray)
        self.basicGeographicMapPathFinder.init(geographicMapInterface, self.basicGeographicMapGraph, self.pathFinderGraphVisitorFactoryInterface.getInstance(geographicMapInterface))
        pathFindingInfo.setPathFinder(self.basicGeographicMapPathFinder)
        return pathFindingInfo
    

    # throws Exception
    def init(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
        super().init(geographicMapInterface, pathFindingInfo, mapArray)
        self.buildPathFindingNodes(geographicMapInterface, pathFindingInfo, mapArray)
    

    # throws Exception
    def buildPathFindingNodesForCellPosition(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]], cellPosition: GeographicMapCellPosition) -> None:
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        cellTypeId: int = mapArray[cellPosition.getRow()][cellPosition.getColumn()]
        geographicMapCellType: GeographicMapCellType = GeographicMapCellTypeFactory.getInstance().get(geographicMapInterface.getCellTypeFromMapCellTypeInt(cellTypeId))
        raceTrackGeographicMapCellType: RaceTrackGeographicMapCellType = geographicMapCellType
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        pathFindingNodeCostInfoFactoryInterface: PathFindingNodeCostInfoFactoryBase = pathFindingInfo.getPathFindingNodeCostInfoFactoryInterface()
        basicGeographicMapUtil: BasicGeographicMapUtil = BasicGeographicMapUtil.getInstance()
        row: int = 0
        column: int = 0
        goingToGeographicMapCellPosition: GeographicMapCellPosition = None
        costFromStart: int = 0
        costToEnd: int = 0
        for index in range(0, self.MAX_DIRECTIONS):
            row = basicGeographicMapUtil.getBorderingRow(index, cellPosition)
            column = basicGeographicMapUtil.getBorderingColumn(index, cellPosition)
            if row < allBinaryTiledLayer.getRows() and column < allBinaryTiledLayer.getColumns() and row >= 0 and column >= 0:
                goingToGeographicMapCellPosition = geographicMapCellPositionFactory.getAt(column, row)
                costFromStart = raceTrackGeographicMapCellType.getTravelCost()
                costToEnd = costFromStart
                pathFindingNodeCostInfoFactoryInterface.create(geographicMapInterface, goingToGeographicMapCellPosition, cellPosition, costFromStart, costToEnd)
    

    # throws Exception
    def buildPathFindingNodes(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, mapArray: list[list[int]]) -> None:
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        totalColumns: int = allBinaryTiledLayer.getColumns()
        totalRows: int = allBinaryTiledLayer.getRows()
        for column in range(0, totalColumns):
            for row in range(0, totalRows):
                self.buildPathFindingNodesForCellPosition(geographicMapInterface, pathFindingInfo, mapArray, geographicMapCellPositionFactory.getAt(column, row))
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMapUtil import BasicGeographicMapUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackRoadsGeographicMapCellHistoryFactory import RaceTrackRoadsGeographicMapCellHistoryFactory
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactoryBase import PathFindingNodeCostInfoFactoryBase
from org.allbinary.media.graphics.geography.pathfinding.BasicGeographicMapGraph import BasicGeographicMapGraph
from org.allbinary.media.graphics.geography.pathfinding.BasicGeographicMapPathFinder import BasicGeographicMapPathFinder
from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorFactoryBase import PathFinderGraphVisitorFactoryBase
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactory import PathFindingNodeCostInfoFactory
from org.allbinary.util.BasicArrayListS import BasicArrayListS


