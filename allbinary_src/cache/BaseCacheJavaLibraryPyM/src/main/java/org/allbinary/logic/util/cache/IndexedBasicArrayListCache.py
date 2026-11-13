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

from org.allbinary.logic.util.cache.BaseBasicArrayListCache import BaseBasicArrayListCache
from org.allbinary.logic.util.cache.CacheInterface import CacheInterface


class IndexedBasicArrayListCache(BaseBasicArrayListCache, CacheInterface):

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from jsinterop.annotations.JsProperty import JsProperty
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.size: int = 0
        self.index: int = 0
    

    # throws Exception
    @staticmethod
    def createCache(size: int) -> IndexedBasicArrayListCache:
        from jsinterop.annotations.JsMethod import JsMethod
        indexedBasicArrayListCache: IndexedBasicArrayListCache = IndexedBasicArrayListCache()
        indexedBasicArrayListCache.init(size)
        return indexedBasicArrayListCache
    

    def __init__(self) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def init(self, size: int) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        if self.size < size:
            self.list_.ensureCapacity(size)
            for index in range(size - 1, self.size - 1, -1):
                self.addDefault()
            self.size = size
    

    def getAt(self, index: int) -> object:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.list_.objectArray[index]
    

    # throws Exception
    def addDefault(self) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        pass
    

    # throws Exception
    def addObject(self, anyType: object) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        self.list_.add(anyType)
    

    # throws Exception
    def add(self, cacheableInterface: CacheableInterface) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        self.list_.add(cacheableInterface)
    

    # throws Exception
    def addArray(self, cacheableInterfaces: list[CacheableInterface]) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        raise Exception("No Imple")
    

    def clear(self) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        self.index = 0
# from jsinterop.annotations.JsType import JsType
# from org.allbinary.string.CommonStrings import CommonStrings
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor
# from jsinterop.annotations.JsProperty import JsProperty


