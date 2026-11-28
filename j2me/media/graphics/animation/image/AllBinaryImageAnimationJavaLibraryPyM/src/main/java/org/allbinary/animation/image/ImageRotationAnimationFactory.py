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
from org.allbinary.animation.image.BaseImageAnimationFactory import BaseImageAnimationFactory


@java_inherited_overloads
class ImageRotationAnimationFactory(BaseImageAnimationFactory):
    def _java_defaults(self):
        vars(self).setdefault("angleIncrement", 0)

    def _init_fields(self) -> None:
        if "angleIncrement" not in vars(self): self.angleIncrement: int = 0
    

    def __init__(self, image: Image, width: int, height: int, dx: int, dy: int, angleIncrement: int, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        super().__init__(image, PrimitiveIntUtil.getArrayInstance(), width, height, 0, 0, animationBehaviorFactory)
        __class__._init_fields(self)
        self.angleIncrement = angleIncrement
        self.animationFactoryInitializationVisitor.dx = dx
        self.animationFactoryInitializationVisitor.dy = dy
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.image.ImageBaseRotationAnimation import ImageBaseRotationAnimation
        from org.allbinary.animation.image.AdjustedImageBaseRotationAnimation import AdjustedImageBaseRotationAnimation
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.math.AngleFactory import AngleFactory
        from org.allbinary.math.AngleInfo import AngleInfo
        if self.animationFactoryInitializationVisitor.dx != 0 or self.animationFactoryInitializationVisitor.dy != 0:
            self.animationFactoryImageScaleUtil.processAdjust(self)
            return AdjustedImageBaseRotationAnimation(self.getImage(), AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationFactoryInitializationVisitor.dx, self.animationFactoryInitializationVisitor.dy, self.animationBehaviorFactory.getOrCreateInstance())
        else:
            return ImageBaseRotationAnimation(self.getImage(), AngleInfo.getInstance(self.angleIncrement), AngleFactory.getInstance().TOTAL_ANGLE, self.animationBehaviorFactory.getOrCreateInstance())
    

    def getAngleIncrementP(self) -> int:
        return self.angleIncrement
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
# from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.math.AngleInfo import AngleInfo


