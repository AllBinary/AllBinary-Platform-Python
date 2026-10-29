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
# package org.allbinary.media.image

from __future__ import annotations



class ImageCreationUtil:
    instance: ImageCreationUtil = None
    

    @staticmethod
    def getInstance() -> ImageCreationUtil:
        return ImageCreationUtil.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def createImageWH(self, width: int, height: int) -> Image:
        image: Image = GameFeatureImageCacheFactory.getInstance().get(type(self).__module__ + "." + type(self).__qualname__, width, height)
        return image
    

    # throws Exception
    def createImage(self, width: int, height: int, maxScaleX: float, maxScaleY: float) -> Image:
        image: Image = GameFeatureImageCacheFactory.getInstance().get(type(self).__module__ + "." + type(self).__qualname__, int((float(width) * maxScaleX)) + 1, int((float(height) * maxScaleY)) + 1)
        return image
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory


ImageCreationUtil.instance = ImageCreationUtil()

