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


class NullRotationAnimationFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):
    NULL_ROTATION_ANIMATION_FACTORY: NullRotationAnimationFactory = None
    class NullRotationAnimation2(NullRotationAnimation):
        

        def __init__(self) -> None:
            from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
            super().__init__(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), IndexedAnimationBehavior(1, 250))
        

        def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
            pass

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
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.ScaleProperties import ScaleProperties
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.animation.NullRotationAnimation2 import NullRotationAnimation2


NullRotationAnimationFactory.NULL_ROTATION_ANIMATION_FACTORY = NullRotationAnimationFactory()

