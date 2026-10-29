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
# package org.allbinary.animation.image

from __future__ import annotations

from org.allbinary.animation.image.ImageBaseRotationAnimation import ImageBaseRotationAnimation


class AllBinaryHTMLImageRotationAnimation(ImageBaseRotationAnimation):

    def _init_fields(self) -> None:
        self.imageRotationUtil: ImageRotationUtil = ImageRotationUtil.getInstance()
        self.imageModifierUtil: ImageModifierUtil = ImageModifierUtil.getInstanceOrCreate()
        self.originalImage: Image = None
        self.twoImages: list[Image] = [None] * (2)
        self.canvasSurfaceArray: list[Canvas] = [None] * (2)
        self.imageToShow: Image = None
        self.bufferedImageIndex: int = 0
        self.alphaProcessor: AlphaBaseProcessor = AlphaBaseProcessor.getInstance()
    

    def __init__(self, originalImage: Image, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(image, angleInfo, totalAngle, animationBehavior)
        self._init_fields()
        self.originalImage = originalImage
        self.imageToShow = image
        self.twoImages[0] = image
        self.twoImages[1] = ImageCopyUtil.getInstance().createImage(image)
        self.canvasSurfaceArray[0] = self.getCanvasSurface(self.twoImages[0])
        self.canvasSurfaceArray[1] = self.getCanvasSurface(self.twoImages[1])
    

    def getCanvasSurface(self, image: Image) -> Canvas:
        htmlImage: PlaynMutableImage = image
        canvasImage: ImageImpl = htmlImage.getImage()
        playN: PlayN = PlayN.getInstance()
        canvas: Canvas = (playN.graphics()).get(canvasImage)
        canvas.translate(self.originalImage.getWidth() / 2, self.originalImage.getHeight() / 2)
        return canvas
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            changed = True
        super().setBasicColorP(basicColor)
        if changed:
            self.updateImage()
    

    def setAlpha(self, alpha: int) -> None:
        from org.allbinary.animation.image.AlphaProcessor import AlphaProcessor
        changed: bool = False
        if self.alphaP != alpha:
            changed = True
        super().setAlpha(alpha)
        if changed:
            self.alphaProcessor = AlphaProcessor.getInstance()
            self.updateImage()
    

    def nextRotation(self) -> None:
        super().nextRotation()
        self.updateImage()
    

    def previousRotation(self) -> None:
        super().previousRotation()
        self.updateImage()
    

    def updateImage(self) -> None:
        canvasSurface: Canvas = self.canvasSurfaceArray[self.bufferedImageIndex]
        canvasSurface.save()
        self.imageRotationUtil.rotateImageCanvasSurfaceClear(self.originalImage, self.twoImages[self.bufferedImageIndex], canvasSurface, self.angleInfo.getAngle() + 90)
        self.alphaProcessor.setAlpha(self.imageModifierUtil, self.originalImage, self.twoImages[self.bufferedImageIndex], self.alphaP)
        self.imageRotationUtil.drawImage(self.originalImage, self.imageToShow, canvasSurface)
        canvasSurface.restore()
        self.swap()
    

    def setFrame(self, index: int) -> None:
        super().setFrame(index)
        self.updateImage()
    

    def swap(self) -> None:
        self.imageToShow = self.twoImages[self.bufferedImageIndex]
        if self.bufferedImageIndex == 0:
            self.bufferedImageIndex = 1
        else:
            self.bufferedImageIndex = 0
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.drawImage(self.imageToShow, x, y, self.anchor)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
from org.allbinary.media.image.ImageRotationUtil import ImageRotationUtil
from org.microemu.device.playn.PlaynMutableImage import PlaynMutableImage
from playn.core.Canvas import Canvas
from playn.core.ImageImpl import ImageImpl
from playn.core.PlayN import PlayN
from playn.html.HtmlGraphics import HtmlGraphics
from playn.html.HtmlImage import HtmlImage
from org.allbinary.animation.image.AlphaBaseProcessor import AlphaBaseProcessor


