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



class PathFindingNodeCostInfo(object):

    def _init_fields(self) -> None:
        self.pathFindingNodeCostInfoData: PathFindingNodeCostInfoData = PathFindingNodeCostInfoData.getInstance()
        self.costFromStartP: int = None
        self.costToEndP: int = None
        self.totalCostP: int = 0
    

    def __init__(self, costFromStart: int, costToGoal: int) -> None:
        self._init_fields()
        self.costFromStartP = costFromStart
        self.costToEndP = costToGoal
        self.setCalculatedTotalCost()
    

    def setCostToEnd(self, costToEnd: int) -> None:
        self.costToEndP = costToEnd
    

    def setTotalCost(self, totalCost: int) -> None:
        self.totalCostP = totalCost
    

    # throws Exception
    def setCalculatedTotalCost(self) -> None:
        self.totalCostP = self.costFromStartP + self.costToEndP
        if self.totalCostP > self.pathFindingNodeCostInfoData.MAX_NODE_COST:
            raise Exception("Max Cost Exceeded")
    

    def setCostFromStart(self, cost: int) -> None:
        self.costFromStartP = cost
    

    def addCostFromStart(self, cost: int) -> None:
        self.costFromStartP += cost
    

    def compareTo(self, pathFindingNodeCostInfo: PathFindingNodeCostInfo) -> int:
        return java.lang.Long.compare(self.totalCostP, pathFindingNodeCostInfo.totalCostP)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(type(self).__module__ + "." + type(self).__qualname__)
        stringBuffer.append(CommonLabels.getInstance().COLON_SEP)
        stringBuffer.append("CostFromStart: ")
        stringBuffer.appendlong(self.costFromStartP)
        stringBuffer.append(" CostToEnd: ")
        stringBuffer.appendlong(self.costToEndP)
        stringBuffer.append(" TotalCost: ")
        stringBuffer.appendlong(self.totalCostP)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoData import PathFindingNodeCostInfoData


