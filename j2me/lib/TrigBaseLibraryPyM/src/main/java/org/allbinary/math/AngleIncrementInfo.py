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
# package org.allbinary.math

from __future__ import annotations



class AngleIncrementInfo:
    INCREMENT: str = "Inc: "

    def _init_fields(self) -> None:
        self.angleIncrement: int = None
        self.DOWN_FRAME: int = None
        self.UP_FRAME: int = None
        self.LEFT_FRAME: int = None
        self.RIGHT_FRAME: int = None
        self.frameUtil: FrameUtil = FrameUtil.getInstance()
    

    def __init__(self, angleIncrement: int) -> None:
        from org.allbinary.math.AngleFactory import AngleFactory
        self._init_fields()
        self.angleIncrement = angleIncrement
        angleFactory: AngleFactory = AngleFactory.getInstance()
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        self.DOWN_FRAME = smallIntegerSingletonFactory.getAt(angleFactory.DOWN.getValue() / self.angleIncrement)
        self.UP_FRAME = smallIntegerSingletonFactory.getAt(int(angleFactory.UP.getValue()))
        self.LEFT_FRAME = smallIntegerSingletonFactory.getAt(angleFactory.LEFT.getValue() / self.angleIncrement)
        self.RIGHT_FRAME = smallIntegerSingletonFactory.getAt(angleFactory.RIGHT.getValue() / self.angleIncrement)
    

    def getFrameAngle(self, frame: int) -> int:
        return self.frameUtil.getFrameAngle(frame, self.angleIncrement)
    

    def getAngleIncrement(self) -> int:
        return self.angleIncrement
    

    def toString(self) -> str:
        return str(StringMaker().append(AngleIncrementInfo.INCREMENT).appendshort(self.angleIncrement))

    def __str__(self) -> str:
        return self.toString()
    

    def getClosestGeneralDirection(self, angle: int) -> int:
        closestDirection: int = SmallIntegerSingletonFactory.getInstance().getAt(360)
        if int(self.UP_FRAME) - angle < int(closestDirection) - angle:
            closestDirection = self.UP_FRAME
        if int(self.DOWN_FRAME) - angle < int(closestDirection) - angle:
            closestDirection = self.DOWN_FRAME
        if int(self.LEFT_FRAME) - angle < int(closestDirection) - angle:
            closestDirection = self.LEFT_FRAME
        if int(self.RIGHT_FRAME) - angle < int(closestDirection) - angle:
            closestDirection = self.RIGHT_FRAME
        return int(closestDirection)
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from jsinterop.annotations.JsProperty import JsProperty
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from org.allbinary.math.FrameUtil import FrameUtil


