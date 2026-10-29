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


class AllBinaryJ2SEImageRotationAnimation(ImageBaseRotationAnimation):

    def _init_fields(self) -> None:
        self.imageRotationUtil: ImageRotationUtil = ImageRotationUtil.getInstance()
        self.imageModifierUtil: ImageModifierUtil = ImageModifierUtil.getInstanceOrCreate()
        self.realOriginalImage: Image = None
        self.originalImageArray: list[Image] = [None] * (1)
        self.twoImages: list[Image] = [None] * (2)
        self.imageToShow: Image = None
        self.bufferedImageIndex: int = 0
        self.lastScaleX: float = 1.0
        self.lastScaleY: float = 1.0
        self.scaleX: float = 1.0
        self.scaleY: float = 1.0
        self.maxScaleX: float = 0.0
        self.maxScaleY: float = 0.0
        self.alphaProcessor: ModifierBaseProcessor = ModifierBaseProcessor.getInstance()
        self.setColorProcessor: ModifierBaseProcessor = ModifierBaseProcessor.getInstance()
        self.changeColorProcessor: ModifierBaseProcessor = ModifierBaseProcessor.getInstance()
        self.scaleProcessor: ScaleBaseProcessor = ScaleProcessor.getInstance()
    

    def __init__(self, originalImage: Image, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(image, angleInfo, totalAngle, animationBehavior)
        self._init_fields()
        self.realOriginalImage = originalImage
        self.originalImageArray[0] = originalImage
        self.imageToShow = image
        self.twoImages[0] = image
        self.twoImages[1] = ImageCopyUtil.getInstance().createImageForRotation(image)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.animation.image.SetColorProcessor import SetColorProcessor
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            changed = True
        super().setBasicColorP(basicColor)
        if changed:
            self.setColorProcessor = SetColorProcessor.getInstance()
            self.updateImage()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        from org.allbinary.animation.image.ChangeColorProcessor import ChangeColorProcessor
        changed: bool = False
        if self.getChangeBasicColor() is None or int(self.getChangeBasicColor()) != int(basicColor):
            changed = True
        super().changeBasicColor(basicColor)
        if changed:
            self.changeColorProcessor = ChangeColorProcessor.getInstance()
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
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        self.scaleX = scaleX
        self.scaleY = scaleY
        if self.scaleX != self.lastScaleX or self.scaleY != self.lastScaleY:
            self.scaleProcessor.update(self.realOriginalImage, self.originalImageArray, self.twoImages, self.bufferedImageIndex, self.scaleX, self.scaleY, self.maxScaleX, self.maxScaleY)
            self.updateImage()
        self.lastScaleX = self.scaleX
        self.lastScaleY = self.scaleY
    

    def setMaxScale(self, maxScaleX: float, maxScaleY: float) -> None:
        self.maxScaleX = maxScaleX
        self.maxScaleY = maxScaleY
        self.scaleProcessor.update(self.realOriginalImage, self.originalImageArray, self.twoImages, self.bufferedImageIndex, self.scaleX, self.scaleY, self.maxScaleX, self.maxScaleY)
        self.updateImage()
    

    def nextRotation(self) -> None:
        super().nextRotation()
        self.updateImage()
    

    def previousRotation(self) -> None:
        super().previousRotation()
        self.updateImage()
    

    def updateImage(self) -> None:
        self.imageRotationUtil.rotateImage(self.originalImageArray[0], self.twoImages[self.bufferedImageIndex], self.angleInfo.getAngle() + 90)
        self.alphaProcessor.updateAlpha(self.imageModifierUtil, NullImage.NULL_IMAGE, self.twoImages[self.bufferedImageIndex], 0, self.alphaP)
        self.setColorProcessor.updateColor(self.imageModifierUtil, NullImage.NULL_IMAGE, self.twoImages[self.bufferedImageIndex], 0, self.basicColor)
        self.changeColorProcessor.updateColor(self.imageModifierUtil, NullImage.NULL_IMAGE, self.twoImages[self.bufferedImageIndex], 0, self.changeBasicColorP)
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
    

    # throws Exception
    def close(self) -> None:
        super().close()
        disposalUtil: DisposalUtil = DisposalUtil.getInstance()
        size2: int = len(self.twoImages)
        for index in range(0, size2):
            disposalUtil.disposeImage(self.twoImages[index])
        size: int = len(self.originalImageArray)
        for index in range(0, size):
            disposalUtil.disposeImage(self.originalImageArray[index])
        disposalUtil.disposeImage(self.realOriginalImage)
        disposalUtil.disposeImage(self.imageToShow)
    

    # throws Throwable
    def finalize(self) -> None:
        super().finalize()
        disposalUtil: DisposalUtil = DisposalUtil.getInstance()
        size2: int = len(self.twoImages)
        for index in range(0, size2):
            disposalUtil.disposeImage(self.twoImages[index])
        size: int = len(self.originalImageArray)
        for index in range(0, size):
            disposalUtil.disposeImage(self.originalImageArray[index])
        disposalUtil.disposeImage(self.realOriginalImage)
        disposalUtil.disposeImage(self.imageToShow)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.DisposalUtil import DisposalUtil
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
from org.allbinary.media.image.ImageRotationUtil import ImageRotationUtil
from org.allbinary.animation.image.ModifierBaseProcessor import ModifierBaseProcessor
from org.allbinary.animation.image.ScaleProcessor import ScaleProcessor


