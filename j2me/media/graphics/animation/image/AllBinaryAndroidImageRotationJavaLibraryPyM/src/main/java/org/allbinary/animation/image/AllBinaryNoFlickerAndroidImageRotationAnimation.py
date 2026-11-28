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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.image.ImageBaseRotationAnimation import ImageBaseRotationAnimation


@java_inherited_overloads
class AllBinaryNoFlickerAndroidImageRotationAnimation(ImageBaseRotationAnimation):
    def _java_defaults(self):
        vars(self).setdefault("imageModifierUtil", None)
        vars(self).setdefault("androidImageUtil", None)
        vars(self).setdefault("matrix", None)
        vars(self).setdefault("halfWidth", 0)
        vars(self).setdefault("halfHeight", 0)
        vars(self).setdefault("increment", 0)
        vars(self).setdefault("originalImage", None)
        vars(self).setdefault("twoImages", None)
        vars(self).setdefault("imageToShow", None)
        vars(self).setdefault("bufferedImageIndex", 0)

    def _init_fields(self) -> None:
        from android.graphics.Matrix import Matrix
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.media.image.AndroidImageUtil import AndroidImageUtil
        from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
        self.imageModifierUtil: ImageModifierUtil = ImageModifierUtil.getInstanceOrCreate()
        self.androidImageUtil: AndroidImageUtil = AndroidImageUtil.getInstance()
        self.matrix: Matrix = Matrix()
        if "halfWidth" not in vars(self): self.halfWidth: int = 0
        if "halfHeight" not in vars(self): self.halfHeight: int = 0
        if "increment" not in vars(self): self.increment: int = 0
        if "originalImage" not in vars(self): self.originalImage: Image = None
        self.twoImages: list[Image] = [None] * (2)
        if "imageToShow" not in vars(self): self.imageToShow: Image = None
        if "bufferedImageIndex" not in vars(self): self.bufferedImageIndex: int = 0
    

    def __init__(self, originalImage: Image, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
        super().__init__(image, angleInfo, totalAngle, animationBehavior)
        __class__._init_fields(self)
        self.originalImage = originalImage
        self.halfWidth = (image.getWidth() >> 1)
        self.halfHeight = (image.getHeight() >> 1)
        self.increment = ((int((self.angleInfo.getAngleIncrementInfo().getAngleIncrement())) + 32768) % 65536 - 32768)
        self.imageToShow = image
        self.twoImages[0] = image
        self.twoImages[1] = ImageCopyUtil.getInstance().createImage(image)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            self.imageModifierUtil.setColor(self.originalImage, self.imageToShow, 0, basicColor)
            changed = True
        java_super_call(super(), "setBasicColorP", basicColor)
        if changed:
            self.matrix.setRotate(0.0, float(self.halfWidth), float(self.halfHeight))
            self.updateImage()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.setBasicColorP(basicColor)
    

    def setAlpha(self, alpha: int) -> None:
        changed: bool = False
        if self.alphaP != alpha:
            changed = True
        java_super_call(super(), "setAlpha", alpha)
        self.imageModifierUtil.setAlpha(self.originalImage, self.imageToShow, 0, self.alphaP)
        if changed:
            self.matrix.setRotate(0.0, float(self.halfWidth), float(self.halfHeight))
            self.updateImage()
    

    def nextRotation(self) -> None:
        java_super_call(super(), "nextRotation")
        self.matrix.setRotate(float(self.increment), float(self.halfWidth), float(self.halfHeight))
        self.updateImage()
    

    def previousRotation(self) -> None:
        java_super_call(super(), "previousRotation")
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
        from javax.microedition.lcdui.Graphics import Graphics
        graphics.drawImage(self.imageToShow, x, y, self.anchor)
# from android.graphics.Matrix import Matrix
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.media.image.AndroidImageUtil import AndroidImageUtil
# from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
# from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil


