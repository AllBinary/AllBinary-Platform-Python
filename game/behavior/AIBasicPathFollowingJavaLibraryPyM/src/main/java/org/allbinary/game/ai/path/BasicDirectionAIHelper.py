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
# package org.allbinary.game.ai.path

from __future__ import annotations

import math


class BasicDirectionAIHelper:

    def _init_fields(self) -> None:
        self.name: str = None
        self.angleInfo: AngleInfo = None
    

    def __init__(self, name: str, angleInfo: AngleInfo) -> None:
        self._init_fields()
        self.name = name
        self.angleInfo = angleInfo
    

    def turnAI(self, frame: int) -> int:
        keyDirection: int = -1
        directionAngle: int = self.angleInfo.getAngleIncrementInfo().getFrameAngle(frame)
        angle: int = self.angleInfo.getAngle()
        degrees: int = abs(directionAngle - angle)
        if degrees < 180:
            if angle > directionAngle:
                keyDirection = Canvas.LEFT
            elif angle < directionAngle:
                keyDirection = Canvas.RIGHT
        else:
            if angle > directionAngle:
                keyDirection = Canvas.RIGHT
            elif angle < directionAngle:
                keyDirection = Canvas.LEFT
        return keyDirection
    

    def getAIKeyPressed(self, frame: int) -> int:
        angle: int = ((int(self.angleInfo.getAngleIncrementInfo().getFrameAngle(int(frame))) + 32768) % 65536 - 32768)
        if self.angleInfo.getAngle() != angle:
            return self.turnAI(int(frame))
        else:
            return Canvas.UP
    

    def getAIKeyPressedFromDirection(self, geographicMapDirectionData: Direction) -> int:
        keyDirection: int = -1
        angleIncrementInfo: AngleIncrementInfo = self.angleInfo.getAngleIncrementInfo()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if geographicMapDirectionData == directionFactory.DOWN:
            keyDirection = self.getAIKeyPressed(angleIncrementInfo.DOWN_FRAME)
        elif geographicMapDirectionData == directionFactory.UP:
            keyDirection = self.getAIKeyPressed(angleIncrementInfo.UP_FRAME)
        elif geographicMapDirectionData == directionFactory.LEFT:
            keyDirection = self.getAIKeyPressed(angleIncrementInfo.LEFT_FRAME)
        elif geographicMapDirectionData == directionFactory.RIGHT:
            keyDirection = self.getAIKeyPressed(angleIncrementInfo.RIGHT_FRAME)
        return keyDirection
    

    def getAngleInfoP(self) -> AngleInfo:
        return self.angleInfo
    

    def getName(self) -> str:
        return self.name
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.math.AngleIncrementInfo import AngleIncrementInfo
from org.allbinary.math.AngleInfo import AngleInfo


