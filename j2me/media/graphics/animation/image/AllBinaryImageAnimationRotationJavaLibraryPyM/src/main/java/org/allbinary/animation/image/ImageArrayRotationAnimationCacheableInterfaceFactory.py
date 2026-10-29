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

from org.allbinary.logic.util.cache.CacheableInterfaceFactoryInterface import CacheableInterfaceFactoryInterface


class ImageArrayRotationAnimationCacheableInterfaceFactory(CacheableInterfaceFactoryInterface):
    

    # throws Exception
    def getInstance(self, key: object) -> CacheableInterface:
        from org.allbinary.animation.image.ImageArrayRotationAnimationCacheable import ImageArrayRotationAnimationCacheable
        return ImageArrayRotationAnimationCacheable(key, AnimationBehavior.getInstance())
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface


