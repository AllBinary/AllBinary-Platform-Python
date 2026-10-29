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

from org.allbinary.animation.image.ImageAnimation import ImageAnimation


class ImageSegmentAnimation(ImageAnimation):

    def _init_fields(self) -> None:
        self.startX: int = None
        self.startY: int = None
        self.drawWidth: int = None
        self.drawHeight: int = None
        self.circularIndexUtil: CircularIndexUtil = None
        self.sequenceArray: list[int] = None
    

    def __init__(self, image: Image, sequenceArray: list[int], animationBehavior: AnimationBehavior) -> None:
        super().__init__(image, animationBehavior)
        self._init_fields()
        self.startX = 0
        self.startY = 0
        self.drawWidth = self.getImage().getWidth()
        self.drawHeight = self.getImage().getHeight()
        self.circularIndexUtil = CircularIndexUtil.createInstance(self.drawHeight)
        self.sequenceArray = sequenceArray
    

    def nextFrame(self) -> None:
        self.circularIndexUtil.next()
    

    def previousFrame(self) -> None:
        self.circularIndexUtil.previous()
    

    def setFrame(self, index: int) -> None:
        self.circularIndexUtil.setIndex(index)
    

    def getFrame(self) -> int:
        return self.circularIndexUtil.getIndex()
    

    def getSize(self) -> int:
        return self.circularIndexUtil.getSize()
    

    def setSequence(self, sequenceArray: list[int]) -> None:
        self.sequenceArray = sequenceArray
    

    def getSequence(self) -> list[int]:
        return self.sequenceArray
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        pass
    

    def getStartX(self) -> int:
        return self.startX
    

    def setStartX(self, startX: int) -> None:
        self.startX = startX
    

    def getStartY(self) -> int:
        return self.startY
    

    def setStartY(self, startY: int) -> None:
        self.startY = startY
    

    def getDrawWidth(self) -> int:
        return self.drawWidth
    

    def setDrawWidth(self, drawWidth: int) -> None:
        self.drawWidth = drawWidth
    

    def getDrawHeight(self) -> int:
        return self.drawHeight
    

    def setDrawHeight(self, drawHeight: int) -> None:
        self.drawHeight = drawHeight
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


