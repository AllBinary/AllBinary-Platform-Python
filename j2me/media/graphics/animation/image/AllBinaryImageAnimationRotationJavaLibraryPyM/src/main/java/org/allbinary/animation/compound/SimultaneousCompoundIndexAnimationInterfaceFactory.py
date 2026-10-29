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

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class SimultaneousCompoundIndexAnimationInterfaceFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.basicAnimationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface] = None
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, basicAnimationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface], animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        self.basicAnimationInterfaceFactoryInterfaceArray = basicAnimationInterfaceFactoryInterfaceArray
        self.animationBehaviorFactory = animationBehaviorFactory
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        size: int = len(self.basicAnimationInterfaceFactoryInterfaceArray)
        animationInterfaceArray: list[IndexedAnimation] = [None] * (size)
        for index in range(0, size):
            animationInterfaceArray[index] = self.basicAnimationInterfaceFactoryInterfaceArray[index].getInstance(instanceId)
        return self.getOrCreate(animationInterfaceArray)
    

    def getOrCreate(self, animationInterfaceArray: list[IndexedAnimation]) -> Animation:
        from org.allbinary.animation.compound.SimultaneousCompoundIndexAnimation import SimultaneousCompoundIndexAnimation
        return SimultaneousCompoundIndexAnimation(animationInterfaceArray, self.animationBehaviorFactory.getOrCreateInstance())
    

    def getBasicAnimationInterfaceFactoryInterfaceArray(self) -> list[AnimationInterfaceFactoryInterface]:
        return self.basicAnimationInterfaceFactoryInterfaceArray
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.media.ScaleProperties import ScaleProperties


