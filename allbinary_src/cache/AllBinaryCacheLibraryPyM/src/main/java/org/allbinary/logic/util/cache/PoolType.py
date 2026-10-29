# 
# AllBinary Open License Version 1 
# Copyright (c) 2007 AllBinary 
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



class PoolType:

    def _init_fields(self) -> None:
        self.cacheType: CacheType = None
    

    def __init__(self, cacheType: CacheType) -> None:
        self._init_fields()
        self.cacheType = cacheType
    

    def getCacheType(self) -> CacheType:
        return self.cacheType
    

    def toString(self) -> str:
        POOL_TYPE: str = "PoolType: "
        return POOL_TYPE + str(self.getCacheType())

    def __str__(self) -> str:
        return self.toString()


