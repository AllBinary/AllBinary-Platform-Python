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
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.RotationAnimation import RotationAnimation


@java_inherited_overloads
class ImageArrayBaseRotationAnimation(RotationAnimation):
    def _java_defaults(self):
        vars(self).setdefault("imageModifierUtil", None)
        vars(self).setdefault("originalImageArray", None)
        vars(self).setdefault("imageArray", None)
        vars(self).setdefault("currentImage", None)
        vars(self).setdefault("totalFrames", 0)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.NullImage import NullImage
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
        self.imageModifierUtil: ImageModifierUtil = ImageModifierUtil.getInstanceOrCreate()
        if "originalImageArray" not in vars(self): self.originalImageArray: list[Image] = None
        self.imageArray: list[Image] = NullImage.NULL_IMAGE_ARRAY
        if "currentImage" not in vars(self): self.currentImage: Image = None
        if "totalFrames" not in vars(self): self.totalFrames: int = 0
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, originalImageArray: list[Image], angleInfo: AngleInfo, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(angleInfo, CircularIndexUtil.createInstance(java_divide(360, angleInfo.getAngleIncrementInfo().getAngleIncrement())
            ), animationBehavior)
        __class__._init_fields(self)
        self.originalImageArray = originalImageArray
        self.setImageArray(self.imageModifierUtil.getImageArray(originalImageArray))
        self.currentImage = self.imageArray[self.circularIndexUtil.getIndex()]
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def setAlpha(self, alpha: int) -> None:
        if self.alphaP != alpha:
            java_super_call(super(), "setAlpha", alpha)
            self.imageModifierUtil.reset()
            index: int = self.circularIndexUtil.getIndex()
            self.imageModifierUtil.setAlpha(self.originalImageArray[index], self.imageArray[index], index, self.alphaP)
    

    def nextRotation(self) -> None:
        java_super_call(super(), "nextRotation")
        index: int = self.circularIndexUtil.getIndex()
        self.imageModifierUtil.setAlpha(self.originalImageArray[index], self.imageArray[index], index, self.alphaP)
        self.currentImage = self.imageArray[index]
    

    def previousRotation(self) -> None:
        java_super_call(super(), "previousRotation")
        index: int = self.circularIndexUtil.getIndex()
        self.imageModifierUtil.setAlpha(self.originalImageArray[index], self.imageArray[index], index, self.alphaP)
        self.currentImage = self.imageArray[index]
    

    def setFrame(self, index2: int) -> None:
        java_super_call(super(), "setFrame", index2)
        index: int = self.circularIndexUtil.getIndex()
        self.imageModifierUtil.setAlpha(self.originalImageArray[index], self.imageArray[index], index, self.alphaP)
        self.currentImage = self.imageArray[index]
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        return PrimitiveIntUtil.getArrayInstance()
    

    def setImageArray(self, imageArray: list[Image]) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        self.imageArray = imageArray
        self.totalFrames = len(imageArray)
        self.circularIndexUtil = CircularIndexUtil.createInstance(self.totalFrames)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        graphics.drawImage(self.currentImage, x, y, self.anchor)
    

    # throws Exception
    def close(self) -> None:
        from org.allbinary.DisposalUtil import DisposalUtil
        disposalUtil: DisposalUtil = DisposalUtil.getInstance()
        size2: int = len(self.imageArray)
        for index in range(0, size2):
            disposalUtil.disposeImage(self.imageArray[index])
        size: int = len(self.originalImageArray)
        for index in range(0, size):
            disposalUtil.disposeImage(self.originalImageArray[index])
        disposalUtil.disposeImage(self.currentImage)
    

    # throws Throwable
    def finalize(self) -> None:
        from org.allbinary.DisposalUtil import DisposalUtil
        disposalUtil: DisposalUtil = DisposalUtil.getInstance()
        size2: int = len(self.imageArray)
        for index in range(0, size2):
            disposalUtil.disposeImage(self.imageArray[index])
        size: int = len(self.originalImageArray)
        for index in range(0, size):
            disposalUtil.disposeImage(self.originalImageArray[index])
        disposalUtil.disposeImage(self.currentImage)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.DisposalUtil import DisposalUtil
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.media.image.ImageModifierUtil import ImageModifierUtil
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


