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

from org.allbinary.animation.RotationAnimation import RotationAnimation


class SimultaneousCompoundRotationAnimation(RotationAnimation):

    def _init_fields(self) -> None:
        self.animationInterfaceArray: list[RotationAnimation] = None
    

    def __init__(self, animationInterfaceArray: list[RotationAnimation], animationBehavior: AnimationBehavior) -> None:
        super().__init__(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), animationBehavior)
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
    

    def previousRotation(self) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].previousRotation()
    

    def nextRotation(self) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].nextRotation()
    

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
    

    def setFrameByDirection(self, direction: Direction) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].setFrameByDirection(direction)
    

    def setFrameToAngle(self, angle: Angle) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].setFrameToAngle(angle)
    

    def adjustFrameToAngle(self, newAngle: Angle) -> None:
        self.adjustFrame(newAngle.getValue())
    

    def adjustFrame(self, angle: int) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].adjustFrame(angle)
    

    def getAngleInfoP(self) -> AngleInfo:
        return self.animationInterfaceArray[0].getAngleInfoP()
    

    def getAnimationInterfaceArray(self) -> list[RotationAnimation]:
        return self.animationInterfaceArray
    

    def setAnimationInterfaceArray(self, animationInterfaceArray: list[RotationAnimation]) -> None:
        self.animationInterfaceArray = animationInterfaceArray
    

    # throws Exception
    def set(self, gl: GL) -> None:
        index = len(self.animationInterfaceArray)
        while (index := index - 1) >= 0:
            self.animationInterfaceArray[index].set(gl)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.direction.Direction import Direction
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


