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

from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


class ImageRotationAnimationFactory(BaseImageAnimationFactory):

    def _init_fields(self) -> None:
        self.angleIncrement: int = None
    

    def __init__(self, image: Image, width: int, height: int, dx: int, dy: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        self._init_fields()
        self.angleIncrement = angleIncrement
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.ImageBaseRotationAnimation import ImageBaseRotationAnimation
        from org.allbinary.animation.image.AdjustedImageBaseRotationAnimation import AdjustedImageBaseRotationAnimation
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            self.animationFactoryImageScaleUtil.processAdjust(self)
            return AdjustedImageBaseRotationAnimation(self.getImage(), AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return ImageBaseRotationAnimation(self.getImage(), AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationBehaviorFactory.getOrCreateInstance())
    

    def getAngleIncrementP(self) -> int:
        return self.angleIncrement
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo


