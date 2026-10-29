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


class VectorAnimationInterfaceFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.currentPoints: list[list[list[int]]] = None
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, currentPoints: list[list[list[int]]], basicColor: BasicColor, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        self.currentPoints = currentPoints
        self.setBasicColorP(basicColor)
        self.animationBehaviorFactory = animationBehaviorFactory
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.VectorAnimation import VectorAnimation
        return VectorAnimation(self.currentPoints, self.getBasicColorP(), self.animationBehaviorFactory.getOrCreateInstance())
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.media.ScaleProperties import ScaleProperties


