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

from org.allbinary.animation.IndexedAnimation import IndexedAnimation


class ImageArrayAnimation(IndexedAnimation):

    def _init_fields(self) -> None:
        self.imageArray: list[Image] = NullImage.NULL_IMAGE_ARRAY
        self.totalFrames: int = 0
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.NULL_CIRCULAR_INDEX_UTIL
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, imageArray: list[Image], animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.setImageArray(imageArray)
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def nextFrame(self) -> None:
        self.circularIndexUtil.next()
    

    def previousFrame(self) -> None:
        self.circularIndexUtil.previous()
    

    def setFrame(self, index: int) -> None:
        self.circularIndexUtil.setIndex(index)
    

    def getFrame(self) -> int:
        return self.circularIndexUtil.getIndex()
    

    def getSize(self) -> int:
        return self.totalFrames
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def getImage(self, index: int) -> Image:
        return self.imageArray[index]
    

    def getImageArray(self) -> list[Image]:
        return self.imageArray
    

    def setImageArray(self, imageArray: list[Image]) -> None:
        self.imageArray = imageArray
        self.totalFrames = len(imageArray)
        self.circularIndexUtil = CircularIndexUtil.createInstance(self.totalFrames)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.drawImage(self.imageArray[self.circularIndexUtil.getIndex()], x, y, self.anchor)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


