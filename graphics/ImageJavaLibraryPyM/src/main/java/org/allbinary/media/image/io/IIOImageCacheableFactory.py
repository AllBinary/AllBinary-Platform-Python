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
# package org.allbinary.media.image.io

from __future__ import annotations

from org.allbinary.logic.util.cache.CacheableInterfaceFactoryInterface import CacheableInterfaceFactoryInterface


class IIOImageCacheableFactory(CacheableInterfaceFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    def getInstance(self, key: object) -> CacheableInterface:
        from org.allbinary.media.image.io.IIOImageCacheable import IIOImageCacheable
        return IIOImageCacheable(key)
from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


