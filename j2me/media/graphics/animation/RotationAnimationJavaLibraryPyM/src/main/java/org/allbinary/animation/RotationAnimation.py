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

from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.RotationAnimationInterface import RotationAnimationInterface


class RotationAnimation(IndexedAnimation, RotationAnimationInterface):

    def _init_fields(self) -> None:
        self.frameUtil: FrameUtil = FrameUtil.getInstance()
        self.directionUtil: DirectionUtil = DirectionUtil.getInstance()
        self.angleInfo: AngleInfo = None
        self.circularIndexUtil: CircularIndexUtil = None
    

    def __init__(self, angleInfo: AngleInfo, circularIndexUtil: CircularIndexUtil, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.angleInfo = angleInfo
        self.circularIndexUtil = circularIndexUtil
    

    def nextRotationX(self) -> None:
        pass
    

    def previousRotationX(self) -> None:
        pass
    

    def nextRotation(self) -> None:
        self.angleInfo.adjustAngle(self.circularIndexUtil.next())
    

    def previousRotation(self) -> None:
        self.angleInfo.adjustAngle(self.circularIndexUtil.previous())
    

    def nextRotationZ(self) -> None:
        pass
    

    def previousRotationZ(self) -> None:
        pass
    

    def setFrame(self, index: int) -> None:
        self.circularIndexUtil.setIndex(index)
        newFrame: int = self.circularIndexUtil.getIndex()
        self.angleInfo.adjustAngle(newFrame)
    

    def setFrameByDirection(self, direction: Direction) -> None:
        angle: Angle = self.directionUtil.getFrameAngle(direction)
        self.adjustFrameToAngle(angle)
    

    def setFrameToAngle(self, angle: Angle) -> None:
        self.adjustFrameToAngle(angle)
    

    def adjustFrameToAngle(self, angle: Angle) -> None:
        self.adjustFrame(angle.getValue())
    

    def adjustFrame(self, angle: int) -> None:
        self.setFrame(self.frameUtil.getFrameForAngle(angle, int(self.angleInfo.getAngleIncrementInfo().getAngleIncrement())))
    

    def getFrame(self) -> int:
        return self.circularIndexUtil.getIndex()
    

    def getSize(self) -> int:
        return self.circularIndexUtil.getSize()
    

    def getAngleInfoP(self) -> AngleInfo:
        return self.angleInfo
    

    def toString(self) -> str:
        return str(StringMaker().append(str(super())).append("circularIndexUtil: ").append(str(self.circularIndexUtil)).append("angleInfo: ").append(str(self.angleInfo)))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionUtil import DirectionUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.math.FrameUtil import FrameUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


