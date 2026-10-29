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

from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


class ImageAnimationFactory(BaseImageAnimationFactory):
    

    # throws Exception
    @staticmethod
    def createFactory(image: Image) -> ImageAnimationFactory:
        return ImageAnimationFactory(image, image.getWidth(), image.getHeight(), 0, 0, AnimationBehaviorFactory.getInstance())
    

    def __init__(self, image: Image, width: int, height: int, dx: int, dy: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, dx, dy, animationBehaviorFactory)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.ImageAnimation import ImageAnimation
        from org.allbinary.animation.image.AdjustedImageAnimation import AdjustedImageAnimation
        scaledImage: Image = self.animationFactoryImageScaleUtil.createImage(self.getImage(), self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        openGLUtil: OpenGLUtil = OpenGLUtil.getInstance()
        scaledImage = openGLUtil.addImage(scaledImage)
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            self.animationFactoryImageScaleUtil.processAdjust(self)
            return AdjustedImageAnimation(scaledImage, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return ImageAnimation(scaledImage, self.animationBehaviorFactory.getOrCreateInstance())
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.graphics.opengles.OpenGLUtil import OpenGLUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


