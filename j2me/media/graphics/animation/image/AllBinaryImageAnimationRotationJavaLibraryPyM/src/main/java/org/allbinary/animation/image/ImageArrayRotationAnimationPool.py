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
# package org.allbinary.animation.image

from __future__ import annotations

from org.allbinary.logic.util.cache.BasicArrayListResetablePool import BasicArrayListResetablePool
from org.allbinary.animation.image.ImageArrayRotationAnimationCacheableInterfaceFactory import ImageArrayRotationAnimationCacheableInterfaceFactory


class ImageArrayRotationAnimationPool(BasicArrayListResetablePool):
    IMAGE_ROTATION_ANIMATION_POOL: PoolInterface = None
    

    def __init__(self, cacheableInterfaceFactoryInterface: CacheableInterfaceFactoryInterface) -> None:
        super().__init__(cacheableInterfaceFactoryInterface)
    

    @staticmethod
    def getInstance() -> PoolInterface:
        return ImageArrayRotationAnimationPool.IMAGE_ROTATION_ANIMATION_POOL
    

    # throws Exception
    def remove(self, key: object) -> CacheableInterface:
        cacheableInterface: CacheableInterface = super().remove(key)
        allBinaryImageRotationAnimationInfo: ImageArrayRotationAnimationInfo = key
        imageArrayRotationAnimationCacheable: ImageArrayRotationAnimationCacheable = (cacheableInterface)
        imageArrayRotationAnimationCacheable.setImageArray(allBinaryImageRotationAnimationInfo.getImageArray())
        return cacheableInterface
from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface
from org.allbinary.logic.util.cache.CacheableInterfaceFactoryInterface import CacheableInterfaceFactoryInterface
from org.allbinary.logic.util.cache.PoolInterface import PoolInterface


ImageArrayRotationAnimationPool.IMAGE_ROTATION_ANIMATION_POOL = ImageArrayRotationAnimationPool(ImageArrayRotationAnimationCacheableInterfaceFactory())

