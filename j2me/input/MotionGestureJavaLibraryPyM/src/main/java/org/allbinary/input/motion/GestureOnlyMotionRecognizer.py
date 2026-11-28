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
class GestureOnlyMotionRecognizer(MotionRecognizer):
    index: int = 0
    pointCircularPool: GPointCircularPool = None
    def _java_defaults(self):
        vars(self).setdefault("motionGestureRecognizer", None)
        vars(self).setdefault("id", 0)

    def _init_fields(self) -> None:
        if "motionGestureRecognizer" not in vars(self): self.motionGestureRecognizer: MotionGestureRecognizer = None
        if "id" not in vars(self): self.id: int = 0
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer
        super().__init__()
        __class__._init_fields(self)
        self.id = ((setattr(GestureOnlyMotionRecognizer, "index", GestureOnlyMotionRecognizer.index + 1) or GestureOnlyMotionRecognizer.index) - 1)
        self.motionGestureRecognizer = MotionGestureRecognizer(self.id)
    

    # throws Exception
    def processStartMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        point: CustomGPoint = GestureOnlyMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processPressedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processEndMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        point: CustomGPoint = GestureOnlyMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processReleasedMotionEvent(point, deviceId, modifiers)
    

    # throws Exception
    def processDraggedMotionEvent(self, x: int, y: int, deviceId: int, modifiers: int) -> None:
        from org.allbinary.graphics.CustomGPoint import CustomGPoint
        point: CustomGPoint = GestureOnlyMotionRecognizer.pointCircularPool.getNextInstance()
        point.setX(x)
        point.setY(y)
        self.motionGestureRecognizer.processDraggedMotionEvent(point, deviceId, modifiers)
# from org.allbinary.graphics.CustomGPoint import CustomGPoint
# from org.allbinary.graphics.GPointCircularPool import GPointCircularPool
# from org.allbinary.input.motion.gesture.MotionGestureRecognizer import MotionGestureRecognizer


def _GestureOnlyMotionRecognizer_pointCircularPool() -> object:
    from org.allbinary.graphics.GPointCircularPool import GPointCircularPool
    return GPointCircularPool(40)

lazy_static(GestureOnlyMotionRecognizer, "pointCircularPool", _GestureOnlyMotionRecognizer_pointCircularPool)

