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



class PaintableToImageUtil:
    instance: PaintableToImageUtil = None
    

    # throws Exception
    @staticmethod
    def getImage(paintableInterface: PaintableInterface, width: int, height: int) -> Image:
        from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
        image: Image = GameFeatureImageCacheFactory.getInstance().get(type(PaintableToImageUtil.instance).__module__ + "." + type(PaintableToImageUtil.instance).__qualname__, width, height)
        graphics: Graphics = image.getGraphics()
        paintableInterface.paint(graphics)
        return image
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


PaintableToImageUtil.instance = PaintableToImageUtil()

