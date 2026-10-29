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

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface


class RotationAnimationFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.totalAngle: int = None
        self.angleIncrement: int = None
    

    @staticmethod
    def createFactory() -> RotationAnimationFactory:
        totalAngle: int = AngleFactory.getInstance().TOTAL_ANGLE
        return RotationAnimationFactory(totalAngle, ((int((totalAngle / GameConfigurationCentral.getInstance().getGameControlFidelity())) + 32768) % 65536 - 32768))
    

    def __init__(self, totalAngle: int, angleIncrement: int) -> None:
        self._init_fields()
        self.totalAngle = totalAngle
        self.angleIncrement = angleIncrement
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.NullRotationAnimation import NullRotationAnimation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        return NullRotationAnimation.createTotalAngle(AngleInfo.getInstance(self.angleIncrement), self.totalAngle, AnimationBehavior.getInstance())
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        from org.allbinary.animation.NullRotationAnimation import NullRotationAnimation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        return NullRotationAnimation.createTotalAngle(AngleInfo.getInstance(self.angleIncrement), self.totalAngle, AnimationBehavior.getInstance())
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.ScaleProperties import ScaleProperties


