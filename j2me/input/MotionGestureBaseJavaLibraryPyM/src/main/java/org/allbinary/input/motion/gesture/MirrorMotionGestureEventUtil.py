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
# package org.allbinary.input.motion.gesture

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class MirrorMotionGestureEventUtil:
    instance: MirrorMotionGestureEventUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.input.motion.gesture.observer.MotionEventCircularPool import MotionEventCircularPool
        self.motionEventCircularPool: MotionEventCircularPool = None
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.gesture.observer.MotionEventCircularPool import MotionEventCircularPool
        self._init_fields()
        self.motionEventCircularPool = MotionEventCircularPool.createPool(2147483647)
    

    # throws Exception
    def mirrorVerticle(self, motionGestureEvent: MotionGestureEvent, halfWidth: int) -> MotionGestureEvent:
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
        event: MotionGestureEvent = self.motionEventCircularPool.getInstance(motionGestureEvent.getMotionGesture())
        previousNewX: int = self.getNewX(motionGestureEvent.getPreviousPoint().getX(), halfWidth)
        currentNewX: int = self.getNewX(motionGestureEvent.getCurrentPoint().getX(), halfWidth)
        pointFactory: PointFactory = PointFactory.getInstance()
        mirroredPreviousPoint: GPoint = pointFactory.createXY(previousNewX, motionGestureEvent.getPreviousPoint().getY())
        mirroredCurrentPoint: GPoint = pointFactory.createXY(currentNewX, motionGestureEvent.getCurrentPoint().getY())
        event.setPreviousPoint(mirroredPreviousPoint)
        event.setCurrentPoint(mirroredCurrentPoint)
        return event
    

    def getNewX(self, x: int, halfWidth: int) -> int:
        newX: int = 0
        if x > halfWidth:
            newX = halfWidth - (x - halfWidth)
        else:
            newX = halfWidth + (halfWidth - x)
        return newX
    

    @staticmethod
    def getInstance() -> MirrorMotionGestureEventUtil:
        return MirrorMotionGestureEventUtil.instance
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.input.motion.gesture.observer.MotionEventCircularPool import MotionEventCircularPool
# from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent


def _MirrorMotionGestureEventUtil_instance() -> object:
    return MirrorMotionGestureEventUtil()

lazy_static(MirrorMotionGestureEventUtil, "instance", _MirrorMotionGestureEventUtil_instance)

