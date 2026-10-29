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
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations

from org.allbinary.media.graphics.geography.pathfinding.GeographicPathFinderBase import GeographicPathFinderBase


class PathFinder(GeographicPathFinderBase):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.mathUtil: MathUtil = MathUtil.getInstance()
        self.openPriorityQueue: PriorityQueue[PathFindingNodeCost] = PriorityQueue()
        self.closedSet: HashSet[PathFindingNodeCost] = HashSet()
        self.geographicMapInterface: object = NullUtil.getInstance().NULL_OBJECT
        self.costArray: list[list[PathFindingNodeCost]] = PathFindingNodeCost.NULL_PATH_FINDING_NODE_COST_ARRAY_ARRAY

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def init(self, geographicMapInterface: BasicGeographicMap) -> None:
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCost import PathFindingNodeCost
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfo import PathFindingNodeCostInfo
        self.geographicMapInterface = geographicMapInterface
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        self.costArray = [[None] * (tiledLayer.getRows()) for _ in range(tiledLayer.getColumns())]
        basicGeographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        node: PathFindingNodeCost = None
        sizeX: int = len(self.costArray)
        sizeY: int = len(self.costArray[0])
        for column in range(0, sizeX):
            for row in range(0, sizeY):
                geographicMapCellType: GeographicMapCellType = geographicMapInterface.getCellTypeAt(basicGeographicMapCellPositionFactory.getAt(column, row))
                raceTrackGeographicMapCellType: RaceTrackGeographicMapCellType = geographicMapCellType
                node = PathFindingNodeCost(NullUtil.getInstance().NULL_OBJECT, basicGeographicMapCellPositionFactory.getAt(column, row), PathFindingNodeCostInfo(int(raceTrackGeographicMapCellType.getTravelCost()), -1))
                self.costArray[column][row] = node
    

    def searchTotalPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, totalPaths: int) -> BasicArrayList:
        try:
            return self.search(startPathFindingNodeList.get(0), endPathFindingNodeList.get(0))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "search", e)
            return self.basicArrayListUtil.getImmutableInstance()
    

    # throws Exception
    def searchTotalPathN(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, totalPaths: int, multipassState: MultipassState) -> BasicArrayList:
        if multipassState.step == 0:
            multipassState.step += 1
        elif multipassState.step == 1:
            self.searchStart(startPathFindingNodeList.get(0), endPathFindingNodeList.get(0), multipassState)
        elif multipassState.step == 2:
            return self.searchN(startPathFindingNodeList.get(0), endPathFindingNodeList.get(0), multipassState)
        return self.basicArrayListUtil.getImmutableInstance()
    

    # throws Exception
    def search(self, startPathFindingNode: PathFindingNode, endPathFindingNode: PathFindingNode) -> BasicArrayList:
        list_: BasicArrayList = self.findPath(startPathFindingNode.geographicMapCellPosition, endPathFindingNode.geographicMapCellPosition)
        pathList: BasicArrayList = BasicArrayListD()
        pathList.add(list_)
        return pathList
    

    # throws Exception
    def searchStart(self, startPathFindingNode: PathFindingNode, endPathFindingNode: PathFindingNode, multipassState: MultipassState) -> None:
        self.findPathStart(startPathFindingNode.geographicMapCellPosition, endPathFindingNode.geographicMapCellPosition, multipassState)
    

    # throws Exception
    def searchN(self, startPathFindingNode: PathFindingNode, endPathFindingNode: PathFindingNode, multipassState: MultipassState) -> BasicArrayList:
        list_: BasicArrayList = self.findPathEnd(startPathFindingNode.geographicMapCellPosition, endPathFindingNode.geographicMapCellPosition, multipassState)
        if list_ is None:
            return self.basicArrayListUtil.getImmutableInstance()
        pathList: BasicArrayList = BasicArrayListD()
        pathList.add(list_)
        multipassState.iteration = 0
        multipassState.step = 0
        return pathList
    

    # throws Exception
    def findPath(self, start: GeographicMapCellPosition, target: GeographicMapCellPosition) -> BasicArrayList:
        self.openPriorityQueue.clear()
        self.closedSet.clear()
        discoveryCalculation: int = 0
        node: PathFindingNodeCost = None
        targetColumn: int = target.getColumn()
        targetRow: int = target.getRow()
        sizeX: int = len(self.costArray)
        sizeY: int = len(self.costArray[0])
        for column in range(0, sizeX):
            for row in range(0, sizeY):
                discoveryCalculation = int(self.mathUtil.abs(column - targetColumn)) + self.mathUtil.abs(row - targetRow)
                node = self.costArray[column][row]
                node.pathFindingNodeCostInfoP.totalCostP = 0
                node.pathFindingNodeCostInfoP.costToEndP = discoveryCalculation
        startNode: PathFindingNodeCost = self.costArray[start.getColumn()][start.getRow()]
        self.openPriorityQueue.add(startNode)
        geographicMapInterface: BasicGeographicMap = self.geographicMapInterface
        basicGeographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        targetNode: PathFindingNodeCost = self.costArray[target.getColumn()][target.getRow()]
        current: PathFindingNodeCost = None
        while True:
            current = self.openPriorityQueue.poll()
            self.closedSet.add(current)
            if current.equals(targetNode):
                return self.extractPath(start, current)
            neighbor: PathFindingNodeCost = None
            neighborInfo: PathFindingNodeCostInfo = None
            calculatedCost: int = 0
            for column in range(current.geographicMapCellPosition.getColumn() - 1, current.geographicMapCellPosition.getColumn() + 2):
                for row in range(current.geographicMapCellPosition.getRow() - 1, current.geographicMapCellPosition.getRow() + 2):
                    if column > 0 and row > 0 and column < allBinaryTiledLayer.getColumns() and row < allBinaryTiledLayer.getRows() and geographicMapInterface.isOnMap(basicGeographicMapCellPositionFactory.getAt(column, row)):
                        neighbor = self.costArray[column][row]
                        if self.closedSet.contains(neighbor):
                            continue
                        neighborInfo = neighbor.pathFindingNodeCostInfoP
                        calculatedCost = neighborInfo.costToEndP + neighborInfo.costFromStartP + current.pathFindingNodeCostInfoP.totalCostP
                        if calculatedCost < neighborInfo.totalCostP or not self.openPriorityQueue.contains(neighbor):
                            neighborInfo.totalCostP = calculatedCost
                            neighbor.parent = current
                            if not self.openPriorityQueue.contains(neighbor):
                                if geographicMapInterface.isOfFourDirections(current.geographicMapCellPosition, neighbor.geographicMapCellPosition):
                                    self.openPriorityQueue.add(neighbor)
            if not (not self.openPriorityQueue.isEmpty()):
                break
        raise RuntimeError()
    

    # throws Exception
    def findPathStart(self, start: GeographicMapCellPosition, target: GeographicMapCellPosition, multipassState: MultipassState) -> None:
        self.openPriorityQueue.clear()
        self.closedSet.clear()
        discoveryCalculation: int = 0
        node: PathFindingNodeCost = None
        targetColumn: int = target.getColumn()
        targetRow: int = target.getRow()
        sizeX: int = len(self.costArray)
        sizeY: int = len(self.costArray[0])
        for column in range(0, sizeX):
            for row in range(0, sizeY):
                discoveryCalculation = int(self.mathUtil.abs(column - targetColumn)) + self.mathUtil.abs(row - targetRow)
                node = self.costArray[column][row]
                node.pathFindingNodeCostInfoP.totalCostP = 0
                node.pathFindingNodeCostInfoP.costToEndP = discoveryCalculation
        startNode: PathFindingNodeCost = self.costArray[start.getColumn()][start.getRow()]
        self.openPriorityQueue.add(startNode)
        multipassState.step += 1
    

    # throws Exception
    def findPathEnd(self, start: GeographicMapCellPosition, target: GeographicMapCellPosition, multipassState: MultipassState) -> BasicArrayList:
        geographicMapInterface: BasicGeographicMap = self.geographicMapInterface
        basicGeographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        targetNode: PathFindingNodeCost = self.costArray[target.getColumn()][target.getRow()]
        current: PathFindingNodeCost = None
        total: int = 0
        while True:
            current = self.openPriorityQueue.poll()
            self.closedSet.add(current)
            if current.equals(targetNode):
                return self.extractPath(start, current)
            neighbor: PathFindingNodeCost = None
            neighborInfo: PathFindingNodeCostInfo = None
            calculatedCost: int = 0
            for column in range(current.geographicMapCellPosition.getColumn() - 1, current.geographicMapCellPosition.getColumn() + 2):
                for row in range(current.geographicMapCellPosition.getRow() - 1, current.geographicMapCellPosition.getRow() + 2):
                    if column > 0 and row > 0 and column < allBinaryTiledLayer.getColumns() and row < allBinaryTiledLayer.getRows() and geographicMapInterface.isOnMap(basicGeographicMapCellPositionFactory.getAt(column, row)):
                        neighbor = self.costArray[column][row]
                        if self.closedSet.contains(neighbor):
                            continue
                        neighborInfo = neighbor.pathFindingNodeCostInfoP
                        calculatedCost = neighborInfo.costToEndP + neighborInfo.costFromStartP + current.pathFindingNodeCostInfoP.totalCostP
                        if calculatedCost < neighborInfo.totalCostP or not self.openPriorityQueue.contains(neighbor):
                            neighborInfo.totalCostP = calculatedCost
                            neighbor.parent = current
                            if not self.openPriorityQueue.contains(neighbor):
                                if geographicMapInterface.isOfFourDirections(current.geographicMapCellPosition, neighbor.geographicMapCellPosition):
                                    self.openPriorityQueue.add(neighbor)
            total += 1
            if total > 10:
                return self.basicArrayListUtil.getImmutableInstance()
            if not (not self.openPriorityQueue.isEmpty()):
                break
        raise RuntimeError()
    

    def extractPath(self, start: GeographicMapCellPosition, current: PathFindingNodeCost) -> BasicArrayList:
        path: BasicArrayList = BasicArrayListD()
        while current.parent != NullUtil.getInstance().NULL_OBJECT:
            path.add(current.geographicMapCellPosition)
            current = current.parent
        path.add(start)
        self.basicArrayListUtil.reverse(path)
        return path
# from java.util.HashSet import HashSet
# from java.util.PriorityQueue import PriorityQueue
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCost import PathFindingNodeCost


