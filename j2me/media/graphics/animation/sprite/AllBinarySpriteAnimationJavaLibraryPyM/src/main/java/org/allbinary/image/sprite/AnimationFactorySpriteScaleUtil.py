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
# package org.allbinary.image.sprite

from __future__ import annotations



class AnimationFactorySpriteScaleUtil:
    instance: AnimationFactorySpriteScaleUtil = None

    def _init_fields(self) -> None:
        self.imageCache: ImageCache = ImageCacheFactory.getInstance()
        self.imageScaleUtil: ImageScaleUtil = ImageScaleUtil.getInstance()
        self.openGLUtil: OpenGLUtil = OpenGLUtil.getInstance()
        self.j2seMath: J2SEMath = J2SEMath.getInstance()
        self.openGLESImageExclusionUtil: OpenGLESImageExclusionUtil = OpenGLESImageExclusionUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AnimationFactorySpriteScaleUtil:
        return AnimationFactorySpriteScaleUtil.instance
    

    # throws Exception
    def createImage(self, image: Image, width: int, height: int, scaleWidth: int, scaleHeight: int) -> Sprite:
        spriteFactory: SpriteFactory = SpriteFactory.getInstance()
        sprite: Sprite = None
        scaledImage: Image = None
        if scaleWidth != 0 and scaleHeight != 0:
            scaleX: float = (float(scaleWidth)) / (float(width))
            scaleY: float = (float(scaleHeight)) / (float(height))
            if (scaleX == 1.0 and scaleY == 1.0) or (scaleX == 0.0 or scaleY == 0.0):
                scaledImage = self.openGLUtil.addImage(image)
                sprite = spriteFactory.createSprite(scaledImage, width, height)
            else:
                if self.openGLESImageExclusionUtil.isCustomScaling(image):
                    width2: int = self.j2seMath.round(float((scaleWidth)) - 0.5)
                    height2: int = self.j2seMath.round(float((scaleHeight)) - 0.5)
                    multiplesOf16Width: int = int(width2 / 16)
                    by16Width: int = multiplesOf16Width * 16
                    scaleX = (float(by16Width)) / float(width)
                    multiplesOf16Height: int = int(height2 / 16)
                    by16Height: int = multiplesOf16Height * 16
                    scaleY = (float(by16Height)) / float(height)
                    if scaleWidth < width:
                        scaleX = scaleX * 2.35
                    if scaleHeight < height:
                        scaleY = scaleY * 2.35
                scaledImage = self.imageScaleUtil.createImage2(self.imageCache, image, scaleX, 1.0, scaleY, 1.0, True)
                sprite = spriteFactory.createSprite(scaledImage, int((float(width) * scaleX)), int((float(height) * scaleY)))
        else:
            scaledImage = self.openGLUtil.addImage(image)
            sprite = spriteFactory.createSprite(scaledImage, width, height)
        return sprite
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.game.Sprite import Sprite
from org.allbinary.game.layer.SpriteFactory import SpriteFactory
from org.allbinary.graphics.opengles.OpenGLUtil import OpenGLUtil
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
from org.allbinary.image.opengles.OpenGLESImageExclusionUtil import OpenGLESImageExclusionUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.J2SEMath import J2SEMath
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.image.ImageScaleUtil import ImageScaleUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings


AnimationFactorySpriteScaleUtil.instance = AnimationFactorySpriteScaleUtil()

