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
from org.allbinary.animation.IndexedAnimation import IndexedAnimation


@java_inherited_overloads
class TweenedImageAnimation(IndexedAnimation):
    def _java_defaults(self):
        vars(self).setdefault("image", None)
        vars(self).setdefault("dx", 0)
        vars(self).setdefault("dy", 0)
        vars(self).setdefault("totalFrames", 0)
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        if "image" not in vars(self): self.image: Image = None
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
        if "totalFrames" not in vars(self): self.totalFrames: int = 0
        if "circularIndexUtil" not in vars(self): self.circularIndexUtil: CircularIndexUtil = None
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, dx: int, dy: int, totalFrames: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(animationBehavior)
        __class__._init_fields(self)
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
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        frame: int = self.getFrame()
        currentX: int = self.dx * frame
        currentY: int = self.dy * frame
        graphics.drawImage(self.image, x + currentX, y + currentY, self.anchor)
    

    # throws Exception
    def close(self) -> None:
        from org.allbinary.DisposalUtil import DisposalUtil
        DisposalUtil.getInstance().disposeImage(self.image)
    

    # throws Throwable
    def finalize(self) -> None:
        from org.allbinary.DisposalUtil import DisposalUtil
        DisposalUtil.getInstance().disposeImage(self.image)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.DisposalUtil import DisposalUtil
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


