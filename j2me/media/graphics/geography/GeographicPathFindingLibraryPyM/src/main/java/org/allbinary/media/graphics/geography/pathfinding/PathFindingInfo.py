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

from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfoInterface import PathFindingInfoInterface
from org.allbinary.media.graphics.geography.pathfinding.PathFindingNodeCostInfoFactoryBase import PathFindingNodeCostInfoFactoryBase


class PathFindingInfo(PathFindingInfoInterface):
    NULL_PATH_FINDING_INFO: PathFindingInfo = None

    def _init_fields(self) -> None:
        self.pathFinder: GeographicPathFinderBase = GeographicPathFinderBase.NULL_GEOGRAPHIC_PATH_FINDER_BASE
        self.startPathFindingNodeList: BasicArrayList = None
        self.endPathFindingNodeList: BasicArrayList = None
        self.pathFindingNodeCostInfoFactoryInterface: PathFindingNodeCostInfoFactoryBase = None
    

    def __init__(self, pathFindingNodeCostInfoFactoryInterface: PathFindingNodeCostInfoFactoryBase, startPathFindingNodeList: BasicArrayList, endPathFindingNodeList: BasicArrayList) -> None:
        self._init_fields()
        self.pathFindingNodeCostInfoFactoryInterface = pathFindingNodeCostInfoFactoryInterface
        self.startPathFindingNodeList = startPathFindingNodeList
        self.endPathFindingNodeList = endPathFindingNodeList
    

    def getStartPathFindingNodeList(self) -> BasicArrayList:
        return self.startPathFindingNodeList
    

    def getEndPathFindingNodeList(self) -> BasicArrayList:
        return self.endPathFindingNodeList
    

    def getPathFinder(self) -> GeographicPathFinderBase:
        return self.pathFinder
    

    def addStartPathFindingNode(self, startPathFindingNode: PathFindingNode) -> None:
        self.startPathFindingNodeList.add(startPathFindingNode)
    

    def addEndPathFindingNode(self, endPathFindingNode: PathFindingNode) -> None:
        self.endPathFindingNodeList.add(endPathFindingNode)
    

    def setPathFinder(self, pathFinder: GeographicPathFinderBase) -> None:
        self.pathFinder = pathFinder
    

    def getPathFindingNodeCostInfoFactoryInterface(self) -> PathFindingNodeCostInfoFactoryBase:
        return self.pathFindingNodeCostInfoFactoryInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.media.graphics.geography.pathfinding.GeographicPathFinderBase import GeographicPathFinderBase


PathFindingInfo.NULL_PATH_FINDING_INFO = PathFindingInfo(PathFindingNodeCostInfoFactoryBase.NULL_PATH_FINDING_NODE_COST_INFO_FACTORY_BASE, BasicArrayListUtil.getInstance().getImmutableInstance(), BasicArrayListUtil.getInstance().getImmutableInstance())

