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


class CompoundIndexedAnimationInterfaceFactory(CompoundAnimationInterfaceFactory):
    

    def __init__(self, basicAnimationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface], animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        super().__init__(basicAnimationInterfaceFactoryInterfaceArray, animationBehaviorFactory)
    

    def createArray(self, size: int) -> list[Animation]:
        return [None] * (size)
    

    def createAnimation(self, animationArray: list[Animation]) -> Animation:
        from org.allbinary.animation.compound.CompoundIndexedAnimation import CompoundIndexedAnimation
        return CompoundIndexedAnimation(animationArray, self.animationBehaviorFactory.getOrCreateInstance())
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil


