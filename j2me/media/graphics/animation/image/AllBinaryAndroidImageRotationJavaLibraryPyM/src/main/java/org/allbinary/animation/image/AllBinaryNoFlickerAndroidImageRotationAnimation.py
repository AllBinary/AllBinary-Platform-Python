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


class AllBinaryNoFlickerAndroidImageRotationAnimation(ImageBaseRotationAnimation):

    def _init_fields(self) -> None:
        self.imageModifierUtil: ImageModifierUtil = ImageModifierUtil.getInstanceOrCreate()
        self.androidImageUtil: AndroidImageUtil = AndroidImageUtil.getInstance()
        self.matrix: Matrix = Matrix()
        self.halfWidth: int = None
        self.halfHeight: int = None
        self.increment: int = None
        self.originalImage: Image = None
        self.twoImages: list[Image] = [None] * (2)
        self.imageToShow: Image = None
        self.bufferedImageIndex: int = 0
    

    def __init__(self, originalImage: Image, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(image, angleInfo, totalAngle, animationBehavior)
        self._init_fields()
        self.originalImage = originalImage
        self.halfWidth = (image.getWidth() >> 1)
        self.halfHeight = (image.getHeight() >> 1)
        self.increment = ((int((self.angleInfo.getAngleIncrementInfo().getAngleIncrement())) + 32768) % 65536 - 32768)
        self.imageToShow = image
        self.twoImages[0] = image
        self.twoImages[1] = ImageCopyUtil.getInstance().createImage(image)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            self.imageModifierUtil.setColor(self.originalImage, self.imageToShow, 0, basicColor)
            changed = True
        super().setBasicColorP(basicColor)
        if changed:
            self.matrix.setRotate(0.0, float(self.halfWidth), float(self.halfHeight))
            self.updateImage()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        self.setBasicColorP(basicColor)
    

    def setAlpha(self, alpha: int) -> None:
        changed: bool = False
        if self.alphaP != alpha:
            changed = True
        super().setAlpha(alpha)
        self.imageModifierUtil.setAlpha(self.originalImage, self.imageToShow, 0, self.alphaP)
        if changed:
            self.matrix.setRotate(0.0, float(self.halfWidth), float(self.halfHeight))
            self.updateImage()
    

    def nextRotation(self) -> None:
        super().nextRotation()
        self.matrix.setRotate(float(self.increment), float(self.halfWidth), float(self.halfHeight))
        self.updateImage()
    

    def previousRotation(self) -> None:
        super().previousRotation()
        self.matrix.setRotate(float(-self.increment), float(self.halfWidth), float(self.halfHeight))
        self.updateImage()
    

    def updateImage(self) -> None:
        self.androidImageUtil.rotate(self.twoImages[self.bufferedImageIndex], self.originalImage, self.matrix, self.imageModifierUtil.paint)
        self.swap()
    

    def setFrame(self, index: int) -> None:
        currentFrame: int = self.circularIndexUtil.getIndex()
        self.circularIndexUtil.setIndex(index)
        newFrame: int = self.circularIndexUtil.getIndex()
        self.angleInfo.adjustAngle(newFrame)
        self.matrix.setRotate(float((newFrame - currentFrame)) * float(self.increment), float(self.halfWidth), float(self.halfHeight))
        self.updateImage()
    

    def swap(self) -> None:
        self.imageToShow = self.twoImages[self.bufferedImageIndex]
        if self.bufferedImageIndex == 0:
            self.bufferedImageIndex = 1
        else:
            self.bufferedImageIndex = 0
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.drawImage(self.imageToShow, x, y, self.anchor)
from android.graphics.Matrix import Matrix
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.media.image.AndroidImageUtil import AndroidImageUtil
from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil


