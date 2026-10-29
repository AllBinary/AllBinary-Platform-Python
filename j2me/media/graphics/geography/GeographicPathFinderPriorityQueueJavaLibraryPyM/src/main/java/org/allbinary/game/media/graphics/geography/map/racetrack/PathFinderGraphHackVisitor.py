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


#1.4.2
class PathFinderGraphHackVisitor(BasePathFinderGraphVisitor):
    

    def __init__(self, geographicMapInterface: BasicGeographicMap, edgeMinimum: int, minPathWeight: int, maxPathWeight: int) -> None:
        super().__init__(geographicMapInterface, edgeMinimum, minPathWeight, maxPathWeight)
    

    # throws Exception
    def visit(self, graph: object, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList) -> None:
        self.fixStart(graph, startPathFindingNodeList)
        self.fixEnd(graph, endPathFindingNodeList)
        self.fixOverPassEdges(graph)
    

    # throws Exception
    def fixStart(self, graph: object, startPathFindingNodeList: BasicArrayList) -> None:
        pass
    

    # throws Exception
    def fixEnd(self, graph: object, endPathFindingNodeList: BasicArrayList) -> None:
        pass
    

    # throws Exception
    def fixOverPassEdges(self, graph: object) -> None:
        pass
    

    # throws Exception
    def fixPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, pathList: BasicArrayList) -> None:
        pass
    

    # throws Exception
    def removeOverPassEdges(self, pathList: BasicArrayList) -> None:
        pass
    

    def isValid(self, graphPath: object) -> bool:
        return False
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap


