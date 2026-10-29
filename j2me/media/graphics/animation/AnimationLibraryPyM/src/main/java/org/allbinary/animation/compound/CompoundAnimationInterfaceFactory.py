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


class CompoundAnimationInterfaceFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.basicAnimationInterfaceFactoryInterfaceArrayP: list[AnimationInterfaceFactoryInterface] = None
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, basicAnimationInterfaceFactoryInterfaceArray: list[AnimationInterfaceFactoryInterface], animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        self.basicAnimationInterfaceFactoryInterfaceArrayP = basicAnimationInterfaceFactoryInterfaceArray
        self.animationBehaviorFactory = animationBehaviorFactory
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        size: int = len(self.basicAnimationInterfaceFactoryInterfaceArrayP)
        animationInterfaceArray: list[Animation] = self.createArray(size)
        for index in range(0, size):
            animationInterfaceArray[index] = self.basicAnimationInterfaceFactoryInterfaceArrayP[index].getInstance(instanceId)
        return self.createAnimation(animationInterfaceArray)
    

    def createArray(self, size: int) -> list[Animation]:
        return NullAnimationFactory.getFactoryInstance().EMPTY_ARRAY
    

    def createAnimation(self, animationInterfaceArray: list[Animation]) -> Animation:
        return NullAnimationFactory.getFactoryInstance().getInstance(0)
    

    def getBasicAnimationInterfaceFactoryInterfaceArray(self) -> list[AnimationInterfaceFactoryInterface]:
        return self.basicAnimationInterfaceFactoryInterfaceArrayP
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        size: int = len(self.basicAnimationInterfaceFactoryInterfaceArrayP)
        for index in range(0, size):
            self.basicAnimationInterfaceFactoryInterfaceArrayP[index].setInitialScale(scaleProperties)
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehaviorFactory import AnimationBehaviorFactory
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.media.ScaleProperties import ScaleProperties


