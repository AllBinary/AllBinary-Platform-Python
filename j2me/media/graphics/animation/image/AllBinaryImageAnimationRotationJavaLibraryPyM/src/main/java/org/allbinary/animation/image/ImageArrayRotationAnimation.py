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
from org.allbinary.animation.image.ImageArrayBaseRotationAnimation import ImageArrayBaseRotationAnimation


@java_inherited_overloads
class ImageArrayRotationAnimation(ImageArrayBaseRotationAnimation):
    def _java_defaults(self):
        vars(self).setdefault("expectedTotalFrames", 0)

    def _init_fields(self) -> None:
        if "expectedTotalFrames" not in vars(self): self.expectedTotalFrames: int = 0
    

    # throws Exception
    @staticmethod
    def createAnimation(anyType: object, animationBehavior: AnimationBehavior) -> ImageArrayRotationAnimation:
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        imageRotationAnimationInfo: ImageArrayRotationAnimationInfo = anyType
        return ImageArrayRotationAnimation(imageRotationAnimationInfo.getImageArray(), imageRotationAnimationInfo.getAngleInfoP(), imageRotationAnimationInfo.getTotalAngle(), animationBehavior)
    

    def __init__(self, imageArray: list[Image], angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        super().__init__(imageArray, angleInfo, animationBehavior)
        __class__._init_fields(self)
        self.initImageArray(imageArray, angleInfo, totalAngle)
    

    # throws Exception
    def initImageArray(self, imageArray: list[Image], angleInfo: AngleInfo, totalAngle: int) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.math.AngleInfo import AngleInfo
        self.expectedTotalFrames = java_divide(totalAngle, self.angleInfo.getAngleIncrementInfo().getAngleIncrement())
            
        self.angleInfo.adjustAngle(0)
        if self.expectedTotalFrames != self.getSize():
            raise Exception("Wrong Number of Frames")
    

    def setImageArray(self, imageArray: list[Image]) -> None:
        from javax.microedition.lcdui.Image import Image
        java_super_call(super(), "setImageArray", imageArray)
        self.angleInfo.adjustAngle(0)
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.math.AngleInfo import AngleInfo


