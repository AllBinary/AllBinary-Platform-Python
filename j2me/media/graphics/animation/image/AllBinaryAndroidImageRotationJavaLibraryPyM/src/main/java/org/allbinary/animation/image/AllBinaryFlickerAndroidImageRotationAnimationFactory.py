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

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class AllBinaryFlickerAndroidImageRotationAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        self.image: Image = NullImage.NULL_IMAGE
        self.angleIncrement: int = None
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, image: Image, width: int, height: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        self._init_fields()
        self.setImage(image)
        self.angleIncrement = angleIncrement
        self.animationBehaviorFactory = animationBehaviorFactory
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.AllBinaryFlickerAndroidImageRotationAnimation import AllBinaryFlickerAndroidImageRotationAnimation
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
        from org.allbinary.math.AngleFactory import AngleFactory
        from org.allbinary.math.AngleInfo import AngleInfo
        image: Image = ImageCopyUtil.getInstance().createImage(self.getImage())
        return AllBinaryFlickerAndroidImageRotationAnimation(self.getImage(), image, AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationBehaviorFactory.getOrCreateInstance())
    

    def getAngleIncrement(self) -> int:
        return self.angleIncrement
    

    def setImage(self, image: Image) -> None:
        from javax.microedition.lcdui.Image import Image
        self.image = image
    

    def getImage(self) -> Image:
        from javax.microedition.lcdui.Image import Image
        return self.image
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        from org.allbinary.media.ScaleProperties import ScaleProperties
        pass
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.media.image.ImageCopyUtil import ImageCopyUtil
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.media.ScaleProperties import ScaleProperties


