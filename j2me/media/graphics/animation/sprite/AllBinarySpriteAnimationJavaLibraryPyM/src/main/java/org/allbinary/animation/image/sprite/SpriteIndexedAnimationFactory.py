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


class SpriteIndexedAnimationFactory(BaseImageAnimationFactory, ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationFactorySpriteScaleUtil: AnimationFactorySpriteScaleUtil = AnimationFactorySpriteScaleUtil.getInstance()
        self.basicColorArray: list[BasicColor] = BasicColorUtil.getInstance().ZERO_ARRAY
    

    # throws Exception
    @staticmethod
    def createCWHDXY(image: Image, basicColorArray: list[BasicColor], width: int, height: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> SpriteIndexedAnimationFactory:
        return SpriteIndexedAnimationFactory(image, basicColorArray, PrimitiveIntUtil.getArrayInstance(), width, height, dx, dy, animationBehaviorFactory)
    

    # throws Exception
    @staticmethod
    def createCWH(image: Image, basicColorArray: list[BasicColor], width: int, height: int, animationBehaviorFactory: AnimationBehaviorFactory) -> SpriteIndexedAnimationFactory:
        spriteIndexedAnimationFactory: SpriteIndexedAnimationFactory = SpriteIndexedAnimationFactory(image, basicColorArray, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        spriteIndexedAnimationFactory.initHWH()
        return spriteIndexedAnimationFactory
    

    # throws Exception
    @staticmethod
    def createWH(image: Image, width: int, height: int, animationBehaviorFactory: AnimationBehaviorFactory) -> SpriteIndexedAnimationFactory:
        return SpriteIndexedAnimationFactory(image, BasicColorUtil.getInstance().ZERO_ARRAY, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
    

    def __init__(self, image: Image, basicColorArray: list[BasicColor], sequenceArray: list[int], width: int, height: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, sequenceArray, width, height, dx, dy, animationBehaviorFactory)
        self._init_fields()
        self.basicColorArray = basicColorArray
    

    def initHWH(self) -> None:
        self.animationFactoryInitializationVisitor.dx = -(self.animationFactoryInitializationVisitor.width >> 2)
        self.animationFactoryInitializationVisitor.dy = -(self.animationFactoryInitializationVisitor.height >> 2)
        if AndroidUtil.isAndroid():
            self.animationFactoryInitializationVisitor.dx += 3
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.sprite.SpriteIndexedAnimation import SpriteIndexedAnimation
        from org.allbinary.animation.image.sprite.AdjustedSpriteIndexedAnimation import AdjustedSpriteIndexedAnimation
        sprite: Sprite = self.animationFactorySpriteScaleUtil.createImage(self.getImage(), self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            return AdjustedSpriteIndexedAnimation(sprite, self.getImage(), self.basicColorArray, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return SpriteIndexedAnimation(sprite, self.getImage(), self.basicColorArray, self.animationBehaviorFactory.getOrCreateInstance())
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.getInstance(0)
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil
from org.allbinary.image.sprite.AnimationFactorySpriteScaleUtil import AnimationFactorySpriteScaleUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


