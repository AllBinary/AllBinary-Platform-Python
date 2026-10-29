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

from org.allbinary.animation.image.ImageArrayRotationAnimation import ImageArrayRotationAnimation


#TWB - Adjustments should be done in the resource creation and not at the animation level
class AdjustedImageArrayRotationAnimation(ImageArrayRotationAnimation):

    def _init_fields(self) -> None:
        self.dx: int = 0
        self.dy: int = 0
    

    # throws Exception
    @staticmethod
    def createAdjustedImageArrayRotationAnimationInfo(anyType: object, animationBehavior: AnimationBehavior) -> AdjustedImageArrayRotationAnimation:
        imageRotationAnimationInfo: ImageArrayRotationAnimationInfo = anyType
        return AdjustedImageArrayRotationAnimation(imageRotationAnimationInfo.getImageArray(), imageRotationAnimationInfo.getAngleInfoP(), imageRotationAnimationInfo.getTotalAngle(), imageRotationAnimationInfo.getDx(), imageRotationAnimationInfo.getDy(), animationBehavior)
    

    # throws Exception
    @staticmethod
    def createAnimation(imageArray: list[Image], angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> AdjustedImageArrayRotationAnimation:
        return AdjustedImageArrayRotationAnimation(imageArray, angleInfo, totalAngle, -(imageArray[0].getWidth() >> 2), -(imageArray[0].getHeight() >> 2), animationBehavior)
    

    def __init__(self, imageArray: list[Image], angleInfo: AngleInfo, totalAngle: int, dx: int, dy: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(imageArray, angleInfo, totalAngle, animationBehavior)
        self._init_fields()
        self.init(dx, dy)
    

    # throws Exception
    def init(self, dx: int, dy: int) -> None:
        self.setDx(dx)
        self.setDy(dy)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        super().paintXY(graphics, x + self.dx, y + self.dy)
    

    def setDx(self, dx: int) -> None:
        self.dx = dx
    

    def getDx(self) -> int:
        return self.dx
    

    def setDy(self, dy: int) -> None:
        self.dy = dy
    

    def getDy(self) -> int:
        return self.dy
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.math.AngleInfo import AngleInfo


