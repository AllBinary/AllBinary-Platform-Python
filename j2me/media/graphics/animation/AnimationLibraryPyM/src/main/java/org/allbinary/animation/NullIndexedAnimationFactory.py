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


class NullIndexedAnimationFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):
    NULL_INDEXED_ANIMATION_ARRAY: list[IndexedAnimation] = [None] * (0)
    NULL_INDEXED_ANIMATION_FACTORY: NullIndexedAnimationFactory = None
    class NullIndexedAnimationInner(NullIndexedAnimation):
        

        def __init__(self) -> None:
            from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
            super().__init__(IndexedAnimationBehavior(1, 250))
        

        def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
            pass

    def _init_fields(self) -> None:
        self.NULL_ANIMATION: Animation = NullIndexedAnimationInner()
    

    def __init__(self) -> None:
        self._init_fields()
    

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
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.animation.NullIndexedAnimationInner import NullIndexedAnimationInner


NullIndexedAnimationFactory.NULL_INDEXED_ANIMATION_FACTORY = NullIndexedAnimationFactory()

