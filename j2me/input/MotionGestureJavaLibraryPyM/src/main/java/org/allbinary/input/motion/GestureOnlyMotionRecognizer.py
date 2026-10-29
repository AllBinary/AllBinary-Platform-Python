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


class GestureOnlyMotionRecognizer(MotionRecognizer):
    index: int = 0
    pointCircularPool: GPointCircularPool = GPointCircularPool(40)

    def _init_fields(self) -> None:
        self.motionGestureRecognizer: MotionGestureRecognizer = None
        self.id: int = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.id = ((setattr(GestureOnlyMotionRecognizer, "index", GestureOnlyMotionRecognizer.index + 1) or GestureOnlyMotionRecognizer.index) - 1)
        self.motionGestureRecognizer = MotionGestureRecognizer(self.id)
    

    # throws Exception
    def processStartMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        point: CustomGPoint = GestureOnlyMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processPressedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processEndMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        point: CustomGPoint = GestureOnlyMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processReleasedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processDraggedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        point: CustomGPoint = GestureOnlyMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processDraggedMotionEvent(point, deviceId, modifiers)
from org.allbinary.graphics.CustomGPoint import CustomGPoint
from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer


