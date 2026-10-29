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
# package org.allbinary.input.motion

from __future__ import annotations

from org.allbinary.graphics.GPointCircularPool import GPointCircularPool
from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer


class AllMotionRecognizer(MotionRecognizer):
    index: int = 0
    pointCircularPool: GPointCircularPool = GPointCircularPool(40)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.motionGestureRecognizer: MotionGestureRecognizer = None
        self.touchButtonProcessing: bool = False
        self.touchButtonRecognizer: TouchButtonRecognizer = None
        self.id: int = None
        self.lastX: int = 0
        self.lastY: int = 0
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.id = ((setattr(AllMotionRecognizer, "index", AllMotionRecognizer.index + 1) or AllMotionRecognizer.index) - 1)
        self.motionGestureRecognizer = MotionGestureRecognizer(self.id)
        self.touchButtonRecognizer = TouchButtonRecognizer()
    

    # throws Exception
    def processStartMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if self.touchButtonRecognizer.pressTouchButtonInput(x, y, deviceId):
            self.touchButtonProcessing = True
        if not self.touchButtonProcessing:
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processPressedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processEndMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if self.touchButtonRecognizer.releaseTouchButtonInput(x, y, deviceId):
            pass
        if not self.touchButtonProcessing:
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processReleasedMotionEvent(point, deviceId, modifiers)
        if self.touchButtonProcessing:
            self.touchButtonProcessing = False
    

    # throws Exception
    def processDraggedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if self.touchButtonProcessing:
            self.touchButtonRecognizer.pressTouchButtonInput(x, y, deviceId)
        if not self.touchButtonProcessing:
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processDraggedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processMovedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        if x != self.lastX or y != self.lastY:
            self.lastX = x
            self.lastY = y
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processMovedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processScrolledMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processScrolledMotionEvent(point, deviceId, modifiers)
    

    def getMotionGestureRecognizer(self) -> MotionGestureRecognizer:
        return self.motionGestureRecognizer
from org.allbinary.graphics.CustomGPoint import CustomGPoint
from org.allbinary.input.motion.button.TouchButtonRecognizer import TouchButtonRecognizer
from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer
from org.allbinary.logic.communication.log.LogUtil import LogUtil


