#
# AllBinary Open License Version 1
# Copyright (c) 2023 AllBinary
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



class ImageJ2MEScaleUtil:
    instance: ImageJ2MEScaleUtil = None
    

    @staticmethod
    def getInstance() -> ImageJ2MEScaleUtil:
        return ImageJ2MEScaleUtil.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def scaleArray(self, images: list[Image], width: int, height: int) -> list[Image]:
        from org.allbinary.media.image.ImageScaleUtil import ImageScaleUtil
        for index in range(0, len(images)):
            image: Image = images[index]
            images[index] = ImageScaleUtil.getInstance().createImage2(GameFeatureImageCacheFactory.getInstance(), image, float(width) / 2.0, float(image.getWidth()), float(height), float(image.getHeight()), False)
        return images
    

    # throws Exception
    def scale(self, image: Image, width: int, height: int) -> Image:
        from org.allbinary.media.image.ImageScaleUtil import ImageScaleUtil
        return ImageScaleUtil.getInstance().createImage2(GameFeatureImageCacheFactory.getInstance(), image, float(width), float(image.getWidth()), float(height), float(image.getHeight()), False)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory


ImageJ2MEScaleUtil.instance = ImageJ2MEScaleUtil()

