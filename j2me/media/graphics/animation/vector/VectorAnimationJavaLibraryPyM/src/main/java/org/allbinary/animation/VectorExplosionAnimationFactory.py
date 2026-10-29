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

from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface


class VectorExplosionAnimationFactory(ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.vectorExplosionGenerator: VectorExplosionGenerator = VectorExplosionGenerator.getInstance()
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        self.animationBehaviorFactory: AnimationBehaviorFactory = None
    

    def __init__(self, basicColor: BasicColor, animationBehaviorFactory: AnimationBehaviorFactory) -> None:
        self._init_fields()
        self.animationBehaviorFactory = animationBehaviorFactory
        self.setBasicColorP(basicColor)
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        from org.allbinary.animation.VectorRotationAnimation import VectorRotationAnimation
        vectorRotationAnimationInterface: VectorAnimationInterface = animationInterface
        frame: int = vectorRotationAnimationInterface.getFrame()
        framePoints: list[list[int]] = vectorRotationAnimationInterface.getPoints(frame)
        points: list[list[list[int]]] = self.vectorExplosionGenerator.getInstance(framePoints, 6, self.vectorExplosionGenerator.ROTATION)
        return VectorRotationAnimation(points, self.getBasicColorP(), self.animationBehaviorFactory.getOrCreateInstance())
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.animation.VectorExplosionGenerator import VectorExplosionGenerator


