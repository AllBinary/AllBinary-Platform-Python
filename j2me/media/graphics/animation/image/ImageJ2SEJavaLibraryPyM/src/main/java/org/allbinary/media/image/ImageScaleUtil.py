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
        self.imageUtil: ImageUtil = ImageUtil.getInstance()
        self.imageJ2SEUtil: ImageJ2SEUtil = ImageJ2SEUtil.getInstance()
        self.imageCreationUtil: ImageCreationUtil = ImageCreationUtil.getInstance()
    

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
        width: int = originalImage.getWidth()
        height: int = originalImage.getHeight()
        scaleX: float = scaleNominatorX / scaleDenominatorX
        scaleY: float = scaleNominatorY / scaleDenominatorY
        image: Image = None
        if cached:
            image = imageCache.get(type(self).__module__ + "." + type(self).__qualname__, int((float(width) * scaleX)), int((float(height) * scaleY)))
        else:
            image = imageCache.get("createImage", int((float(width) * scaleX)), int((float(height) * scaleY)))
        self.scale(originalImage, image, scaleX, scaleY, True)
        return image
    

    # throws Exception
    def scale2(self, originalImage: Image, originalImageArray: list[Image], ximageToShowArray: list[Image], unused: int, scaleX: float, scaleY: float, maxScaleX: float, maxScaleY: float) -> None:
        if maxScaleX * originalImage.getWidth() > originalImageArray[0].getWidth() or maxScaleY * originalImage.getHeight() > originalImageArray[0].getHeight():
            originalImageArray[0] = self.imageCreationUtil.createImage(originalImage.getWidth(), originalImage.getHeight(), maxScaleX, maxScaleY)
        self.scale(originalImage, originalImageArray[0], scaleX, scaleY, False)
    

    def scale(self, originalImage: Image, newMaxSizeImage: Image, scaleX: float, scaleY: float, clear: bool) -> None:
        bufferedImage: BufferedImage = self.imageUtil.getBufferedImage(originalImage)
        newBufferedImage: BufferedImage = self.imageUtil.getBufferedImage(newMaxSizeImage)
        at: AffineTransform = AffineTransform.getScaleInstance(scaleX, scaleY)
        g: Graphics2D = newBufferedImage.createGraphics()
        if clear:
            g.setBackground(self.imageJ2SEUtil.TRANSPARENT_COLOR)
            g.clearRect(0, 0, newBufferedImage.getWidth(), newBufferedImage.getHeight())
        g.drawRenderedImage(bufferedImage, at)
        g.dispose()
# from java.awt.Graphics2D import Graphics2D
# from java.awt.geom.AffineTransform import AffineTransform
# from java.awt.image.BufferedImage import BufferedImage
# from javax.microedition.lcdui.Image import Image
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.media.image.ImageUtil import ImageUtil
from org.allbinary.media.image.ImageJ2SEUtil import ImageJ2SEUtil
from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil


ImageScaleUtil.instance = ImageScaleUtil()

