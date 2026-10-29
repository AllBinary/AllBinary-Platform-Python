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

from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


class OneRowSpriteIndexedAnimationFactory(BaseImageAnimationFactory):

    def _init_fields(self) -> None:
        self.animationFactorySpriteScaleUtil: AnimationFactorySpriteScaleUtil = AnimationFactorySpriteScaleUtil.getInstance()
    

    # throws Exception
    @staticmethod
    def createFactoryDX(image: Image, dx: int, animationBehaviorFactory: AnimationBehaviorFactory) -> OneRowSpriteIndexedAnimationFactory:
        oneRowSpriteIndexedAnimationFactory: OneRowSpriteIndexedAnimationFactory = OneRowSpriteIndexedAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), image.getHeight(), image.getHeight(), 0, 0, animationBehaviorFactory)
        oneRowSpriteIndexedAnimationFactory.initW(dx)
        return oneRowSpriteIndexedAnimationFactory
    

    # throws Exception
    @staticmethod
    def createFactoryDXY(image: Image, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> OneRowSpriteIndexedAnimationFactory:
        oneRowSpriteIndexedAnimationFactory: OneRowSpriteIndexedAnimationFactory = OneRowSpriteIndexedAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), image.getHeight(), image.getHeight(), 0, 0, animationBehaviorFactory)
        oneRowSpriteIndexedAnimationFactory.init(dx, dy)
        return oneRowSpriteIndexedAnimationFactory
    

    # throws Exception
    @staticmethod
    def createFactoryWH(image: Image, width: int, height: int, animationBehaviorFactory: AnimationBehaviorFactory) -> OneRowSpriteIndexedAnimationFactory:
        return OneRowSpriteIndexedAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
    

    # throws Exception
    @staticmethod
    def createFactory(image: Image, animationBehaviorFactory: AnimationBehaviorFactory) -> OneRowSpriteIndexedAnimationFactory:
        return OneRowSpriteIndexedAnimationFactory(image, PrimitiveIntUtil.getArrayInstance(), image.getHeight(), image.getHeight(), 0, 0, animationBehaviorFactory)
    

    def __init__(self, image: Image, sequenceArray: list[int], width: int, height: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, sequenceArray, width, height, dx, dy, animationBehaviorFactory)
        self._init_fields()
    

    def init(self, dx: int, dy: int) -> None:
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
    

    def initW(self, dx: int) -> None:
        self.init(dx, 0)
        self.animationFactoryInitializationVisitor.dx += -(self.animationFactoryInitializationVisitor.width >> 2)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.sprite.SpriteIndexedAnimation import SpriteIndexedAnimation
        from org.allbinary.animation.image.sprite.AdjustedSpriteIndexedAnimation import AdjustedSpriteIndexedAnimation
        sprite: Sprite = self.animationFactorySpriteScaleUtil.createImage(self.getImage(), self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            return AdjustedSpriteIndexedAnimation(sprite, self.getImage(), BasicColorUtil.getInstance().ZERO_ARRAY, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return SpriteIndexedAnimation(sprite, self.getImage(), BasicColorUtil.getInstance().ZERO_ARRAY, self.animationBehaviorFactory.getOrCreateInstance())
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil
from org.allbinary.image.sprite.AnimationFactorySpriteScaleUtil import AnimationFactorySpriteScaleUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


