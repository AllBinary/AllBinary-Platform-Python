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


class ColorCompositeSpriteIndexedAnimationFactory(BaseImageAnimationFactory, ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationFactorySpriteScaleUtil: AnimationFactorySpriteScaleUtil = AnimationFactorySpriteScaleUtil.getInstance()
        self.basicColorArray: list[BasicColor] = None
    

    def __init__(self, image: Image, basicColorArray: list[BasicColor], width: int, height: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        self._init_fields()
        self.basicColorArray = basicColorArray
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.sprite.SpriteIndexedAnimation import SpriteIndexedAnimation
        sprite: Sprite = self.animationFactorySpriteScaleUtil.createImage(self.getImage(), self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        return SpriteIndexedAnimation(sprite, self.getImage(), self.basicColorArray, self.animationBehaviorFactory.getOrCreateInstance())
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.getInstance(0)
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.image.sprite.AnimationFactorySpriteScaleUtil import AnimationFactorySpriteScaleUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


