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

from org.allbinary.media.graphics.geography.pathfinding.PathFindingNode import PathFindingNode


class PathFindingNodeCost(PathFindingNode, object):
    NULL_PATH_FINDING_NODE_COST_ARRAY_ARRAY: list[list[PathFindingNodeCost]] = None

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.pathFindingNodeCostInfoP: PathFindingNodeCostInfo = None
    

    def __init__(self, parent: object, geographicMapCellPosition: GeographicMapCellPosition, pathFindingNodeCostInfo: PathFindingNodeCostInfo) -> None:
        super().__init__(parent, geographicMapCellPosition)
        self._init_fields()
        self.pathFindingNodeCostInfoP = pathFindingNodeCostInfo
        if self.geographicMapCellPosition is None:
            raise Exception("No GeographicMapCellPosition")
        if self.getPathFindingNodeCostInfo() is None:
            raise Exception("No PathFindingNodeCostInfo")
    

    def getPathFindingNodeCostInfo(self) -> PathFindingNodeCostInfo:
        return self.pathFindingNodeCostInfoP
    

    def setPathFindingNodeCostInfo(self, pathFindingNodeCostInfo: PathFindingNodeCostInfo) -> None:
        self.pathFindingNodeCostInfoP = pathFindingNodeCostInfo
    

    def compareTo(self, pathFindingNodeCost: PathFindingNodeCost) -> int:
        return self.pathFindingNodeCostInfoP.compareTo(pathFindingNodeCost.pathFindingNodeCostInfoP)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(CommonLabels.getInstance().COLON_SEP)
        stringBuffer.append(str(self.getPathFindingNodeCostInfo()))
        stringBuffer.append(" Path: ")
        stringBuffer.append(str(self.geographicMapCellPosition))
        pathFindingNode: PathFindingNode = self.parent
        while pathFindingNode is not None:
            stringBuffer.append(str(pathFindingNode.geographicMapCellPosition))
            stringBuffer.append(self.commonSeps.SPACE)
            pathFindingNode = pathFindingNode.parent
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.string.CommonLabels import CommonLabels


PathFindingNodeCost.NULL_PATH_FINDING_NODE_COST_ARRAY_ARRAY = [[None] * (0) for _ in range(0)]

