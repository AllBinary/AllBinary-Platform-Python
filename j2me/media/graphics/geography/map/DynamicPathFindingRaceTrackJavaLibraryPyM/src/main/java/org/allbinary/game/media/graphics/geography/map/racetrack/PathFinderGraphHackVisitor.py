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

from org.allbinary.game.media.graphics.geography.map.racetrack.BasePathFinderGraphVisitor import BasePathFinderGraphVisitor


class PathFinderGraphHackVisitor(BasePathFinderGraphVisitor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, geographicMapInterface: BasicGeographicMap, edgeMinimum: int, minPathWeight: int, maxPathWeight: int) -> None:
        super().__init__(geographicMapInterface, edgeMinimum, minPathWeight, maxPathWeight)
        self._init_fields()
    

    # throws Exception
    def visit(self, graph: SimpleWeightedGraph, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList) -> None:
        self.fixStart(graph, startPathFindingNodeList)
        self.fixEnd(graph, endPathFindingNodeList)
        self.fixOverPassEdges(graph)
    

    # throws Exception
    def fixStart(self, graph: SimpleWeightedGraph[CellPosition, DefaultWeightedEdge], startPathFindingNodeList: BasicArrayList) -> None:
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = self.geographicMapInterface.getGeographicMapCellPositionFactory()
        tiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        for index in range(startPathFindingNodeList.size() - 1, 0 - 1, -1):
            startPathFindingNode: PathFindingNode = startPathFindingNodeList.get(index)
            geographicMapCellPosition: GeographicMapCellPosition = startPathFindingNode.geographicMapCellPosition
            column: int = geographicMapCellPosition.getColumn()
            row: int = geographicMapCellPosition.getRow()
            nextRow: int = row + 1
            if tiledLayer.isOnTileLayer(column, nextRow):
                geographicMapCellPositionNeighbor: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(column, nextRow)
                graph.removeEdge(geographicMapCellPosition, geographicMapCellPositionNeighbor)
    

    # throws Exception
    def fixEnd(self, graph: SimpleWeightedGraph[CellPosition, DefaultWeightedEdge], endPathFindingNodeList: BasicArrayList) -> None:
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = self.geographicMapInterface.getGeographicMapCellPositionFactory()
        tiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        for index in range(endPathFindingNodeList.size() - 1, 0 - 1, -1):
            endPathFindingNode: PathFindingNode = endPathFindingNodeList.get(index)
            geographicMapCellPosition: GeographicMapCellPosition = endPathFindingNode.geographicMapCellPosition
            graph.addVertex(geographicMapCellPosition)
            column: int = geographicMapCellPosition.getColumn()
            row: int = geographicMapCellPosition.getRow()
            nextRow: int = row + 1
            if tiledLayer.isOnTileLayer(column, nextRow):
                geographicMapCellPositionNeighbor: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(column, nextRow)
                graph.addEdge(geographicMapCellPosition, geographicMapCellPositionNeighbor)
    

    # throws Exception
    def fixOverPassEdges(self, graph: SimpleWeightedGraph[CellPosition, DefaultWeightedEdge]) -> None:
        from org.allbinary.game.media.graphics.geography.map.racetrack.CellPositionArray import CellPositionArray
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = self.geographicMapInterface.getGeographicMapCellPositionFactory()
        raceTrackGeographicMap: RaceTrackGeographicMap = self.geographicMapInterface
        CellPositionArray: list[CellPosition] = raceTrackGeographicMap.getRaceTrackData().getOverPassGeographicMapCellPositionArray()
        for index in range(len(CellPositionArray) - 1, 0 - 1, -1):
            overPassGeographicMapCellPosition: CellPosition = CellPositionArray[index]
            self.logUtil.putF("Fixing Over Pass: " + str(overPassGeographicMapCellPosition.getColumn()) + ", " + str(overPassGeographicMapCellPosition.getRow()), self, "fixOverPassEdges")
            underPassGeographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(overPassGeographicMapCellPosition.getColumn(), overPassGeographicMapCellPosition.getRow())
            rightUnderPassGeographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(overPassGeographicMapCellPosition.getColumn() + 1, overPassGeographicMapCellPosition.getRow())
            leftUnderPassGeographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(overPassGeographicMapCellPosition.getColumn() - 1, overPassGeographicMapCellPosition.getRow())
            graph.removeEdge(underPassGeographicMapCellPosition, rightUnderPassGeographicMapCellPosition)
            graph.removeEdge(underPassGeographicMapCellPosition, leftUnderPassGeographicMapCellPosition)
            graph.addVertex(overPassGeographicMapCellPosition)
            graph.addEdge(overPassGeographicMapCellPosition, rightUnderPassGeographicMapCellPosition)
            graph.addEdge(overPassGeographicMapCellPosition, leftUnderPassGeographicMapCellPosition)
    

    # throws Exception
    def fixPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, pathList: BasicArrayList) -> None:
        for index in range(startPathFindingNodeList.size() - 1, 0 - 1, -1):
            endPathFindingNode: PathFindingNode = endPathFindingNodeList.get(index)
            startPathFindingNode: PathFindingNode = startPathFindingNodeList.get(index)
            if BasicGeographicMapUtil.getInstance().isSameCellPosition(startPathFindingNode.geographicMapCellPosition, endPathFindingNode.geographicMapCellPosition):
                if pathList.remove(endPathFindingNode.geographicMapCellPosition):
                    pathList.remove(startPathFindingNode.geographicMapCellPosition)
                    pathList.addAt(0, startPathFindingNode.geographicMapCellPosition)
        self.removeOverPassEdges(pathList)
    

    # throws Exception
    def removeOverPassEdges(self, pathList: BasicArrayList) -> None:
        from org.allbinary.game.media.graphics.geography.map.racetrack.CellPositionArray import CellPositionArray
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = self.geographicMapInterface.getGeographicMapCellPositionFactory()
        raceTrackGeographicMap: RaceTrackGeographicMap = self.geographicMapInterface
        CellPositionArray: list[CellPosition] = raceTrackGeographicMap.getRaceTrackData().getOverPassGeographicMapCellPositionArray()
        for index in range(len(CellPositionArray) - 1, 0 - 1, -1):
            overPassGeographicMapCellPosition: CellPosition = CellPositionArray[index]
            underPassGeographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(overPassGeographicMapCellPosition.getColumn(), overPassGeographicMapCellPosition.getRow())
            indexOf: int = pathList.indexOf(overPassGeographicMapCellPosition)
            if indexOf != -1:
                pathList.set(indexOf, underPassGeographicMapCellPosition)
    

    def isValid(self, graphPath: GraphPath) -> bool:
        if graphPath.getEdgeList().size() > self.edgeMinimum and graphPath.getWeight() < self.maxPathWeight and graphPath.getWeight() > self.minPathWeight:
            return True
        else:
            return False
from org.jgrapht.GraphPath import GraphPath
from org.jgrapht.graph.DefaultWeightedEdge import DefaultWeightedEdge
from org.jgrapht.graph.SimpleWeightedGraph import SimpleWeightedGraph
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMapUtil import BasicGeographicMapUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMap import RaceTrackGeographicMap
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode


