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
# package org.allbinary.animation.image.sprite

from __future__ import annotations

from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


class AllBinarySpriteRotationAnimationFactory(BaseImageAnimationFactory, ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationFactorySpriteScaleUtil: AnimationFactorySpriteScaleUtil = AnimationFactorySpriteScaleUtil.getInstance()
    

    # throws Exception
    @staticmethod
    def createWHDY(image: Image, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinarySpriteRotationAnimationFactory:
        spriteRotationAnimationFactory: AllBinarySpriteRotationAnimationFactory = AllBinarySpriteRotationAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), (image.getHeight() >> 2), (image.getHeight() >> 2), 0, 0, animationBehaviorFactory)
        spriteRotationAnimationFactory.initWH(dx, dy)
        return spriteRotationAnimationFactory
    

    # throws Exception
    @staticmethod
    def createWH(image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinarySpriteRotationAnimationFactory:
        return AllBinarySpriteRotationAnimationFactory.createWHDY(image, 0, 0, animationBehaviorFactory)
    

    # throws Exception
    @staticmethod
    def createDXY(image: Image, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinarySpriteRotationAnimationFactory:
        spriteRotationAnimationFactory: AllBinarySpriteRotationAnimationFactory = AllBinarySpriteRotationAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), image.getHeight(), image.getHeight(), 0, 0, animationBehaviorFactory)
        spriteRotationAnimationFactory.init(dx, dy)
        return spriteRotationAnimationFactory
    

    # throws Exception
    @staticmethod
    def createDXYQ(image: Image, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinarySpriteRotationAnimationFactory:
        spriteRotationAnimationFactory: AllBinarySpriteRotationAnimationFactory = AllBinarySpriteRotationAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), (image.getHeight() >> 2), (image.getHeight() >> 2), 0, 0, animationBehaviorFactory)
        spriteRotationAnimationFactory.init(dx, dy)
        return spriteRotationAnimationFactory
    

    # throws Exception
    @staticmethod
    def createQ(image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinarySpriteRotationAnimationFactory:
        return AllBinarySpriteRotationAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), (image.getHeight() >> 2), (image.getHeight() >> 2), 0, 0, animationBehaviorFactory)
    

    # throws Exception
    @staticmethod
    def createWHF(image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> AllBinarySpriteRotationAnimationFactory:
        return AllBinarySpriteRotationAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), image.getHeight(), image.getHeight(), 0, 0, animationBehaviorFactory)
    

    def __init__(self, image: Image, sequenceArray: list[int], width: int, height: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, sequenceArray, width, height, dx, dy, animationBehaviorFactory)
        self._init_fields()
        if animationBehaviorFactory == AnimationBehaviorFactory.getInstance():
            ForcedLogUtil.log("Using default AnimationBehaviorFactory with IndexedAnimationFactory", self)
    

    def init(self, dx: int, dy: int) -> None:
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
    

    def initWH(self, dx: int, dy: int) -> None:
        self.init(dx, dy)
        self.animationFactoryInitializationVisitor.dx += -self.animationFactoryInitializationVisitor.width / 5
        self.animationFactoryInitializationVisitor.dy += -self.animationFactoryInitializationVisitor.height / 5
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.sprite.AllBinarySpriteRotationAnimation import AllBinarySpriteRotationAnimation
        from org.allbinary.animation.image.sprite.AllBinaryAdjustedSpriteRotationAnimation import AllBinaryAdjustedSpriteRotationAnimation
        sprite: Sprite = self.animationFactorySpriteScaleUtil.createImage(self.getImage(), self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            return AllBinaryAdjustedSpriteRotationAnimation(sprite, self.getImage(), self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return AllBinarySpriteRotationAnimation(sprite, self.getImage(), self.animationBehaviorFactory.getOrCreateInstance())
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.getInstance(0)
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.image.sprite.AnimationFactorySpriteScaleUtil import AnimationFactorySpriteScaleUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


