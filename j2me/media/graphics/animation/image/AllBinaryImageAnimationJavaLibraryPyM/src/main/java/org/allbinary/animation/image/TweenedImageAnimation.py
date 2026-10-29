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


class TweenedImageAnimation(IndexedAnimation):

    def _init_fields(self) -> None:
        self.image: Image = None
        self.dx: int = None
        self.dy: int = None
        self.totalFrames: int = None
        self.circularIndexUtil: CircularIndexUtil = None
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, dx: int, dy: int, totalFrames: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.image = image
        self.dx = dx
        self.dy = dy
        self.totalFrames = totalFrames
        self.circularIndexUtil = CircularIndexUtil.createInstance(self.totalFrames)
    

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
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        frame: int = self.getFrame()
        currentX: int = self.dx * frame
        currentY: int = self.dy * frame
        graphics.drawImage(self.image, x + currentX, y + currentY, self.anchor)
    

    # throws Exception
    def close(self) -> None:
        DisposalUtil.getInstance().disposeImage(self.image)
    

    # throws Throwable
    def finalize(self) -> None:
        DisposalUtil.getInstance().disposeImage(self.image)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.DisposalUtil import DisposalUtil
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


