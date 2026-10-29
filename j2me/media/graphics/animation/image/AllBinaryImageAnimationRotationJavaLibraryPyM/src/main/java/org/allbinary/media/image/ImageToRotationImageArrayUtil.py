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



class ImageToRotationImageArrayUtil:
    instance: ImageToRotationImageArrayUtil = None
    

    @staticmethod
    def getInstance() -> ImageToRotationImageArrayUtil:
        return ImageToRotationImageArrayUtil.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def generate(self, image: Image, angleIncrement: int, totalAngle: int) -> list[Image]:
        from org.allbinary.media.image.ImageRotationUtil import ImageRotationUtil
        imageRotationUtil: ImageRotationUtil = ImageRotationUtil.getInstance()
        totalFrames: int = int(totalAngle / angleIncrement)
        imageArray: list[Image] = [None] * (totalFrames)
        imageArray[0] = image
        for index in range(1, totalFrames):
            imageArray[index] = imageRotationUtil.createRotatedImage(image, index * angleIncrement)
        return imageArray
# from javax.microedition.lcdui.Image import Image


ImageToRotationImageArrayUtil.instance = ImageToRotationImageArrayUtil()

