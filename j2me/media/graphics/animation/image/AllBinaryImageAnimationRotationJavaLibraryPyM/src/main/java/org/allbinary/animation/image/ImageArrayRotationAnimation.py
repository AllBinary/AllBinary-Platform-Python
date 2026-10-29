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

from org.allbinary.animation.image.ImageArrayBaseRotationAnimation import ImageArrayBaseRotationAnimation


class ImageArrayRotationAnimation(ImageArrayBaseRotationAnimation):

    def _init_fields(self) -> None:
        self.expectedTotalFrames: int = 0
    

    # throws Exception
    @staticmethod
    def createAnimation(anyType: object, animationBehavior: AnimationBehavior) -> ImageArrayRotationAnimation:
        imageRotationAnimationInfo: ImageArrayRotationAnimationInfo = anyType
        return ImageArrayRotationAnimation(imageRotationAnimationInfo.getImageArray(), imageRotationAnimationInfo.getAngleInfoP(), imageRotationAnimationInfo.getTotalAngle(), animationBehavior)
    

    def __init__(self, imageArray: list[Image], angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(imageArray, angleInfo, animationBehavior)
        self._init_fields()
        self.init(imageArray, angleInfo, totalAngle)
    

    # throws Exception
    def init(self, imageArray: list[Image], angleInfo: AngleInfo, totalAngle: int) -> None:
        self.expectedTotalFrames = totalAngle / self.angleInfo.getAngleIncrementInfo().getAngleIncrement()
        self.angleInfo.adjustAngle(0)
        if self.expectedTotalFrames != self.getSize():
            raise Exception("Wrong Number of Frames")
    

    def setImageArray(self, imageArray: list[Image]) -> None:
        super().setImageArray(imageArray)
        self.angleInfo.adjustAngle(0)
# from javax.microedition.lcdui.Image import Image
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.math.AngleInfo import AngleInfo


