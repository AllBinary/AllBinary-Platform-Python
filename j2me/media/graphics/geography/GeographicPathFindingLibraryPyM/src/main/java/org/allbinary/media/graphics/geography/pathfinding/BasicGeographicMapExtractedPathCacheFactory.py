# Generated Code Do Not Modify
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.cache.BaseBasicArrayListCache import BaseBasicArrayListCache


@java_inherited_overloads
class BasicGeographicMapExtractedPathCacheFactory(BaseBasicArrayListCache):
    instance: BasicGeographicMapExtractedPathCacheFactory = None
    def _java_defaults(self):
        vars(self).setdefault("maxConcurrentPaths", 0)
        vars(self).setdefault("maxPaths", 0)

    def _init_fields(self) -> None:
        if "maxConcurrentPaths" not in vars(self): self.maxConcurrentPaths: int = 0
        if "maxPaths" not in vars(self): self.maxPaths: int = 0
    

    @staticmethod
    def getInstance() -> BasicGeographicMapExtractedPathCacheFactory:
        return BasicGeographicMapExtractedPathCacheFactory.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def init(self, maxConcurrentPaths: int, maxPaths: int) -> None:
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
        if maxConcurrentPaths != self.maxConcurrentPaths:
            for index in range(maxConcurrentPaths, self.maxConcurrentPaths - 1, -1):
                self.list_.add(BasicArrayListS(maxPaths))
            self.maxConcurrentPaths = maxConcurrentPaths
        self.maxPaths = maxPaths
    

    def getPath(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
        if self.list_.size() > 0:
            return self.list_.removeAt(0)
        else:
            return BasicArrayListS(self.maxPaths)
    

    def release(self, list_: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        list_.clear()
        self.list_.add(list_)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListS import BasicArrayListS


def _BasicGeographicMapExtractedPathCacheFactory_instance() -> object:
    return BasicGeographicMapExtractedPathCacheFactory()

lazy_static(BasicGeographicMapExtractedPathCacheFactory, "instance", _BasicGeographicMapExtractedPathCacheFactory_instance)

