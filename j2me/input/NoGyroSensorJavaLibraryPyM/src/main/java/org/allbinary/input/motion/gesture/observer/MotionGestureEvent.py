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
# package org.allbinary.input.motion.gesture.observer

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class MotionGestureEvent(AllBinaryEventObject):
    PREVIOUS: str = " Previous: "
    HASHCODE: str = " hashcode: "

    def _init_fields(self) -> None:
        self.motionGesture: MotionGestureInput = TouchMotionGestureFactory.getInstance().NO_MOTION
        self.id: int = None
        self.previousPoint: GPoint = PointFactory.getInstance().ZERO_ZERO
        self.currentPoint: GPoint = PointFactory.getInstance().ZERO_ZERO
        self.commonLabels: CommonLabels = CommonLabels.getInstance()
    

    def __init__(self, source: object, id: int, motionGesture: MotionGestureInput) -> None:
        super().__init__(source)
        self._init_fields()
        self.id = id
        self.setMotionGesture(motionGesture)
    

    def getMotionGesture(self) -> MotionGestureInput:
        return self.motionGesture
    

    def setMotionGesture(self, motionGesture: MotionGestureInput) -> None:
        self.motionGesture = motionGesture
    

    def getPreviousPoint(self) -> GPoint:
        return self.previousPoint
    

    def setPreviousPoint(self, previousPoint: GPoint) -> None:
        self.previousPoint = previousPoint
    

    def getCurrentPoint(self) -> GPoint:
        return self.currentPoint
    

    def setCurrentPoint(self, currentPoint: GPoint) -> None:
        self.currentPoint = currentPoint
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringUtil: StringUtil = StringUtil.getInstance()
        stringBuffer.append(stringUtil.toString(self.motionGesture))
        stringBuffer.append(self.commonLabels.CURRENT)
        stringBuffer.append(stringUtil.toString(self.currentPoint))
        stringBuffer.append(MotionGestureEvent.PREVIOUS)
        stringBuffer.append(stringUtil.toString(self.previousPoint))
        stringBuffer.append(MotionGestureEvent.HASHCODE)
        stringBuffer.appendint(int(TsUtil.getInstance().hashCode(self)))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getId(self) -> int:
        return self.id
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels


