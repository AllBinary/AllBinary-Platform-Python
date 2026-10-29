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
# package org.allbinary.animation.compound

from __future__ import annotations

from org.allbinary.animation.compound.CompoundAnimationInterfaceFactory import CompoundAnimationInterfaceFactory


class CompoundRotationAnimationInterfaceFactory(CompoundAnimationInterfaceFactory):
    

    def __init__(self, basicAnimationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface], animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(basicAnimationInterfaceFactoryInterfaceArray, animationBehaviorFactory)
        if animationBehaviorFactory == AnimationBehaviorFactory.getInstance():
            ForcedLogUtil.log("Using default AnimationBehaviorFactory with IndexedAnimationFactory", self)
    

    def createArray(self, size: int) -> list[Animation]:
        return [None] * (size)
    

    def createAnimation(self, animationInterfaceArray: list[Animation]) -> Animation:
        from org.allbinary.animation.compound.CompoundRotationAnimation import CompoundRotationAnimation
        return CompoundRotationAnimation(animationInterfaceArray, self.animationBehaviorFactory.getOrCreateInstance())
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.RotationAnimation import RotationAnimation
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil


