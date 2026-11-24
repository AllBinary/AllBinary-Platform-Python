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
from java.lang.JavaRuntimeStatic import lazy_static


class ImageRotationUtil:
    instance: ImageRotationUtil = None

    def _init_fields(self) -> None:
        from playn.html.HTMLPlaynUtil import HTMLPlaynUtil
        self.playnUtil: HTMLPlaynUtil = HTMLPlaynUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ImageRotationUtil:
        return ImageRotationUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def rotateImage(self, originalImage: Image, image: Image, totalAngle: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
        from playn.core.Canvas import Canvas
        from playn.core.ImageImpl import ImageImpl
        if image.isMutable():
            htmlImage: PlaynMutableImage = image
            canvasImage: ImageImpl = htmlImage.getImage()
            canvas: Canvas = self.playnUtil.getCanvas(canvasImage)
            canvas.save()
            canvas.clear()
            canvas.translate(originalImage.getWidth() / 2, originalImage.getHeight() / 2)
            image2: Image = self.rotateImageCanvasSurface(originalImage, image, canvas, totalAngle)
            self.drawImage(originalImage, image, canvas)
            canvas.restore()
            return image2
        else:
            return None
    

    def rotateImageCanvasSurfaceClear(self, originalImage: Image, image: Image, canvasSurface: Canvas, totalAngle: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from playn.core.Canvas import Canvas
        if image.isMutable():
            canvasSurface.translate(-originalImage.getWidth() / 2, -originalImage.getHeight() / 2)
            canvasSurface.clear()
            canvasSurface.translate(originalImage.getWidth() / 2, originalImage.getHeight() / 2)
            return self.rotateImageCanvasSurface(originalImage, image, canvasSurface, totalAngle)
        else:
            return None
    

    def rotateImageCanvasSurface(self, originalImage: Image, image: Image, canvasSurface: Canvas, totalAngle: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from playn.core.Canvas import Canvas
        if image.isMutable():
            canvasSurface.rotate(float(math.radians(totalAngle)))
            return image
        else:
            return None
    

    def drawImage(self, originalImage: Image, image: Image, canvasSurface: Canvas) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.microemu.device.playn.PlaynImmutableImage import PlaynImmutableImage
        from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
        from playn.core.Canvas import Canvas
        from playn.core.CoreImage import CoreImage
        originalPlayNImage: CoreImage = None
        if originalImage.isMutable():
            originalHTMLImage: PlaynMutableImage = originalImage
            originalPlayNImage = originalHTMLImage.getImage()
        else:
            originalHTMLImage: PlaynImmutableImage = originalImage
            originalPlayNImage = originalHTMLImage.getImage()
        canvasSurface.draw(originalPlayNImage, -originalImage.getWidth() / 2, -originalImage.getHeight() / 2)
    

    # throws Exception
    def createRotatedImage(self, originalImage: Image, rotationInDegrees: int) -> Image:
        from org.allbinary.media.image.ImageCreationUtil import ImageCreationUtil
        from javax.microedition.lcdui.Image import Image
        image: Image = ImageCreationUtil.getInstance().createImageWH(originalImage.getWidth(), originalImage.getHeight())
        rotatedImage: Image = self.rotateImage(originalImage, image, rotationInDegrees)
        if rotatedImage is None:
            raise Exception("Not Mutable")
        return rotatedImage
# from javax.microedition.lcdui.Image import Image
# from org.microemu.device.playn.PlaynImmutableImage import PlaynImmutableImage
# from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
# from playn.core.Canvas import Canvas
# from playn.core.CoreImage import CoreImage
# from playn.core.ImageImpl import ImageImpl
# from playn.html.HTMLPlaynUtil import HTMLPlaynUtil


def _ImageRotationUtil_instance() -> object:
    return ImageRotationUtil()

lazy_static(ImageRotationUtil, "instance", _ImageRotationUtil_instance)

