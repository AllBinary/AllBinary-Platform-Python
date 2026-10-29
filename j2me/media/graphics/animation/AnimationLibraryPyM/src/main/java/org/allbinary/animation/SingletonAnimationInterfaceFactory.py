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


class SingletonAnimationInterfaceFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.animationInterface: Animation = None
    

    def __init__(self, animationInterface: Animation) -> None:
        self._init_fields()
        self.animationInterface = animationInterface
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        return self.animationInterface
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.animationInterface
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.media.ScaleProperties import ScaleProperties


