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
from org.allbinary.animation.compound.CompoundAnimationInterface import CompoundAnimationInterface


class AutoCompoundRotationAnimation(RotationAnimation, CompoundAnimationInterface):

    def _init_fields(self) -> None:
        self.animationInterfaceArray: list[RotationAnimation] = None
    

    def __init__(self, animationInterfaceArray: list[RotationAnimation], animationBehavior: AnimationBehavior) -> None:
        super().__init__(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), animationBehavior)
        self._init_fields()
        self.animationInterfaceArray = animationInterfaceArray
        self.circularIndexUtil = CircularIndexUtil.createInstance(len(self.animationInterfaceArray))
    

    def setFrame(self, index: int) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].setFrame(index)
    

    def getFrame(self) -> int:
        return self.animationInterfaceArray[self.circularIndexUtil.getIndex()].getFrame()
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.animationInterfaceArray[self.circularIndexUtil.getIndex()].getAnimationSize()
    

    def getSize(self) -> int:
        return self.animationInterfaceArray[self.circularIndexUtil.getIndex()].getSize()
    

    def previousFrame(self) -> None:
        self.circularIndexUtil.previous()
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].previousFrame()
    

    # throws Exception
    def nextFrame(self) -> None:
        self.circularIndexUtil.next()
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].nextFrame()
    

    def previousRotation(self) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].previousRotation()
    

    def nextRotation(self) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].nextRotation()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

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
    

    def setFrameByDirection(self, direction: Direction) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].setFrameByDirection(direction)
    

    def setFrameToAngle(self, angle: Angle) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].setFrameToAngle(angle)
    

    def adjustFrameToAngle(self, newAngle: Angle) -> None:
        self.adjustFrame(newAngle.getValue())
    

    def adjustFrame(self, angle: int) -> None:
        self.animationInterfaceArray[self.circularIndexUtil.getIndex()].adjustFrame(angle)
    

    def getAngleInfoP(self) -> AngleInfo:
        return self.animationInterfaceArray[self.circularIndexUtil.getIndex()].getAngleInfoP()
    

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
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.direction.Direction import Direction
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


