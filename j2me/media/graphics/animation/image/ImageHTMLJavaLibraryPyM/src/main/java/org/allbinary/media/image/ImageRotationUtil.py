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

import math


class ImageRotationUtil:
    instance: ImageRotationUtil = None
    

    @staticmethod
    def getInstance() -> ImageRotationUtil:
        return ImageRotationUtil.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def createRotatedImage(self, originalImage: Image, rotationInDegrees: int) -> Image:
        from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil
        image: Image = ImageCreationUtil.getInstance().getInstance(originalImage.getWidth(), originalImage.getHeight())
        if image.isMutable():
            originalPlayNImage: Image = None
            if originalImage.isMutable():
                originalHTMLImage: PlaynMutableImage = originalImage
                originalPlayNImage = originalHTMLImage.getImage()
            else:
                originalHTMLImage: PlaynImmutableImage = originalImage
                originalPlayNImage = originalHTMLImage.getImage()
            htmlImage: PlaynMutableImage = image
            canvasImage: CanvasImage = htmlImage.getImage()
            canvasSurface: CanvasSurface = htmlImage.getCanvasSurface(canvasImage)
            canvasSurface.translate(originalPlayNImage.width() / 2, originalPlayNImage.height() / 2)
            canvasSurface.rotate(float(math.radians(rotationInDegrees)))
            canvasSurface.drawImage(originalPlayNImage, -originalPlayNImage.width() / 2, -originalPlayNImage.height() / 2)
            return image
        else:
            raise Exception("Not Mutable")
# from javax.microedition.lcdui.Image import Image
from org.microemu.device.playn.PlaynImmutableImage import PlaynImmutableImage
from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
from playn.core.CanvasImage import CanvasImage
from playn.core.CanvasSurface import CanvasSurface


ImageRotationUtil.instance = ImageRotationUtil()

