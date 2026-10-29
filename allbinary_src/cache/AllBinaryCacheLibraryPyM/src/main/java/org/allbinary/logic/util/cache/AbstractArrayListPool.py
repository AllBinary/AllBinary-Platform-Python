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

from org.allbinary.logic.util.cache.PoolInterface import PoolInterface


class AbstractArrayListPool(PoolInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.buffers: BasicArrayList = BasicArrayListD()
        self.cacheableInterfaceFactoryInterface: CacheableInterfaceFactoryInterface = None
    

    def __init__(self, cacheableInterfaceFactoryInterface: CacheableInterfaceFactoryInterface) -> None:
        self._init_fields()
        self.cacheableInterfaceFactoryInterface = cacheableInterfaceFactoryInterface
    

    # throws Exception
    def clear(self) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def remove(self, key: object) -> CacheableInterface:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def add(self, cacheableInterface: CacheableInterface) -> None:
        self.buffers.add(cacheableInterface)
    

    # throws Exception
    def addArray(self, cacheableInterfaces: list[CacheableInterface]) -> None:
        for index in range(0, len(cacheableInterfaces)):
            self.buffers.add(cacheableInterfaces[index])
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


