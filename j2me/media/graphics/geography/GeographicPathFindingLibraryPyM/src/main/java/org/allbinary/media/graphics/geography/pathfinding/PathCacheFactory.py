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



class PathCacheFactory:
    pathFactory: PathCacheFactory = None

    def _init_fields(self) -> None:
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PathCacheFactory:
        return PathCacheFactory.pathFactory
    

    def getSize(self) -> int:
        return self.hashtable.size()
    

    def add(self, pathId: int, list_: BasicArrayList) -> None:
        self.hashtable.put(pathId, list_)
    

    def remove(self, pathId: int) -> None:
        self.hashtable.remove(pathId)
    

    # throws Exception
    def removeAll(self) -> None:
        self.hashtable.clear()
        if self.hashtable.size() > 0:
            raise Exception("Did not clear")
    

    # throws Exception
    def getOrCreate(self, pathIdInteger: int) -> BasicArrayList:
        listCanBeNull: object = self.hashtable.get(pathIdInteger)
        if listCanBeNull is None:
            listCanBeNull = self.basicArrayListUtil.getImmutableInstance()
        return listCanBeNull
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


PathCacheFactory.pathFactory = PathCacheFactory()

