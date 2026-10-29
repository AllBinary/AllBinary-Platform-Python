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

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageJ2MEScaleUtil:
        return ImageJ2MEScaleUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def scaleArray(self, images: list[Image], width: int, height: int) -> list[Image]:
        scaledImages: list[Image] = [None] * (len(images))
        index = len(images)
        while (index := index - 1) >= 0:
            scaledImages[index] = self.scale(images[index], width, height)
        return scaledImages
    

    # throws Exception
    def scale(self, image: Image, width: int, height: int) -> Image:
        originalPlayNImage: Image = None
        if image.isMutable():
            originalHTMLImage: PlaynMutableImage = image
            originalPlayNImage = originalHTMLImage.getImage()
        else:
            originalHTMLImage: PlaynImmutableImage = image
            originalPlayNImage = originalHTMLImage.getImage()
        scaledImage: Image = Image.createImage(width, height)
        htmlImage: PlaynMutableImage = scaledImage
        canvasImage: CanvasImage = htmlImage.getImage()
        canvasSurface: CanvasSurface = htmlImage.getCanvasSurface(canvasImage)
        canvasSurface.drawImage(originalPlayNImage, 0, 0, scaledImage.getWidth(), scaledImage.getHeight(), 0, 0, image.getWidth(), image.getHeight())
        return scaledImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.microemu.device.playn.PlaynImmutableImage import PlaynImmutableImage
from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
from playn.core.CanvasImage import CanvasImage
from playn.core.CanvasSurface import CanvasSurface


ImageJ2MEScaleUtil.instance = ImageJ2MEScaleUtil()

