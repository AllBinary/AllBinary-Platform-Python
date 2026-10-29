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


#TWB - Adjustments should be done in the resource creation and not at the animation level
class PooledImageArrayRotationAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.allBinaryImageRotationAnimationInfo: object = NullUtil.getInstance().NULL_OBJECT
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    # throws Exception
    @staticmethod
    def createFactory(image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> PooledImageArrayRotationAnimationFactory:
        totalAngle: int = int(AngleFactory.getInstance().TOTAL_ANGLE)
        angleIncrement: int = (totalAngle / GameConfigurationCentral.getInstance().getGameControlFidelity())
        return PooledImageArrayRotationAnimationFactory(image, image.getWidth(), image.getHeight(), -(image.getWidth() >> 2), -(image.getHeight() >> 2), angleIncrement, animationBehaviorFactory)
    

    # throws Exception
    @staticmethod
    def createDXY(image: Image, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> PooledImageArrayRotationAnimationFactory:
        totalAngle: int = int(AngleFactory.getInstance().TOTAL_ANGLE)
        angleIncrement: int = (totalAngle / GameConfigurationCentral.getInstance().getGameControlFidelity())
        return PooledImageArrayRotationAnimationFactory(image, image.getWidth(), image.getHeight(), dx, dy, angleIncrement, animationBehaviorFactory)
    

    def __init__(self, image: Image, width: int, height: int, dx: int, dy: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        from org.allbinary.animation.image.ImageArrayRotationAnimationInfo import ImageArrayRotationAnimationInfo
        self._init_fields()
        self.animationBehaviorFactory = animationBehaviorFactory
        totalAngle: int = int(AngleFactory.getInstance().TOTAL_ANGLE)
        imageArray: list[Image] = ImageToRotationImageArrayUtil.getInstance().generate(image, angleIncrement, totalAngle)
        self.allBinaryImageRotationAnimationInfo = ImageArrayRotationAnimationInfo(imageArray, angleIncrement, totalAngle, dx, dy)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.AdjustedImageArrayRotationAnimation import AdjustedImageArrayRotationAnimation
        return AdjustedImageArrayRotationAnimation.createAdjustedImageArrayRotationAnimationInfo(self.allBinaryImageRotationAnimationInfo, self.animationBehaviorFactory.getOrCreateInstance())
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.media.image.ImageToRotationImageArrayUtil import ImageToRotationImageArrayUtil


