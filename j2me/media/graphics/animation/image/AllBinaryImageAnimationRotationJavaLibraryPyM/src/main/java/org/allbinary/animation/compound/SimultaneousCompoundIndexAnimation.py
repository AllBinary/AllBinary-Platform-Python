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


class SimultaneousCompoundIndexAnimation(IndexedAnimation):

    def _init_fields(self) -> None:
        self.animationInterfaceArray: list[IndexedAnimation] = None
    

    def __init__(self, animationInterfaceArray: list[IndexedAnimation], animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.animationInterfaceArray = animationInterfaceArray
    

    def setFrame(self, frameIndex: int) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].setFrame(frameIndex)
    

    def getFrame(self) -> int:
        return self.animationInterfaceArray[0].getFrame()
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.animationInterfaceArray[0].getAnimationSize()
    

    def getSize(self) -> int:
        return self.animationInterfaceArray[0].getSize()
    

    def previousFrame(self) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].previousFrame()
    

    # throws Exception
    def nextFrame(self) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].nextFrame()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].paintXY(graphics, x, y)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].paintThreedXYZ(graphics, x, y, z)
    

    # throws Exception
    def set(self, gl: GL) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].set(gl)
    

    def getAnimationInterfaceArray(self) -> list[IndexedAnimation]:
        return self.animationInterfaceArray
    

    def setAnimationInterfaceArray(self, animationInterfaceArray: list[IndexedAnimation]) -> None:
        self.animationInterfaceArray = animationInterfaceArray
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil


