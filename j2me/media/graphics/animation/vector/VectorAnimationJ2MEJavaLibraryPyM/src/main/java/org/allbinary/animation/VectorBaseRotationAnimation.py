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

from org.allbinary.animation.RotationAnimation import RotationAnimation
from org.allbinary.animation.VectorAnimationInterface import VectorAnimationInterface


class VectorBaseRotationAnimation(RotationAnimation, VectorAnimationInterface):

    def _init_fields(self) -> None:
        self.currentPoints: list[list[list[int]]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY_ARRAY
    

    def __init__(self, angleInfo: AngleInfo, currentPoints: list[list[list[int]]], basicColor: BasicColor, animationBehavior: AnimationBehavior) -> None:
        super().__init__(angleInfo, CircularIndexUtil.createInstance(360 / angleInfo.getAngleIncrementInfo().getAngleIncrement()), animationBehavior)
        self._init_fields()
        self.setPoints(currentPoints)
        self.setBasicColorP(basicColor)
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def getFrame(self) -> int:
        return self.circularIndexUtil.getIndex()
    

    def setFrame(self, index: int) -> None:
        self.circularIndexUtil.setIndex(index)
    

    def nextFrame(self) -> None:
        self.circularIndexUtil.next()
    

    def previousFrame(self) -> None:
        self.circularIndexUtil.previous()
    

    def getSize(self) -> int:
        return len(self.currentPoints)
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP(graphics, self.basicColor)
        try:
            nextPointX: int = 0
            nextPointY: int = 0
            nextPoint: list[int] = None
            point: list[int] = None
            currentPointsFrame: list[list[int]] = self.currentPoints[self.circularIndexUtil.getIndex()]
            size: int = len(currentPointsFrame)
            index: int = size - 2
            while (index := index - 1) >= 0:
                nextPoint = currentPointsFrame[index]
                point = currentPointsFrame[index + 1]
                nextPointX = nextPoint[0]
                nextPointY = nextPoint[1]
                if nextPointX != 1000:
                    graphics.drawLine(point[0] + x, point[1] + y, nextPointX + x, nextPointY + y)
                else:
                    index -= 1
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "paintVectors", e)
    

    def getPoints(self, frame: int) -> list[list[int]]:
        return self.currentPoints[frame]
    

    def setPoints(self, currentPoints: list[list[list[int]]]) -> None:
        self.currentPoints = currentPoints
        self.circularIndexUtil = CircularIndexUtil.createInstance(len(self.currentPoints))
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


