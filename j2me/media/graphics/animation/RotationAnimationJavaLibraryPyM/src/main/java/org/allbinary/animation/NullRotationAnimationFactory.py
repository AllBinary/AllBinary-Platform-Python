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

from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface


class NullRotationAnimationFactory(*java_bases(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface)):
    NULL_ROTATION_ANIMATION_FACTORY: NullRotationAnimationFactory = None

    def _init_fields(self) -> None:
        self.NULL_ROTATION_ANIMATION_ARRAY: list[RotationAnimation] = [None] * (0)
        self.NULL_ANIMATION: Animation = NullRotationAnimation2()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getFactoryInstance() -> NullRotationAnimationFactory:
        return NullRotationAnimationFactory.NULL_ROTATION_ANIMATION_FACTORY
    

    def getInstance(self, instanceId: int) -> Animation:
        return self.NULL_ANIMATION
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.NULL_ANIMATION
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        from org.allbinary.media.ScaleProperties import ScaleProperties
        pass
# from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.animation.NullRotationAnimation2 import NullRotationAnimation2


def _NullRotationAnimationFactory_NULL_ROTATION_ANIMATION_FACTORY() -> object:
    return NullRotationAnimationFactory()

lazy_static(NullRotationAnimationFactory, "NULL_ROTATION_ANIMATION_FACTORY", _NullRotationAnimationFactory_NULL_ROTATION_ANIMATION_FACTORY)

