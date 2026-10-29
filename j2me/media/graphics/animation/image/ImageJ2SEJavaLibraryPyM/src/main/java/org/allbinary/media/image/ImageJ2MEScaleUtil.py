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
        scaledImages: list[Image] = [None] * (len(images))
        index = len(images)
        while (index := index - 1) >= 0:
            scaledImages[index] = self.scale(images[index], width, height)
        return scaledImages
    

    # throws Exception
    def scale(self, image: Image, width: int, height: int) -> Image:
        sourceWidth: int = image.getWidth()
        sourceHeight: int = image.getHeight()
        originalData: list[int] = [0] * (image.getWidth() * image.getHeight())
        image.getRGB(originalData, 0, image.getWidth(), 0, 0, image.getWidth(), image.getHeight())
        scaledData: list[int] = [0] * (width * height)
        heightRatioFactor: int = int((8 * sourceHeight) / height)
        widthRatioFactor: int = int((8 * sourceWidth) / width)
        scaledIndex: int = len(scaledData) - 1
        dx: int = 0
        dy: int = 0
        index = height
        while (index := index - 1) >= 0:
            dy = (index * heightRatioFactor) >> 3
            index2 = width
            while (index2 := index2 - 1) >= 0:
                dx = (index2 * widthRatioFactor) >> 3
                scaledData[((scaledIndex := scaledIndex - 1) + 1)] = originalData[(sourceWidth * dy) + dx]
        scaledImage: Image = Image.createRGBImage(scaledData, width, height, True)
        return scaledImage
# from javax.microedition.lcdui.Image import Image


ImageJ2MEScaleUtil.instance = ImageJ2MEScaleUtil()

