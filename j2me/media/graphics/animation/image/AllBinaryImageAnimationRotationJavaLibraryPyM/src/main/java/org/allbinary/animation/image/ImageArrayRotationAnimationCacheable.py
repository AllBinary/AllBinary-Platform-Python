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

from org.allbinary.logic.util.cache.CacheableInterface import CacheableInterface
from org.allbinary.animation.image.AdjustedImageArrayRotationAnimation import AdjustedImageArrayRotationAnimation


class ImageArrayRotationAnimationCacheable(AdjustedImageArrayRotationAnimation, CacheableInterface):
    

    def __init__(self, anyType: object, animationBehavior: AnimationBehavior) -> None:
        super().__init__((anyType).getImageArray(), (anyType).getAngleInfoP(), (anyType).getTotalAngle(), (anyType).getDx(), (anyType).getDy(), animationBehavior)
    

    def getKey(self) -> object:
        return NullUtil.getInstance().NULL_OBJECT
    

    def toString(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringUtil import StringUtil


