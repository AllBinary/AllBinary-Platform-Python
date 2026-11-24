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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.graphics.geography.pathfinding.PathGeneratorInterface import PathGeneratorInterface


class PathGenerator(PathGeneratorInterface):
    SINGLETON: PathGenerator = None
    

    @staticmethod
    def getInstance() -> PathGenerator:
        return PathGenerator.SINGLETON
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def init(self, geographicMapInterface: object, totalPaths: int) -> None:
        pass
    

    # throws Exception
    def getInstanceNoCache(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, totalPaths: int) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        geographicMapCellPositionBasicArrayList: BasicArrayList = self.create(geographicMapInterface, pathFindingInfo, totalPaths)
        return geographicMapCellPositionBasicArrayList
    

    # throws Exception
    def createList(self, geographicMapInterface: BasicGeographicMap, geographicMapCellHistory: GeographicMapCellHistory, pathFindingInfo: PathFindingInfo, totalPaths: int) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    # throws Exception
    def create(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, totalPaths: int) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        startPathFindingNodeList: BasicArrayList = pathFindingInfo.getStartPathFindingNodeList()
        endPathFindingNodeList: BasicArrayList = pathFindingInfo.getEndPathFindingNodeList()
        geographicPathFinderInterface: GeographicPathFinderBase = pathFindingInfo.getPathFinder()
        geographicMapCellPositionBasicArrayList: BasicArrayList = geographicPathFinderInterface.searchTotalPath(startPathFindingNodeList, endPathFindingNodeList, totalPaths)
        return geographicMapCellPositionBasicArrayList
    

    # throws Exception
    def createN(self, geographicMapInterface: BasicGeographicMap, pathFindingInfo: PathFindingInfo, totalPaths: int, multipassState: MultipassState) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        startPathFindingNodeList: BasicArrayList = pathFindingInfo.getStartPathFindingNodeList()
        endPathFindingNodeList: BasicArrayList = pathFindingInfo.getEndPathFindingNodeList()
        geographicPathFinderInterface: GeographicPathFinderBase = pathFindingInfo.getPathFinder()
        geographicMapCellPositionBasicArrayList: BasicArrayList = geographicPathFinderInterface.searchTotalPathN(startPathFindingNodeList, endPathFindingNodeList, totalPaths, multipassState)
        return geographicMapCellPositionBasicArrayList
    

    # throws Exception
    def isValid(self, pathList: BasicArrayList, geographicMapCellHistory: GeographicMapCellHistory) -> bool:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _PathGenerator_SINGLETON() -> object:
    return PathGenerator()

lazy_static(PathGenerator, "SINGLETON", _PathGenerator_SINGLETON)

