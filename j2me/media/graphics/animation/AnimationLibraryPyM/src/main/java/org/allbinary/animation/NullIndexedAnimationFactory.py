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


class NullIndexedAnimationFactory(*java_bases(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface)):
    NULL_INDEXED_ANIMATION_ARRAY: list[IndexedAnimation] = [None] * (0)
    NULL_INDEXED_ANIMATION_FACTORY: NullIndexedAnimationFactory = None

    def _init_fields(self) -> None:
        self.NULL_ANIMATION: Animation = NullIndexedAnimationInner()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getFactoryInstance() -> NullIndexedAnimationFactory:
        return NullIndexedAnimationFactory.NULL_INDEXED_ANIMATION_FACTORY
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        return self.NULL_ANIMATION
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.NULL_ANIMATION
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        from org.allbinary.media.ScaleProperties import ScaleProperties
        pass
# from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.animation.NullIndexedAnimationInner import NullIndexedAnimationInner


def _NullIndexedAnimationFactory_NULL_INDEXED_ANIMATION_FACTORY() -> object:
    return NullIndexedAnimationFactory()

lazy_static(NullIndexedAnimationFactory, "NULL_INDEXED_ANIMATION_FACTORY", _NullIndexedAnimationFactory_NULL_INDEXED_ANIMATION_FACTORY)

