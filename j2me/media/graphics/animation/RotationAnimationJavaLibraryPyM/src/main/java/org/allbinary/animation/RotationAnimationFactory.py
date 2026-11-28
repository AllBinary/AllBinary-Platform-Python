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
# package org.allbinary.animation

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface


class RotationAnimationFactory(*java_bases(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface)):

    def _init_fields(self) -> None:
        if "totalAngle" not in vars(self): self.totalAngle: int = 0
        if "angleIncrement" not in vars(self): self.angleIncrement: int = 0
    

    @staticmethod
    def createFactory() -> RotationAnimationFactory:
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        from org.allbinary.math.AngleFactory import AngleFactory
        totalAngle: int = AngleFactory.getInstance().TOTAL_ANGLE
        return RotationAnimationFactory(totalAngle, ((int((java_divide(totalAngle, GameConfigurationCentral.getInstance().getGameControlFidelity()))) + 32768) % 65536 - 32768))
    

    def __init__(self, totalAngle: int, angleIncrement: int) -> None:
        __class__._init_fields(self)
        self.totalAngle = totalAngle
        self.angleIncrement = angleIncrement
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.NullRotationAnimation import NullRotationAnimation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        return NullRotationAnimation.createTotalAngle(AngleInfo.getInstance(self.angleIncrement), self.totalAngle, AnimationBehavior.getInstance())
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        from org.allbinary.animation.NullRotationAnimation import NullRotationAnimation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        return NullRotationAnimation.createTotalAngle(AngleInfo.getInstance(self.angleIncrement), self.totalAngle, AnimationBehavior.getInstance())
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        from org.allbinary.media.ScaleProperties import ScaleProperties
        pass
# from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.media.ScaleProperties import ScaleProperties


