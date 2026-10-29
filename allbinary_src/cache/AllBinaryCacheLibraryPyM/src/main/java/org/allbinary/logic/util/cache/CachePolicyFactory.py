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



class CachePolicyFactory:
    instance: CachePolicyFactory = None

    def _init_fields(self) -> None:
        self.NAME: str = "lru"
        self.MAX_TIME_THOUSAND_MAX: CachePolicy = CachePolicy(self.NAME, 9223372036854775807, 1000)
        self.THIRTY_MINUTES_TEN_THOUSAND_MAX: CachePolicy = CachePolicy(self.NAME, 1000 * 60 * 30, 10000)
        self.THIRTY_MINUTES_FIFTY_THOUSAND_MAX: CachePolicy = CachePolicy(self.NAME, 1000 * 60 * 30, 100000)
        self.ONE_MINUTE_FIVE_MAX: CachePolicy = CachePolicy(self.NAME, 1000 * 60 * 1, 5)
        self.ONE_MINUTE_TEN_MAX: CachePolicy = CachePolicy(self.NAME, 1000 * 60 * 1, 10)
        self.ONE_MINUTE_ONE_HUNDRED_MAX: CachePolicy = CachePolicy(self.NAME, 1000 * 60 * 1, 100)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CachePolicyFactory:
        return CachePolicyFactory.instance
from org.allbinary.logic.util.cache.CachePolicy import CachePolicy


CachePolicyFactory.instance = CachePolicyFactory()

