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

from org.allbinary.media.graphics.geography.pathfinding.PathGeneratorInterface import PathGeneratorInterface


class StaticPathGenerator(PathGeneratorInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
        PreLogUtil.put("Using Static Path Finding", self, CommonStrings.getInstance().CONSTRUCTOR)
    

    # throws Exception
    def init(self, geographicMapInterface: object, totalPaths: int) -> None:
        pass
    

    # throws Exception
    def getGeographicMapCellPositionListFromBasicGeographicMapCellPositionList(self, geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory, pathList: BasicArrayList) -> BasicArrayList:
        list_: BasicArrayList = BasicArrayListD()
        size: int = pathList.size()
        basicGeographicMapCellPosition: CellPosition = None
        geographicMapCellPosition: GeographicMapCellPosition = None
        for index in range(0, size):
            basicGeographicMapCellPosition = pathList.get(index)
            geographicMapCellPosition = geographicMapCellPositionFactory.getAt(basicGeographicMapCellPosition.getColumn(), basicGeographicMapCellPosition.getRow())
            list_.add(geographicMapCellPosition)
        return list_
    

    # throws Exception
    def createList(self, geographicMapInterface: BasicGeographicMap, geographicMapCellHistory: GeographicMapCellHistory, pathFindingInfo: PathFindingInfo, totalPaths: int) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.pathfinding.PathCacheFactory import PathCacheFactory
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            pathCacheFactory: PathCacheFactory = PathCacheFactory.getInstance()
            mapIdInteger: int = geographicMapInterface.getAllBinaryTiledLayer().getDataId()
            list_: BasicArrayList = pathCacheFactory.getOrCreate(mapIdInteger)
            if list_ == self.basicArrayListUtil.getImmutableInstance():
                list_ = BasicArrayListD()
                smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
                geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
                id: int = PathData.getInstance().OFFSET + int(mapIdInteger)
                basicList: BasicArrayList = pathCacheFactory.getOrCreate(smallIntegerSingletonFactory.getAt(id))
                size: int = basicList.size()
                pathList: BasicArrayList = None
                for index in range(0, size):
                    pathList = self.getGeographicMapCellPositionListFromBasicGeographicMapCellPositionList(geographicMapCellPositionFactory, basicList.get(index))
                    list_.add(pathList)
                pathCacheFactory.add(mapIdInteger, list_)
                pathCacheFactory.remove(smallIntegerSingletonFactory.getAt(id))
            self.logUtil.putF(str(StringMaker().append("Using Cached Path(s): ").append(StringUtil.getInstance().toString(list_))), self, commonStrings.GET_INSTANCE)
            return list_
        except Exception as e:
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return BasicArrayListD()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.PathData import PathData
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


