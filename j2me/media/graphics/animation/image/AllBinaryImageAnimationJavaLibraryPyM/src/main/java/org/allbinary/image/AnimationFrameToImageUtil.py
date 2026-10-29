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
# package org.allbinary.image

from __future__ import annotations



class AnimationFrameToImageUtil:
    instance: AnimationFrameToImageUtil = None
    

    @staticmethod
    def getInstance() -> AnimationFrameToImageUtil:
        return AnimationFrameToImageUtil.instance
    

    # throws Exception
    def getInstanceTranslate(self, width: int, height: int, animationInterface: Animation) -> Image:
        from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
        image: Image = GameFeatureImageCacheFactory.getInstance().get(type(AnimationFrameToImageUtil.instance).__module__ + "." + type(AnimationFrameToImageUtil.instance).__qualname__, ((width * 3) >> 1), ((height * 3) >> 1))
        graphics: Graphics = image.getGraphics()
        tranlateX: int = (width >> 2)
        tranlateY: int = (height >> 2)
        graphics.translate(tranlateX, tranlateY)
        animationInterface.paintXY(graphics, 0, 0)
        graphics.translate(-tranlateX, -tranlateY)
        return image
    

    # throws Exception
    def getInstanceWH(self, width: int, height: int, animationInterface: Animation) -> Image:
        from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
        image: Image = GameFeatureImageCacheFactory.getInstance().get(type(AnimationFrameToImageUtil.instance).__module__ + "." + type(AnimationFrameToImageUtil.instance).__qualname__, width, height)
        graphics: Graphics = image.getGraphics()
        animationInterface.paintXY(graphics, 0, 0)
        return image
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.Animation import Animation


AnimationFrameToImageUtil.instance = AnimationFrameToImageUtil()

