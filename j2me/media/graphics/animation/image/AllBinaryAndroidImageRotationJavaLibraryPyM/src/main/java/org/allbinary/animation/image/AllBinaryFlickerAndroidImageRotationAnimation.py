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
class AllBinaryFlickerAndroidImageRotationAnimation(ImageBaseRotationAnimation):
    def _java_defaults(self):
        vars(self).setdefault("imageModifierUtil", None)
        vars(self).setdefault("androidImageUtil", None)
        vars(self).setdefault("matrix", None)
        vars(self).setdefault("halfWidth", 0)
        vars(self).setdefault("halfHeight", 0)
        vars(self).setdefault("increment", 0)
        vars(self).setdefault("originalImage", None)

    def _init_fields(self) -> None:
        from android.graphics.Matrix import Matrix
        from org.allbinary.media.image.AndroidImageUtil import AndroidImageUtil
        from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
        self.imageModifierUtil: ImageModifierUtil = ImageModifierUtil.getInstanceOrCreate()
        self.androidImageUtil: AndroidImageUtil = AndroidImageUtil.getInstance()
        self.matrix: Matrix = Matrix()
        if "halfWidth" not in vars(self): self.halfWidth: int = 0
        if "halfHeight" not in vars(self): self.halfHeight: int = 0
        if "increment" not in vars(self): self.increment: int = 0
        if "originalImage" not in vars(self): self.originalImage: Image = None
    

    def __init__(self, originalImage: Image, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        super().__init__(image, angleInfo, totalAngle, animationBehavior)
        __class__._init_fields(self)
        self.originalImage = originalImage
        self.halfWidth = (image.getWidth() >> 1)
        self.halfHeight = (image.getHeight() >> 1)
        self.increment = ((int((self.angleInfo.getAngleIncrementInfo().getAngleIncrement())) + 32768) % 65536 - 32768)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            self.imageModifierUtil.setColor(self.originalImage, self.getImage(), 0, basicColor)
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
        self.imageModifierUtil.setAlpha(self.originalImage, self.getImage(), 0, self.alphaP)
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
        self.androidImageUtil.rotate(self.getImage(), self.originalImage, self.matrix, self.imageModifierUtil.paint)
    

    def setFrame(self, index: int) -> None:
        currentFrame: int = self.circularIndexUtil.getIndex()
        self.circularIndexUtil.setIndex(index)
        newFrame: int = self.circularIndexUtil.getIndex()
        self.angleInfo.adjustAngle(newFrame)
        self.matrix.setRotate(float((newFrame - currentFrame)) * float(self.increment), float(self.halfWidth), float(self.halfHeight))
        self.updateImage()
# from android.graphics.Matrix import Matrix
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.media.image.AndroidImageUtil import AndroidImageUtil
# from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil


