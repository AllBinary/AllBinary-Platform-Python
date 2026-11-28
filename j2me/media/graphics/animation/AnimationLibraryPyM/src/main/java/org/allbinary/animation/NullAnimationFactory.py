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


class NullAnimationFactory(*java_bases(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface)):
    NULL_NOT_FOR_USE_ANIMATION_FACTORY: NullAnimationFactory = None
    NULL_ANIMATION_FACTORY: NullAnimationFactory = None

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        _java_listener_owner = self
        class _JavaListenerN65758(Animation):
                


            def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
                from javax.microedition.lcdui.Graphics import Graphics
                pass
        self.NULL_ANIMATION: Animation = _JavaListenerN65758()
            
        self.EMPTY_ARRAY: list[Animation] = [None] * (0)
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getFactoryInstance() -> NullAnimationFactory:
        return NullAnimationFactory.NULL_ANIMATION_FACTORY
    

    def getInstance(self, instanceId: int) -> Animation:
        return self.NULL_ANIMATION
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.NULL_ANIMATION
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        from org.allbinary.media.ScaleProperties import ScaleProperties
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.animation.Animation import Animation


def _NullAnimationFactory_NULL_NOT_FOR_USE_ANIMATION_FACTORY() -> object:
    return NullAnimationFactory()

lazy_static(NullAnimationFactory, "NULL_NOT_FOR_USE_ANIMATION_FACTORY", _NullAnimationFactory_NULL_NOT_FOR_USE_ANIMATION_FACTORY)

def _NullAnimationFactory_NULL_ANIMATION_FACTORY() -> object:
    return NullAnimationFactory()

lazy_static(NullAnimationFactory, "NULL_ANIMATION_FACTORY", _NullAnimationFactory_NULL_ANIMATION_FACTORY)

