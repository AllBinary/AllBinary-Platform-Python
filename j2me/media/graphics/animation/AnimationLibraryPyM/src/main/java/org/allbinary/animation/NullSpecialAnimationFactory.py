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


class NullSpecialAnimationFactory(AnimationInterfaceFactoryInterface, ProceduralAnimationInterfaceFactoryInterface):
    NULL_SPECIAL_ANIMATION_FACTORY: NullSpecialAnimationFactory = None
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getFactoryInstance() -> NullSpecialAnimationFactory:
        return NullSpecialAnimationFactory.NULL_SPECIAL_ANIMATION_FACTORY
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        return SpecialAnimation.getInstance()
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        return SpecialAnimation.getInstance()
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.animation.special.SpecialAnimation import SpecialAnimation
from org.allbinary.media.ScaleProperties import ScaleProperties


NullSpecialAnimationFactory.NULL_SPECIAL_ANIMATION_FACTORY = NullSpecialAnimationFactory()

