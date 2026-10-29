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
from org.allbinary.animation.VectorAnimationInterface import VectorAnimationInterface


class VectorAnimation(IndexedAnimation, VectorAnimationInterface):

    def _init_fields(self) -> None:
        self.currentPoints: list[list[list[int]]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY_ARRAY
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(0)
    

    @staticmethod
    def createVectorAnimation(currentPoints2: list[list[int]], basicColor: BasicColor, animationBehavior: AnimationBehavior) -> VectorAnimation:
        currentPoints: list[list[list[int]]] = [[[0] * (2) for _ in range(len(currentPoints2))] for _ in range(1)]
        size: int = len(currentPoints2)
        for index in range(0, size):
            currentPoints[0][index][0] = currentPoints2[index][0]
            currentPoints[0][index][1] = currentPoints2[index][1]
        return VectorAnimation(currentPoints, basicColor, animationBehavior)
    

    def __init__(self, currentPoints: list[list[list[int]]], basicColor: BasicColor, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.setPoints(currentPoints)
        self.setBasicColorP(basicColor)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        changed: bool = False
        if self.getBasicColorP() is None or int(self.getBasicColorP()) != int(basicColor):
            changed = True
        super().setBasicColorP(basicColor)
        if changed:
            self.updateModifiers()
    

    def changeBasicColor(self, basicColor: BasicColor) -> None:
        changed: bool = False
        if self.getChangeBasicColor() is None or int(self.getChangeBasicColor()) != int(basicColor):
            changed = True
        super().changeBasicColor(basicColor)
        if changed:
            self.updateModifiers()
    

    def setAlpha(self, alpha: int) -> None:
        changed: bool = False
        if self.alphaP != alpha:
            changed = True
        super().setAlpha(alpha)
        if changed:
            self.updateModifiers()
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        pass
    

    def setMaxScale(self, maxScaleX: float, maxScaleY: float) -> None:
        pass
    

    def updateModifiers(self) -> None:
        pass
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def getSize(self) -> int:
        return len(self.currentPoints)
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        return PrimitiveIntUtil.getArrayInstance()
    

    def nextFrame(self) -> None:
        self.circularIndexUtil.next()
    

    def previousFrame(self) -> None:
        self.circularIndexUtil.previous()
    

    def paintVectors(self, graphics: Graphics, x: int, y: int) -> None:
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
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP(graphics, self.basicColor)
        self.paintVectors(graphics, x, y)
    

    def getFrame(self) -> int:
        return self.circularIndexUtil.getIndex()
    

    def setFrame(self, index: int) -> None:
        self.circularIndexUtil.setIndex(index)
    

    def getPoints(self, frame: int) -> list[list[int]]:
        return self.currentPoints[frame]
    

    def setPoints(self, currentPoints: list[list[list[int]]]) -> None:
        self.currentPoints = currentPoints
        self.circularIndexUtil = CircularIndexUtil.createInstance(len(currentPoints))
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil


