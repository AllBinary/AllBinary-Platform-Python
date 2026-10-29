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

import time
from org.allbinary.animation.special.SpecialAnimation import SpecialAnimation


class TitleAnimation(SpecialAnimation):

    def _init_fields(self) -> None:
        self.systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
        self.deltaX: float = 0.0
        self.deltaY: float = 0.0
        self.deltaZ: float = 0.0
        self.basicColorArray: list[BasicColor] = None
        self.dxArray: list[int] = None
        self.dyArray: list[int] = None
        self.widthP: int = None
        self.animationInterfaceArray: list[IndexedAnimation] = None
        self.sizeP: int = None
        self.y: int = None
        self.lastFrameStartTime: int = None
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.CLEAR_COLOR: BasicColor = BasicColorFactory.getInstance().CLEAR_COLOR
    

    @staticmethod
    def createAnimation(animationInterfaceArray: list[IndexedAnimation], basicColorArray: list[BasicColor], dxArray: list[int], dyArray: list[int], y: int, width: int) -> TitleAnimation:
        return TitleAnimation(animationInterfaceArray, basicColorArray, dxArray, dyArray, y, width, IndexedAnimationBehavior(1, 250))
    

    def __init__(self, animationInterfaceArray: list[IndexedAnimation], basicColorArray: list[BasicColor], dxArray: list[int], dyArray: list[int], y: int, width: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.lastFrameStartTime = self.systemWrapper.currentTimeMillis()
        self.animationInterfaceArray = animationInterfaceArray
        self.sizeP = len(self.animationInterfaceArray)
        self.basicColorArray = basicColorArray
        self.dxArray = dxArray
        self.dyArray = dyArray
        self.y = y
        self.widthP = width
        self.reset()
    

    def nextFrame(self) -> None:
        currentTime: int = self.systemWrapper.currentTimeMillis()
        totalTimeElapsed: int = currentTime - self.lastFrameStartTime
        indexedAnimationBehavior: IndexedAnimationBehavior = self.getAnimationBehavior()
        if totalTimeElapsed > indexedAnimationBehavior.frameDelayTime:
            self.previousFrame()
            self.lastFrameStartTime = currentTime
        if self.animationInterfaceArray[0].getFrame() == 0:
            indexedAnimationBehavior.loopIndex += 1
    

    def isComplete(self) -> bool:
        indexedAnimationBehavior: IndexedAnimationBehavior = self.getAnimationBehavior()
        if indexedAnimationBehavior.loopTotal == -1 or indexedAnimationBehavior.loopIndex < indexedAnimationBehavior.loopTotal or self.getFrame() != 0:
            return False
        else:
            return True
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def getSize(self) -> int:
        return self.animationInterfaceArray[0].getSize()
    

    def getFrame(self) -> int:
        return self.animationInterfaceArray[0].getFrame()
    

    def setFrame(self, frame: int) -> None:
        for index in range(0, self.sizeP):
            self.animationInterfaceArray[index].setFrame(frame)
    

    def setLastFrame(self) -> None:
        self.setFrame(self.getSize() - 1)
    

    def reset(self) -> None:
        self.setLastFrame()
        indexedAnimationBehavior: IndexedAnimationBehavior = (self.getAnimationBehavior())
        indexedAnimationBehavior.reset()
    

    def previousFrame(self) -> None:
        for index in range(0, self.sizeP):
            self.animationInterfaceArray[index].previousFrame()
    

    def paintFrameXY(self, graphics: Graphics, frame: int, x: int, y: int) -> None:
        self.setFrame(frame)
        self.paintXY(graphics, x, y)
    

    def paintXY(self, graphics: Graphics, ax: int, ay: int) -> None:
        x: int = 0
        if self.widthP != -2147483648:
            x = ((self.displayInfoSingleton.getLastWidth() - self.widthP) / 2)
        deltaX: int = 0
        deltaY: int = 0
        for index in range(0, self.sizeP):
            deltaX = self.dxArray[index] + x
            deltaY = self.dyArray[index] + self.y
            if self.basicColorArray[index] != self.CLEAR_COLOR:
                self.basicSetColorUtil.setBasicColorP(graphics, self.basicColorArray[index])
            self.animationInterfaceArray[index].paintXY(graphics, deltaX, deltaY)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


