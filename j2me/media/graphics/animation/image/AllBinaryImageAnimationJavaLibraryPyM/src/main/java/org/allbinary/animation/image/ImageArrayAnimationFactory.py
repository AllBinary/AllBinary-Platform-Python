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

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class ImageArrayAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.dx: int = 0
        self.dy: int = 0
        self.imageArray: list[Image] = None
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, imageArray: list[Image], dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        self.imageArray = imageArray
        self.animationBehaviorFactory = animationBehaviorFactory
        self.dx = dx
        self.dy = dy
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.ImageArrayAnimation import ImageArrayAnimation
        from org.allbinary.animation.image.AdjustedImageArrayAnimation import AdjustedImageArrayAnimation
        if self.dx != 0 or self.dy != 0:
            return AdjustedImageArrayAnimation(self.imageArray, self.dx, self.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return ImageArrayAnimation(self.imageArray, AnimationBehavior.getInstance())
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.media.ScaleProperties import ScaleProperties


