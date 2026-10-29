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



class ImageScaleUtil:
    instance: ImageScaleUtil = None
    

    @staticmethod
    def getInstance() -> ImageScaleUtil:
        return ImageScaleUtil.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def createImage2(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool) -> Image:
        return self.createImage3(imageCache, originalImage, scaleNominatorX, scaleDenominatorX, scaleNominatorY, scaleDenominatorY, cached, True)
    

    # throws Exception
    def createImage3(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool, mutable: bool) -> Image:
        return originalImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.ImageCache import ImageCache


ImageScaleUtil.instance = ImageScaleUtil()

