# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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


class LazyImageRotationAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.layoutIndex: int = None
        self.animationInterfaceFactoryInterface: BaseImageAnimationFactory = None
        self.scaleProperties: ScaleProperties = ScaleProperties.instance
    

    def __init__(self, layoutIndex: int, associatedLazyAnimationId: int, animationInterfaceFactoryInterface: BaseImageAnimationFactory) -> None:
        self._init_fields()
        self.layoutIndex = layoutIndex
        self.animationInterfaceFactoryInterface = animationInterfaceFactoryInterface
        ImageCacheFactory.getInstance().hasAnyLazyAnimationFactories = True
        if self.animationInterfaceFactoryInterface.animationBehaviorFactory == AnimationBehaviorFactory.getInstance():
            ForcedLogUtil.log("Using default AnimationBehaviorFactory with IndexedAnimationFactory", self)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        if self.animationInterfaceFactoryInterface.getImage().isReady():
            self.animationInterfaceFactoryInterface.setInitialScale(self.scaleProperties)
            return self.animationInterfaceFactoryInterface.getInstance(instanceId)
        else:
            return LazyImageRotationAnimation(self.layoutIndex, instanceId, self.scaleProperties, self.animationInterfaceFactoryInterface, self.animationInterfaceFactoryInterface.animationBehaviorFactory.getOrCreateInstance())
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        self.scaleProperties = scaleProperties
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.media.ScaleProperties import ScaleProperties


