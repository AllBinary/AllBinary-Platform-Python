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


class IndependentVectorExplosionRotationAnimationFactory(ProceduralAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.framePoints: list[list[list[int]]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY_ARRAY
        self.vectorInfo: VectorInfo = None
        self.basicColor: BasicColor = None
        self.vectorAnimationFactoryInterface: VectorAnimationFactoryInterface = None
        self.vectorExplosionGenerator: VectorExplosionGenerator = VectorExplosionGenerator.getInstance()
    

    def __init__(self, vectorInfo: VectorInfo, basicColor: BasicColor, vectorAnimationFactoryInterface: VectorAnimationFactoryInterface) -> None:
        self._init_fields()
        self.vectorInfo = vectorInfo
        self.basicColor = basicColor
        self.vectorAnimationFactoryInterface = vectorAnimationFactoryInterface
        self.init()
    

    # throws Exception
    def init(self) -> None:
        from org.allbinary.animation.VectorRotationGenerator import VectorRotationGenerator
        self.framePoints = VectorRotationGenerator.getInstance().getInstance(self.vectorInfo)
    

    # throws Exception
    def getInstanceAnimation(self, animationInterface: Animation) -> Animation:
        frame: int = 0
        if animationInterface is not None:
            rotationAnimationInterface: IndexedAnimation = animationInterface
            frame = rotationAnimationInterface.getFrame()
        points: list[list[list[int]]] = self.vectorExplosionGenerator.getInstance(self.framePoints[frame], 6, self.vectorExplosionGenerator.ROTATION)
        return self.vectorAnimationFactoryInterface.getInstance(points, self.basicColor)
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.vector.VectorInfo import VectorInfo
from org.allbinary.animation.VectorExplosionGenerator import VectorExplosionGenerator


