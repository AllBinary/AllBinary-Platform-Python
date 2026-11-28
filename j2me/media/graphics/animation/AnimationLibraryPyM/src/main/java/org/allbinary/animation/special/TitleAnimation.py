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
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.special.SpecialAnimation import SpecialAnimation


@java_inherited_overloads
class TitleAnimation(SpecialAnimation):
    def _java_defaults(self):
        vars(self).setdefault("systemWrapper", None)
        vars(self).setdefault("deltaX", 0.0)
        vars(self).setdefault("deltaY", 0.0)
        vars(self).setdefault("deltaZ", 0.0)
        vars(self).setdefault("basicColorArray", None)
        vars(self).setdefault("dxArray", None)
        vars(self).setdefault("dyArray", None)
        vars(self).setdefault("widthP", 0)
        vars(self).setdefault("animationInterfaceArray", None)
        vars(self).setdefault("sizeP", 0)
        vars(self).setdefault("y", 0)
        vars(self).setdefault("lastFrameStartTime", 0)
        vars(self).setdefault("displayInfoSingleton", None)
        vars(self).setdefault("CLEAR_COLOR", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
        self.systemWrapper: ABSystemWrapper = ABSystemWrapper.getInstance()
        if "deltaX" not in vars(self): self.deltaX: float = 0.0
        if "deltaY" not in vars(self): self.deltaY: float = 0.0
        if "deltaZ" not in vars(self): self.deltaZ: float = 0.0
        if "basicColorArray" not in vars(self): self.basicColorArray: list[BasicColor] = None
        if "dxArray" not in vars(self): self.dxArray: list[int] = None
        if "dyArray" not in vars(self): self.dyArray: list[int] = None
        if "widthP" not in vars(self): self.widthP: int = 0
        if "animationInterfaceArray" not in vars(self): self.animationInterfaceArray: list[IndexedAnimation] = None
        if "sizeP" not in vars(self): self.sizeP: int = 0
        if "y" not in vars(self): self.y: int = 0
        if "lastFrameStartTime" not in vars(self): self.lastFrameStartTime: int = 0
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.CLEAR_COLOR: BasicColor = BasicColorFactory.getInstance().CLEAR_COLOR
    

    @staticmethod
    def createAnimation(animationInterfaceArray: list[IndexedAnimation], basicColorArray: list[BasicColor], dxArray: list[int], dyArray: list[int], y: int, width: int) -> TitleAnimation:
        from org.allbinary.animation.IndexedAnimation import IndexedAnimation
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return TitleAnimation(animationInterfaceArray, basicColorArray, dxArray, dyArray, y, width, IndexedAnimationBehavior(1, 250))
    

    def __init__(self, animationInterfaceArray: list[IndexedAnimation], basicColorArray: list[BasicColor], dxArray: list[int], dyArray: list[int], y: int, width: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.animation.IndexedAnimation import IndexedAnimation
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(animationBehavior)
        __class__._init_fields(self)
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
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        currentTime: int = self.systemWrapper.currentTimeMillis()
        totalTimeElapsed: int = currentTime - self.lastFrameStartTime
        indexedAnimationBehavior: IndexedAnimationBehavior = self.getAnimationBehavior()
        if totalTimeElapsed > indexedAnimationBehavior.frameDelayTime:
            self.previousFrame()
            self.lastFrameStartTime = currentTime
        if self.animationInterfaceArray[0].getFrame() == 0:
            indexedAnimationBehavior.loopIndex += 1
    

    def isComplete(self) -> bool:
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        indexedAnimationBehavior: IndexedAnimationBehavior = self.getAnimationBehavior()
        if indexedAnimationBehavior.loopTotal == -1 or indexedAnimationBehavior.loopIndex < indexedAnimationBehavior.loopTotal or self.getFrame() != 0:
            return False
        else:
            return True
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
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
        from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
        self.setLastFrame()
        indexedAnimationBehavior: IndexedAnimationBehavior = (self.getAnimationBehavior())
        indexedAnimationBehavior.reset()
    

    def previousFrame(self) -> None:
        for index in range(0, self.sizeP):
            self.animationInterfaceArray[index].previousFrame()
    

    def paintFrameXY(self, graphics: Graphics, frame: int, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.setFrame(frame)
        self.paintXY(graphics, x, y)
    

    def paintXY(self, graphics: Graphics, ax: int, ay: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        x: int = 0
        if self.widthP != -2147483648:
            x = (java_divide((self.displayInfoSingleton.getLastWidth() - self.widthP), 2))
        deltaX: int = 0
        deltaY: int = 0
        for index in range(0, self.sizeP):
            deltaX = self.dxArray[index] + x
            deltaY = self.dyArray[index] + self.y
            if self.basicColorArray[index] != self.CLEAR_COLOR:
                self.basicSetColorUtil.setBasicColorP(graphics, self.basicColorArray[index])
            self.animationInterfaceArray[index].paintXY(graphics, deltaX, deltaY)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.animation.IndexedAnimation import IndexedAnimation
# from org.allbinary.animation.IndexedAnimationBehavior import IndexedAnimationBehavior
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


