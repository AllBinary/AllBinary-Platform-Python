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


class VectorToImageArrayRotationAnimationFactory(BaseImageAnimationFactory):

    def _init_fields(self) -> None:
        self.imageArray: list[Image] = NullImage.NULL_IMAGE_ARRAY
        self.angleIncrement: int = 0
    

    def __init__(self, vectorInfo: VectorInfo, basicColor: BasicColor, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(AnimationFrameToImageUtil.getInstance().getInstanceTranslate(vectorInfo.getWidth(), vectorInfo.getHeight(), VectorAnimation.createVectorAnimation(vectorInfo.getPoints(), basicColor, animationBehaviorFactory.getOrCreateInstance())), PrimitiveIntUtil.getArrayInstance(), 0, 0, 0, 0, animationBehaviorFactory)
        self._init_fields()
        self.init()
    

    # throws Exception
    def init(self) -> None:
        angleFactory: AngleFactory = AngleFactory.getInstance()
        self.angleIncrement = angleFactory.TOTAL_ANGLE / GameConfigurationCentral.getInstance().getGameControlFidelity()
        self.imageArray = ImageToRotationImageArrayUtil.getInstance().generate(self.getImage(), self.getAngleIncrement(), int(angleFactory.TOTAL_ANGLE))
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.AdjustedImageArrayRotationAnimation import AdjustedImageArrayRotationAnimation
        from org.allbinary.animation.image.AdjustedImageArrayRotationAnimation import AdjustedImageArrayRotationAnimation
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            return AdjustedImageArrayRotationAnimation(self.imageArray, AngleInfo.getInstance(((int(self.getAngleIncrement()) + 32768) % 65536 - 32768)), int(AngleFactory.getInstance().TOTAL_ANGLE), self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return AdjustedImageArrayRotationAnimation.createAnimation(self.imageArray, AngleInfo.getInstance(((int(self.angleIncrement) + 32768) % 65536 - 32768)), int(AngleFactory.getInstance().TOTAL_ANGLE), self.animationBehaviorFactory.getOrCreateInstance())
    

    def getAngleIncrement(self) -> int:
        return self.angleIncrement
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.VectorAnimation import VectorAnimation
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.image.AnimationFrameToImageUtil import AnimationFrameToImageUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.media.image.ImageToRotationImageArrayUtil import ImageToRotationImageArrayUtil
from org.allbinary.vector.VectorInfo import VectorInfo


