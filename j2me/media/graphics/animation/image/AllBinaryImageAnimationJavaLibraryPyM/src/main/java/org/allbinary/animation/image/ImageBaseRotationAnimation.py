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

from org.allbinary.animation.RotationAnimation import RotationAnimation


class ImageBaseRotationAnimation(RotationAnimation):

    def _init_fields(self) -> None:
        self.image: Image = None
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(angleInfo, CircularIndexUtil.createInstance(totalAngle / angleInfo.getAngleIncrementInfo().getAngleIncrement()), animationBehavior)
        self._init_fields()
        self.image = image
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.drawImage(self.image, x, y, self.anchor)
    

    def getImage(self) -> Image:
        return self.image
    

    def getWidth(self) -> int:
        return self.image.getWidth()
    

    def getHeight(self) -> int:
        return self.image.getHeight()
    

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
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


