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

    def _init_fields(self) -> None:
        self.playnUtil: HTMLPlaynUtil = HTMLPlaynUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageScaleUtil:
        return ImageScaleUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createImage2(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool) -> Image:
        return self.createImage3(imageCache, originalImage, scaleNominatorX, scaleDenominatorX, scaleNominatorY, scaleDenominatorY, cached, True)
    

    # throws Exception
    def createImage3(self, imageCache: ImageCache, originalImage: Image, scaleNominatorX: float, scaleDenominatorX: float, scaleNominatorY: float, scaleDenominatorY: float, cached: bool, mutable: bool) -> Image:
        scaleX: float = scaleNominatorX / scaleDenominatorX
        scaleY: float = scaleNominatorY / scaleDenominatorY
        return self.createImage(imageCache, originalImage, scaleX, scaleY, cached)
    

    # throws Exception
    def createImage(self, imageCache: ImageCache, originalImage: Image, scaleX: float, scaleY: float, cached: bool) -> Image:
        return self.createImageInternal(originalImage, scaleX, scaleY)
    

    # throws Exception
    def createImageInternal(self, originalImage: Image, scaleX: float, scaleY: float) -> Image:
        from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil
        image: Image = ImageCreationUtil.getInstance().createImageWH(int((originalImage.getWidth() * scaleX)), int((originalImage.getHeight() * scaleY)))
        if image.isMutable():
            originalPlayNImage: CoreImage = None
            if originalImage.isMutable():
                originalHTMLImage: PlaynMutableImage = originalImage
                originalPlayNImage = originalHTMLImage.getImage()
            else:
                originalHTMLImage: PlaynImmutableImage = originalImage
                originalPlayNImage = originalHTMLImage.getImage()
            htmlImage: PlaynMutableImage = image
            canvasImage: ImageImpl = htmlImage.getImage()
            canvas: Canvas = self.playnUtil.getCanvas(canvasImage)
            canvas.drawScale(originalPlayNImage, 0, 0, image.getWidth(), image.getHeight(), 0, 0, originalImage.getWidth(), originalImage.getHeight())
            return image
        else:
            raise Exception("Not Mutable")
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.ImageCache import ImageCache
from org.microemu.device.playn.PlaynImmutableImage import PlaynImmutableImage
from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
from playn.core.Canvas import Canvas
from playn.core.CoreImage import CoreImage
from playn.core.ImageImpl import ImageImpl
from playn.html.HTMLPlaynUtil import HTMLPlaynUtil


ImageScaleUtil.instance = ImageScaleUtil()

