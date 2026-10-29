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
# package org.allbinary.image

from __future__ import annotations



class AnimationFactoryImageScaleUtil:
    instance: AnimationFactoryImageScaleUtil = None

    def _init_fields(self) -> None:
        self.imageScaleUtil: ImageJ2MEScaleUtil = ImageJ2MEScaleUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AnimationFactoryImageScaleUtil:
        return AnimationFactoryImageScaleUtil.instance
    

    # throws Exception
    def createImage(self, image: Image, width: int, height: int, scaleWidth: int, scaleHeight: int) -> Image:
        scaledImage: Image = None
        if scaleWidth != 0 and scaleHeight != 0:
            scaleX: float = (float(scaleWidth)) / (float(width))
            scaleY: float = (float(scaleHeight)) / (float(height))
            if (scaleX == 1.0 and scaleY == 1.0) or (scaleX == 0.0 or scaleY == 0.0):
                scaledImage = image
            else:
                scaledWidth: int = int((scaleX * float(width)))
                scaledHeight: int = int((scaleY * float(height)))
                scaledImage = self.imageScaleUtil.scale(image, scaledWidth, scaledHeight)
        else:
            scaledImage = image
        return scaledImage
    

    # throws Exception
    def processAdjust(self, baseImageAnimationFactory: BaseImageAnimationFactory) -> None:
        scaleProperties: ScaleProperties = baseImageAnimationFactory.getScalePropertiesP()
        if scaleProperties.scaleWidth != 0 and scaleProperties.scaleHeight != 0:
            animationFactoryInitializationVisitor: AnimationFactoryInitializationVisitor = baseImageAnimationFactory.getAnimationFactoryInitializationVisitorP()
            scaleX: float = (float(scaleProperties.scaleWidth)) / (float(animationFactoryInitializationVisitor.width))
            scaleY: float = (float(scaleProperties.scaleHeight)) / (float(animationFactoryInitializationVisitor.height))
            if (scaleX == 1.0 and scaleY == 1.0) or (scaleX == 0.0 or scaleY == 0.0):
                pass
            else:
                animationFactoryInitializationVisitor.dx = int((animationFactoryInitializationVisitor.originalDx * scaleX))
                animationFactoryInitializationVisitor.dy = int((animationFactoryInitializationVisitor.originalDy * scaleY))
        else:
            pass
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.image.AnimationFactoryInitializationVisitor import AnimationFactoryInitializationVisitor
from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.media.image.ImageJ2MEScaleUtil import ImageJ2MEScaleUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings


AnimationFactoryImageScaleUtil.instance = AnimationFactoryImageScaleUtil()

