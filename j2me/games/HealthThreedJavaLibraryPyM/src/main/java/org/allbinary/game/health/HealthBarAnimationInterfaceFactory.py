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
# package org.allbinary.game.health

from __future__ import annotations

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface


class HealthBarAnimationInterfaceFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getInstanceByLocation(self, layerInterface: AllBinaryLayer, location: int) -> HealthBarAnimation:
        from org.allbinary.game.health.HealthBarThreedAnimation import HealthBarThreedAnimation
        return HealthBarThreedAnimation(layerInterface, location)
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        return None
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return None
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.animation.Animation import Animation
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.ScaleProperties import ScaleProperties


