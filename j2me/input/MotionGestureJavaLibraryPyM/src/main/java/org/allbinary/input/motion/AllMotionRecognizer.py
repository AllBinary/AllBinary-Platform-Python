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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer


@java_inherited_overloads
class AllMotionRecognizer(MotionRecognizer):
    index: int = 0
    pointCircularPool: GPointCircularPool = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("motionGestureRecognizer", None)
        vars(self).setdefault("touchButtonProcessing", False)
        vars(self).setdefault("touchButtonRecognizer", None)
        vars(self).setdefault("id", 0)
        vars(self).setdefault("lastX", 0)
        vars(self).setdefault("lastY", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "motionGestureRecognizer" not in vars(self): self.motionGestureRecognizer: MotionGestureRecognizer = None
        self.touchButtonProcessing: bool = False
        if "touchButtonRecognizer" not in vars(self): self.touchButtonRecognizer: TouchButtonRecognizer = None
        if "id" not in vars(self): self.id: int = 0
        if "lastX" not in vars(self): self.lastX: int = 0
        if "lastY" not in vars(self): self.lastY: int = 0
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.motion.button.TouchButtonRecognizer import TouchButtonRecognizer
        from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer
        super().__init__()
        __class__._init_fields(self)
        self.id = ((setattr(AllMotionRecognizer, "index", AllMotionRecognizer.index + 1) or AllMotionRecognizer.index) - 1)
        self.motionGestureRecognizer = MotionGestureRecognizer(self.id)
        self.touchButtonRecognizer = TouchButtonRecognizer()
    

    # throws Exception
    def processStartMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        if self.touchButtonRecognizer.pressTouchButtonInput(x, y, deviceId):
            self.touchButtonProcessing = True
        if not (self.touchButtonProcessing):
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processPressedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processEndMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        if self.touchButtonRecognizer.releaseTouchButtonInput(x, y, deviceId):
            pass
        if not (self.touchButtonProcessing):
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processReleasedMotionEvent(point, deviceId, modifiers)
        if self.touchButtonProcessing:
            self.touchButtonProcessing = False
    

    # throws Exception
    def processDraggedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        if self.touchButtonProcessing:
            self.touchButtonRecognizer.pressTouchButtonInput(x, y, deviceId)
        if not (self.touchButtonProcessing):
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processDraggedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processMovedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        if x != self.lastX or y != self.lastY:
            self.lastX = x
            self.lastY = y
            point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
            point.setX(x)
            point.setY(y)
            self.motionGestureRecognizer.processMovedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processScrolledMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        point: CustomGPoint = AllMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processScrolledMotionEvent(point, deviceId, modifiers)
    

    def getMotionGestureRecognizer(self) -> MotionGestureRecognizer:
        from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer
        return self.motionGestureRecognizer
# from org.allbinary.graphics.CustomGPoint import CustomGPoint
# from org.allbinary.graphics.GPointCircularPool import GPointCircularPool
# from org.allbinary.input.motion.button.TouchButtonRecognizer import TouchButtonRecognizer
# from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _AllMotionRecognizer_pointCircularPool() -> object:
    from org.allbinary.graphics.GPointCircularPool import GPointCircularPool
    return GPointCircularPool(40)

lazy_static(AllMotionRecognizer, "pointCircularPool", _AllMotionRecognizer_pointCircularPool)

