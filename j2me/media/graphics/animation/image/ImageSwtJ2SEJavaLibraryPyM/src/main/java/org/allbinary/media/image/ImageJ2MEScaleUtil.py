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
        scaledImages: list[Image] = [None] * (len(images))
        index = len(images)
        while (index := index - 1) >= 0:
            scaledImages[index] = self.scale(images[index], width, height)
        return scaledImages
    

    # throws Exception
    def scale(self, image: Image, width: int, height: int) -> Image:
        from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
        scaledImage: Image = ImageCopyUtil.getInstance().createImageWH(image, width, height, True)
        return scaledImage
# from javax.microedition.lcdui.Image import Image


ImageJ2MEScaleUtil.instance = ImageJ2MEScaleUtil()

