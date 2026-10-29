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


class NullAnimationFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):
    NULL_NOT_FOR_USE_ANIMATION_FACTORY: NullAnimationFactory = None
    NULL_ANIMATION_FACTORY: NullAnimationFactory = None

    def _init_fields(self) -> None:
        self.NULL_ANIMATION: Animation = (Animation()  # Java anonymous class body:
#         
# 
#         def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
#             pass
)
        self.EMPTY_ARRAY: list[Animation] = [None] * (0)
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getFactoryInstance() -> NullAnimationFactory:
        return NullAnimationFactory.NULL_ANIMATION_FACTORY
    

    def getInstance(self, instanceId: int) -> Animation:
        return self.NULL_ANIMATION
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return self.NULL_ANIMATION
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.animation.Animation import Animation


NullAnimationFactory.NULL_NOT_FOR_USE_ANIMATION_FACTORY = NullAnimationFactory()

NullAnimationFactory.NULL_ANIMATION_FACTORY = NullAnimationFactory()

