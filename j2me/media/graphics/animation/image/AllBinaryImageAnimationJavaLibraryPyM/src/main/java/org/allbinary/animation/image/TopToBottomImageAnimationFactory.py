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


class TopToBottomImageAnimationFactory(BaseImageAnimationFactory):
    

    def __init__(self, image: Image, sequenceArray: list[int], animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(image, sequenceArray, image.getWidth(), image.getHeight(), 0, 0, animationBehaviorFactory)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.TopToBottomImageAnimation import TopToBottomImageAnimation
        scaledImage: Image = self.animationFactoryImageScaleUtil.createImage(self.getImage(), self.animationFactoryInitializationVisitor.width, self.animationFactoryInitializationVisitor.height, self.scaleProperties.scaleWidth, self.scaleProperties.scaleHeight)
        return TopToBottomImageAnimation(scaledImage, self.getSequenceArray(), self.animationBehaviorFactory.getOrCreateInstance())
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory


