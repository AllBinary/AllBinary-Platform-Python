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
from org.allbinary.animation.compound.CompoundAnimationInterface import CompoundAnimationInterface


class CompoundIndexedAnimation(IndexedAnimation, CompoundAnimationInterface):

    def _init_fields(self) -> None:
        self.circularIndexUtil: CircularIndexUtil = None
        self.animationInterfaceArray: list[Animation] = None
    

    def __init__(self, animationInterfaceArray: list[Animation], animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.animationInterfaceArray = animationInterfaceArray
        self.circularIndexUtil = CircularIndexUtil.createInstance(len(self.animationInterfaceArray))
    

    def setFrame(self, index: int) -> None:
        indexedAnimation: IndexedAnimation = self.animationInterfaceArray[self.circularIndexUtil.getIndex()]
        indexedAnimation.setFrame(index)
    

    def getFrame(self) -> int:
        indexedAnimation: IndexedAnimation = self.animationInterfaceArray[self.circularIndexUtil.getIndex()]
        return indexedAnimation.getFrame()
    

    def getSize(self) -> int:
        indexedAnimation: IndexedAnimation = self.animationInterfaceArray[self.circularIndexUtil.getIndex()]
        return indexedAnimation.getSize()
    

    def previousFrame(self) -> None:
        indexedAnimation: IndexedAnimation = self.animationInterfaceArray[self.circularIndexUtil.getIndex()]
        indexedAnimation.previousFrame()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    # throws Exception
    def nextFrame(self) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].nextFrame()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].paintXY(graphics, x, y)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].paintThreedXYZ(graphics, x, y, z)
    

    def getCurrentAnimation(self) -> IndexedAnimation:
        return self.animationInterfaceArray[self.circularIndexUtil.getIndex()]
    

    def nextAnimation(self) -> None:
        frame: int = self.getFrame()
        self.circularIndexUtil.next()
        self.setFrame(frame)
    

    def previousAnimation(self) -> None:
        frame: int = self.getFrame()
        self.circularIndexUtil.previous()
        self.setFrame(frame)
    

    def setAnimation(self, index: int) -> None:
        frame: int = self.getFrame()
        self.circularIndexUtil.setIndex(index)
        self.setFrame(frame)
    

    def getAnimationInterfaceArray(self) -> list[Animation]:
        return self.animationInterfaceArray
    

    def setAnimationInterfaceArray(self, animationInterfaceArray: list[Animation]) -> None:
        self.animationInterfaceArray = animationInterfaceArray
    

    # throws Exception
    def set(self, gl: GL) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].set(gl)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


