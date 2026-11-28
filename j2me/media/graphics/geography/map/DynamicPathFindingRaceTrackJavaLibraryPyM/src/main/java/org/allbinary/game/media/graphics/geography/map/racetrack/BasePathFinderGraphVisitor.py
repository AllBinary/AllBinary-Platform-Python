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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.media.graphics.geography.pathfinding.PathFinderGraphVisitorBase import PathFinderGraphVisitorBase


@java_inherited_overloads
class BasePathFinderGraphVisitor(PathFinderGraphVisitorBase):
    def _java_defaults(self):
        vars(self).setdefault("geographicMapInterface", None)
        vars(self).setdefault("edgeMinimum", 0)
        vars(self).setdefault("minPathWeight", 0)
        vars(self).setdefault("maxPathWeight", 0)

    def _init_fields(self) -> None:
        if "geographicMapInterface" not in vars(self): self.geographicMapInterface: BasicGeographicMap = None
        if "edgeMinimum" not in vars(self): self.edgeMinimum: int = 0
        if "minPathWeight" not in vars(self): self.minPathWeight: int = 0
        if "maxPathWeight" not in vars(self): self.maxPathWeight: int = 0
    

    def __init__(self, geographicMapInterface: BasicGeographicMap, edgeMinimum: int, minPathWeight: int, maxPathWeight: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        super().__init__()
        __class__._init_fields(self)
        self.geographicMapInterface = geographicMapInterface
        self.edgeMinimum = edgeMinimum
        self.minPathWeight = minPathWeight
        self.maxPathWeight = maxPathWeight
    

    # throws Exception
    def visit(self, graph: SimpleWeightedGraph, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList) -> None:
        from org.jgrapht.graph.SimpleWeightedGraph import SimpleWeightedGraph
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
    

    # throws Exception
    def fixPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, pathList: BasicArrayList) -> None:
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
        from org.allbinary.util.BasicArrayList import BasicArrayList
        for index in range(startPathFindingNodeList.size() - 1, 0 - 1, -1):
            startPathFindingNode: PathFindingNode = startPathFindingNodeList.get(index)
            pathList.remove(startPathFindingNode.geographicMapCellPosition)
            pathList.addAt(0, startPathFindingNode.geographicMapCellPosition)
    

    def isValid(self, graphPath: GraphPath) -> bool:
        from org.jgrapht.GraphPath import GraphPath
        if graphPath.getEdgeList().size() > self.edgeMinimum and graphPath.getWeight() < self.maxPathWeight and graphPath.getWeight() > self.minPathWeight:
            return True
        else:
            return False
    

    def getInvalidReason(self, graphPath: GraphPath) -> str:
        from org.jgrapht.GraphPath import GraphPath
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        if graphPath.getEdgeList().size() < self.edgeMinimum:
            stringBuffer.append("Ignoring Small: " + str(graphPath.getEdgeList().size()))
        if graphPath.getWeight() <= self.minPathWeight:
            stringBuffer.append(" Low Weighted Path: " + str(graphPath.getWeight()))
        if graphPath.getWeight() >= self.maxPathWeight:
            stringBuffer.append(" To High Weighted Path: " + str(graphPath.getWeight()))
        return str(stringBuffer)
# from org.jgrapht.GraphPath import GraphPath
# from org.jgrapht.graph.SimpleWeightedGraph import SimpleWeightedGraph
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
# from org.allbinary.util.BasicArrayList import BasicArrayList


