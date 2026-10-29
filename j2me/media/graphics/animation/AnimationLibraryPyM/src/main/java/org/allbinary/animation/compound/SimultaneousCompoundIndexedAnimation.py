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

from org.allbinary.animation.IndexedAnimation import IndexedAnimation


class SimultaneousCompoundIndexedAnimation(IndexedAnimation):

    def _init_fields(self) -> None:
        self.animationInterfaceArray: list[Animation] = None
    

    def __init__(self, animationInterfaceArray: list[Animation], animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.animationInterfaceArray = animationInterfaceArray
    

    def setFrame(self, frameIndex: int) -> None:
        indexedAnimation: IndexedAnimation = None
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            indexedAnimation = self.animationInterfaceArray[index]
            indexedAnimation.setFrame(frameIndex)
    

    def getFrame(self) -> int:
        indexedAnimation: IndexedAnimation = self.animationInterfaceArray[0]
        return indexedAnimation.getFrame()
    

    def getSize(self) -> int:
        indexedAnimation: IndexedAnimation = self.animationInterfaceArray[0]
        return indexedAnimation.getSize()
    

    def previousFrame(self) -> None:
        indexedAnimation: IndexedAnimation = None
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            indexedAnimation = self.animationInterfaceArray[index]
            indexedAnimation.previousFrame()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    # throws Exception
    def nextFrame(self) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].nextFrame()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        size: int = len(self.animationInterfaceArray)
        for index in range(0, size):
            self.animationInterfaceArray[index].paintXY(graphics, x, y)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        size: int = len(self.animationInterfaceArray)
        for index in range(0, size):
            self.animationInterfaceArray[index].paintThreedXYZ(graphics, x, y, z)
    

    def getAnimationInterfaceArray(self) -> list[Animation]:
        return self.animationInterfaceArray
    

    def setAnimationInterfaceArray(self, animationInterfaceArray: list[Animation]) -> None:
        self.animationInterfaceArray = animationInterfaceArray
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


