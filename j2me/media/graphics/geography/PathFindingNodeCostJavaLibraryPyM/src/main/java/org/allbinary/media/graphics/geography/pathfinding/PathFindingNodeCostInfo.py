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
        if "costFromStartP" not in vars(self): self.costFromStartP: int = 0
        if "costToEndP" not in vars(self): self.costToEndP: int = 0
        if "totalCostP" not in vars(self): self.totalCostP: int = 0
    

    def __init__(self, costFromStart: int, costToGoal: int) -> None:
        __class__._init_fields(self)
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
        if self.totalCostP < pathFindingNodeCostInfo.totalCostP:
            return -1
        elif self.totalCostP > pathFindingNodeCostInfo.totalCostP:
            return 1
        return 0
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonLabels import CommonLabels
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self)))
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
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoData import PathFindingNodeCostInfoData


