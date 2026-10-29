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
# package org.allbinary.graphics.color

from __future__ import annotations

import threading


class BasicColorCacheFactory:
    instance: BasicColorCacheFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    

    @staticmethod
    def getInstance() -> BasicColorCacheFactory:
        return BasicColorCacheFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def add(self, basicDefaultColor: BasicColor) -> None:
        self.hashtable.put(int(int(basicDefaultColor)), basicDefaultColor)
    

    def getAndOrCreate(self, integer: int) -> BasicColor:
        with self._lock:
            return self._getAndOrCreate_unlocked(integer)

    def _getAndOrCreate_unlocked(self, integer: int) -> BasicColor:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        basicColor: BasicColor = self.hashtable.get(integer)
        if basicColor is None:
            basicColor = BasicColorFactory.getInstance().createInstance(int(integer))
            self.hashtable.put(integer, basicColor)
        return basicColor
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


BasicColorCacheFactory.instance = BasicColorCacheFactory()

