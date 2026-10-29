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
# package org.allbinary.animation.special

from __future__ import annotations

from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
from org.allbinary.animation.special.SpecialAnimationInterface import SpecialAnimationInterface


class SpecialAnimation(IndexedAnimation, SpecialAnimationInterface):
    NULL_SPECIAL_ANIMATION: SpecialAnimation = None
    

    @staticmethod
    def getInstance() -> SpecialAnimation:
        return SpecialAnimation.NULL_SPECIAL_ANIMATION
    

    def __init__(self, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
    

    def nextFrame(self) -> None:
        indexedAnimationBehavior: IndexedAnimationBehavior = (self.animationBehaviorP)
        indexedAnimationBehavior.loopIndex += 1
    

    def setLastFrame(self) -> None:
        pass
    

    def isComplete(self) -> bool:
        return False
    

    def open(self) -> None:
        pass
    

    def close(self) -> None:
        pass
    

    def process(self) -> None:
        pass
from org.allbinary.animation.AnimationBehavior import AnimationBehavior


SpecialAnimation.NULL_SPECIAL_ANIMATION = SpecialAnimation(IndexedAnimationBehavior(1, 250))

