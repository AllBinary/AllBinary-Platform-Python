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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.image.ImageAnimation import ImageAnimation


@java_inherited_overloads
class ImageSegmentAnimation(ImageAnimation):
    def _java_defaults(self):
        vars(self).setdefault("startX", 0)
        vars(self).setdefault("startY", 0)
        vars(self).setdefault("drawWidth", 0)
        vars(self).setdefault("drawHeight", 0)
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("sequenceArray", None)

    def _init_fields(self) -> None:
        if "startX" not in vars(self): self.startX: int = 0
        if "startY" not in vars(self): self.startY: int = 0
        if "drawWidth" not in vars(self): self.drawWidth: int = 0
        if "drawHeight" not in vars(self): self.drawHeight: int = 0
        if "circularIndexUtil" not in vars(self): self.circularIndexUtil: CircularIndexUtil = None
        if "sequenceArray" not in vars(self): self.sequenceArray: list[int] = None
    

    def __init__(self, image: Image, sequenceArray: list[int], animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(image, animationBehavior)
        __class__._init_fields(self)
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
        from javax.microedition.lcdui.Graphics import Graphics
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
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


