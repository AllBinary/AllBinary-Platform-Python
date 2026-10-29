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


class AllBinaryArrayImageRotationAnimationFactory(BaseImageAnimationFactory):

    def _init_fields(self) -> None:
        self.imageArray: list[Image] = NullImage.NULL_IMAGE_ARRAY
        self.angleIncrement: int = None
    

    # throws Exception
    @staticmethod
    def createFactory(image: Image, dx: int, dy: int) -> AllBinaryArrayImageRotationAnimationFactory:
        arrayImageRotationAnimationFactory: AllBinaryArrayImageRotationAnimationFactory = AllBinaryArrayImageRotationAnimationFactory(image, image.getWidth(), image.getHeight(), AngleFactory.getInstance().TOTAL_ANGLE / GameConfigurationCentral.getInstance().getGameControlFidelity(), AnimationBehaviorFactory.getInstance())
        arrayImageRotationAnimationFactory.initDXY(dx, dy)
        return arrayImageRotationAnimationFactory
    

    # throws Exception
    @staticmethod
    def createFactoryA(image: Image, dx: int, dy: int, angleIncrement: int) -> AllBinaryArrayImageRotationAnimationFactory:
        arrayImageRotationAnimationFactory: AllBinaryArrayImageRotationAnimationFactory = AllBinaryArrayImageRotationAnimationFactory(image, image.getWidth(), image.getHeight(), angleIncrement, AnimationBehaviorFactory.getInstance())
        arrayImageRotationAnimationFactory.initDXY(dx, dy)
        return arrayImageRotationAnimationFactory
    

    def __init__(self, image: Image, width: int, height: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        self._init_fields()
        self.angleIncrement = angleIncrement
        self.init()
    

    # throws Exception
    def init(self) -> None:
        self.setImageArray(ImageToRotationImageArrayUtil.getInstance().generate(self.getImage(), self.getAngleIncrement(), int(AngleFactory.getInstance().TOTAL_ANGLE)))
    

    def initDXY(self, dx: int, dy: int) -> None:
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
        self.animationFactoryInitializationVisitor.originalDx = dx
        self.animationFactoryInitializationVisitor.originalDy = dy
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.ImageArrayRotationAnimation import ImageArrayRotationAnimation
        from org.allbinary.animation.image.AdjustedImageArrayRotationAnimation import AdjustedImageArrayRotationAnimation
        scaledImageArray: list[Image] = [None] * (len(self.imageArray))
        size: int = len(scaledImageArray)
        image: Image = self.getImage()
        for index in range(0, size):
            scaledImageArray[index] = self.animationFactoryImageScaleUtil.createImage(image, image.getWidth(), image.getHeight(), self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            self.animationFactoryImageScaleUtil.processAdjust(self)
            return AdjustedImageArrayRotationAnimation(scaledImageArray, AngleInfo.getInstance(((int(self.getAngleIncrement()) + 32768) % 65536 - 32768)), int(AngleFactory.getInstance().TOTAL_ANGLE), self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return ImageArrayRotationAnimation(scaledImageArray, AngleInfo.getInstance(((int(self.getAngleIncrement()) + 32768) % 65536 - 32768)), int(AngleFactory.getInstance().TOTAL_ANGLE), self.animationBehaviorFactory.getOrCreateInstance())
    

    def setImageArray(self, imageArray: list[Image]) -> None:
        self.imageArray = imageArray
    

    def getAngleIncrement(self) -> int:
        return self.angleIncrement
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.image.ImageToRotationImageArrayUtil import ImageToRotationImageArrayUtil


