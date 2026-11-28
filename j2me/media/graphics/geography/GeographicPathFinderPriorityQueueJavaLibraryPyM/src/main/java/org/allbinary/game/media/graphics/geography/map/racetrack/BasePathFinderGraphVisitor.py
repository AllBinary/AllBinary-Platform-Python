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


#1.4.2
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
    def visit(self, graph: object, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
    

    # throws Exception
    def fixPath(self, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList, pathList: BasicArrayList) -> None:
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
        from org.allbinary.util.BasicArrayList import BasicArrayList
        startPathFindingNode: PathFindingNode = None
        for index in range(startPathFindingNodeList.size() - 1, 0 - 1, -1):
            startPathFindingNode = startPathFindingNodeList.get(index)
            pathList.remove(startPathFindingNode.geographicMapCellPosition)
            pathList.addAt(0, startPathFindingNode.geographicMapCellPosition)
    

    def isValid(self, graphPath: object) -> bool:
        return False
    

    def getInvalidReason(self, graphPath: object) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode
# from org.allbinary.util.BasicArrayList import BasicArrayList


