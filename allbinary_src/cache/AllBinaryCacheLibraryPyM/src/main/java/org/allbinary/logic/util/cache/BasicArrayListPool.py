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
# package org.allbinary.logic.util.cache

from __future__ import annotations

from org.allbinary.logic.util.cache.AbstractArrayListPool import AbstractArrayListPool


class BasicArrayListPool(AbstractArrayListPool):
    

    def __init__(self, cacheableInterfaceFactoryInterface: CacheableInterfaceFactoryInterface) -> None:
        super().__init__(cacheableInterfaceFactoryInterface)
    

    def clear(self) -> None:
        self.buffers.clear()
    

    # throws Exception
    def remove(self, key: object) -> CacheableInterface:
        size: int = self.buffers.size()
        if size > 0:
            return self.buffers.removeAt(size - 1)
        else:
            return self.cacheableInterfaceFactoryInterface.getInstance(key)
    

    # throws Exception
    def addAll(self, usedList: BasicArrayList) -> None:
        index = usedList.size()
        while (index := index - 1) >= 0:
            anyType: CacheableInterface = usedList.objectArray[index]
            self.add(anyType)
        usedList.clear()
    

    # throws Exception
    def releaseUsedBackToPool(self, usedList: BasicArrayList) -> None:
        index = usedList.size()
        while (index := index - 1) >= 0:
            list_: BasicArrayListCacheable = usedList.objectArray[index]
            if list_.size() == 0:
                usedList.removeAt(index)
                self.add(list_)
from org.allbinary.util.BasicArrayList import BasicArrayList


