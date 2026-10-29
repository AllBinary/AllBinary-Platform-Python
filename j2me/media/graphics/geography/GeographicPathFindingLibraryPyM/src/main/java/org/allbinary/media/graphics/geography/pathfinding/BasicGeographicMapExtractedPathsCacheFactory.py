# Generated Code Do Not Modify
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations

from org.allbinary.logic.util.cache.BaseBasicArrayListCache import BaseBasicArrayListCache


class BasicGeographicMapExtractedPathsCacheFactory(BaseBasicArrayListCache):
    instance: BasicGeographicMapExtractedPathsCacheFactory = None

    def _init_fields(self) -> None:
        self.maxConcurrentPaths: int = 0
        self.maxPaths: int = 0
    

    @staticmethod
    def getInstance() -> BasicGeographicMapExtractedPathsCacheFactory:
        return BasicGeographicMapExtractedPathsCacheFactory.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def init(self, maxConcurrentPaths: int, maxPaths: int) -> None:
        if maxConcurrentPaths != self.maxConcurrentPaths:
            for index in range(maxConcurrentPaths, self.maxConcurrentPaths - 1, -1):
                self.list_.add(BasicArrayListS(maxPaths))
            self.maxConcurrentPaths = maxConcurrentPaths
        self.maxPaths = maxPaths
    

    def getPaths(self) -> BasicArrayList:
        if self.list_.size() > 0:
            return self.list_.removeAt(0)
        else:
            return BasicArrayListS(self.maxPaths)
    

    def release(self, list_: BasicArrayList) -> None:
        from org.allbinary.media.graphics.geography.pathfinding.BasicGeographicMapExtractedPathCacheFactory import BasicGeographicMapExtractedPathCacheFactory
        for index in range(list_.size() - 1, 0 - 1, -1):
            BasicGeographicMapExtractedPathCacheFactory.getInstance().release(list_.get(index))
        list_.clear()
        self.list_.add(list_)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListS import BasicArrayListS


BasicGeographicMapExtractedPathsCacheFactory.instance = BasicGeographicMapExtractedPathsCacheFactory()

