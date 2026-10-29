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

import math


class MotionGestureRecognizer:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.j2seMath: J2SEMath = J2SEMath.getInstance()
        self.origin: GPoint = PointFactory.getInstance().ZERO_ZERO
        self.previous: GPoint = self.origin
        self.intermediate: GPoint = self.origin
        self.line: Line = Line(self.origin, self.origin)
        self.motionGesturesHandler: BasicMotionGesturesHandler = None
        self.movedMotionGesturesHandler: BasicEventHandler = None
        self.scrolledMotionGesturesHandler: BasicEventHandler = None
        self.motionEventCircularPool: MotionEventCircularPool = None
    

    def __init__(self, id: int) -> None:
        self._init_fields()
        self.motionEventCircularPool = MotionEventCircularPool.createPool(id)
        motionGesturesHandler: BasicEventHandler = BasicEventHandler()
        movedMotionGesturesHandler: BasicEventHandler = motionGesturesHandler
        scrolledMotionGesturesHandler: BasicEventHandler = motionGesturesHandler
        try:
            motionGesturesHandler = BasicMotionGesturesHandler.getInstance()
            movedMotionGesturesHandler = MovedMotionGesturesHandler.getInstance()
            scrolledMotionGesturesHandler = ScrolledMotionGesturesHandler.getInstance()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
        self.motionGesturesHandler = motionGesturesHandler
        self.movedMotionGesturesHandler = movedMotionGesturesHandler
        self.scrolledMotionGesturesHandler = scrolledMotionGesturesHandler
    

    # throws Exception
    def processPressedMotionEvent(self, current: GPoint, deviceId: int, button: int) -> bool:
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        self.intermediate = self.origin
        self.previous = self.origin
        event: MotionGestureEvent = self.motionEventCircularPool.getInstance(TouchMotionGestureFactory.getInstance().PRESSED)
        event.setPreviousPoint(self.previous)
        event.setCurrentPoint(current)
        self.motionGesturesHandler.fireEvent(event)
        return True
    

    # throws Exception
    def processReleasedMotionEvent(self, current: GPoint, deviceId: int, button: int) -> bool:
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        event: MotionGestureEvent = self.motionEventCircularPool.getInstance(TouchMotionGestureFactory.getInstance().RELEASED)
        event.setPreviousPoint(self.previous)
        event.setCurrentPoint(current)
        self.motionGesturesHandler.fireEvent(event)
        return True
    

    # throws Exception
    def processDraggedMotionEvent(self, current: GPoint, deviceId: int, buttonMask: int) -> None:
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        if self.previous == self.origin or self.intermediate == self.origin:
            self.previous = current
            self.intermediate = current
            return
        self.line.setP1(self.previous)
        self.line.setP2(current)
        minimumMotionGesture: int = MotionGestureConfigurationFactory.getInstance().getMinimumMotionGesture()
        if self.j2seMath.abs(float(self.line.getDeltaX())) < minimumMotionGesture and self.j2seMath.abs(float(self.line.getDeltaY())) < minimumMotionGesture:
            self.intermediate = current
            return
        gradient: float = self.line.getGradient()
        absGradient: float = float(self.j2seMath.abs(gradient))
        conf: MotionGestureConfiguration = MotionGestureConfigurationFactory.getInstance()
        touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
        newMotionGesture: MotionGestureInput = touchMotionGestureFactory.NO_MOTION
        diagonalToleranceHigher: float = 12.0
        diagonalToleranceLower: float = 12.0
        if conf.isDiagonalMotionGestureAllowed():
            diagonalToleranceHigher = float((90 - conf.getDiagonalTolerance()))
            diagonalToleranceLower = float(conf.getDiagonalTolerance())
        if absGradient > math.tan(math.radians(diagonalToleranceHigher)):
            if self.line.getDeltaY() > 0:
                newMotionGesture = touchMotionGestureFactory.UP
            else:
                newMotionGesture = touchMotionGestureFactory.DOWN
        else:
            if absGradient < math.tan(math.radians(diagonalToleranceLower)):
                if self.line.getDeltaX() > 0:
                    newMotionGesture = touchMotionGestureFactory.LEFT
                else:
                    newMotionGesture = touchMotionGestureFactory.RIGHT
            else:
                if gradient > 0.0:
                    if self.line.getDeltaX() > 0:
                        newMotionGesture = touchMotionGestureFactory.DIAGONAL_UP_LEFT
                    else:
                        newMotionGesture = touchMotionGestureFactory.DIAGONAL_DOWN_RIGHT
                else:
                    if self.line.getDeltaX() > 0:
                        newMotionGesture = touchMotionGestureFactory.DIAGONAL_DOWN_LEFT
                    else:
                        newMotionGesture = touchMotionGestureFactory.DIAGONAL_UP_RIGHT
        self.previous = current
        self.intermediate = current
        event: MotionGestureEvent = self.motionEventCircularPool.getInstance(newMotionGesture)
        event.setPreviousPoint(self.previous)
        event.setCurrentPoint(current)
        self.motionGesturesHandler.fireEvent(event)
        return
    

    # throws Exception
    def processMovedMotionEvent(self, current: GPoint, deviceId: int, button: int) -> bool:
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        event: MotionGestureEvent = self.motionEventCircularPool.getInstance(TouchMotionGestureFactory.getInstance().NO_MOTION)
        event.setPreviousPoint(self.previous)
        event.setCurrentPoint(current)
        self.movedMotionGesturesHandler.fireEvent(event)
        return True
    

    # throws Exception
    def processScrolledMotionEvent(self, current: GPoint, deviceId: int, button: int) -> bool:
        from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
        touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
        newMotionGesture: MotionGestureInput = touchMotionGestureFactory.NO_MOTION
        if button > 0:
            newMotionGesture = touchMotionGestureFactory.SCROLL_UP
        elif button < 0:
            newMotionGesture = touchMotionGestureFactory.SCROLL_DOWN
        event: MotionGestureEvent = self.motionEventCircularPool.getInstance(newMotionGesture)
        event.setPreviousPoint(self.previous)
        event.setCurrentPoint(current)
        self.scrolledMotionGesturesHandler.fireEvent(event)
        return True
    

    def getMotionGesturesHandler(self) -> BasicMotionGesturesHandler:
        return self.motionGesturesHandler
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Line import Line
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfiguration import MotionGestureConfiguration
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfigurationFactory import MotionGestureConfigurationFactory
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.input.motion.gesture.observer.MotionEventCircularPool import MotionEventCircularPool
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.input.motion.gesture.observer.MovedMotionGesturesHandler import MovedMotionGesturesHandler
from org.allbinary.input.motion.gesture.observer.ScrolledMotionGesturesHandler import ScrolledMotionGesturesHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.J2SEMath import J2SEMath
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler
from org.allbinary.string.CommonStrings import CommonStrings


