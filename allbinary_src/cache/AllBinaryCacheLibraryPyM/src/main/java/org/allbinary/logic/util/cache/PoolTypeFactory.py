# Generated Code Do Not Modify
# package org.allbinary.logic.util.cache

from __future__ import annotations



class PoolTypeFactory:
    instance: PoolTypeFactory = None

    def _init_fields(self) -> None:
        self.VECTOR_POOL: PoolType = PoolType(CacheTypeFactory.getInstance().NO_CACHE)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PoolTypeFactory:
        return PoolTypeFactory.instance
from org.allbinary.logic.util.cache.PoolType import PoolType
from org.allbinary.logic.util.cache.CacheTypeFactory import CacheTypeFactory


PoolTypeFactory.instance = PoolTypeFactory()

