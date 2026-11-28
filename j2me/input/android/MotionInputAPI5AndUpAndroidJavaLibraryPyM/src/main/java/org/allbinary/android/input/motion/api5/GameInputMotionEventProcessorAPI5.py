#
# AllBinary Open License Version 1
# Copyright (c) 2009 AllBinary
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
# package org.allbinary.android.input.motion.api5

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.android.input.motion.BaseGameInputMotionEventProcessor import BaseGameInputMotionEventProcessor


@java_inherited_overloads
class GameInputMotionEventProcessorAPI5(BaseGameInputMotionEventProcessor):
    instance: object = None
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("displayInfo", None)
        vars(self).setdefault("motionRecognizerArray", None)
        vars(self).setdefault("TOTAL_MINUS_ONE", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if "motionRecognizerArray" not in vars(self): self.motionRecognizerArray: list[MotionRecognizer] = None
        if "TOTAL_MINUS_ONE" not in vars(self): self.TOTAL_MINUS_ONE: int = 0
    

    @staticmethod
    def getInstance() -> GameInputMotionEventProcessorAPI5:
        from org.allbinary.logic.NullUtil import NullUtil
        if GameInputMotionEventProcessorAPI5.instance == NullUtil.getInstance().NULL_OBJECT:
            GameInputMotionEventProcessorAPI5.instance = GameInputMotionEventProcessorAPI5()
        return GameInputMotionEventProcessorAPI5.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.android.input.motion.api5.GameInputMotionInfoAPI5 import GameInputMotionInfoAPI5
        from org.allbinary.input.motion.AllMotionRecognizer import AllMotionRecognizer
        super().__init__()
        __class__._init_fields(self)
        size: int = GameInputMotionInfoAPI5.getInstance().MAX_POINTERS
        self.motionRecognizerArray = [None] * (size)
        self.TOTAL_MINUS_ONE = size
        for index in range(0, size):
            self.motionRecognizerArray[index] = AllMotionRecognizer()
    

    def isValid(self, pointerId: int) -> bool:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        if pointerId > self.TOTAL_MINUS_ONE:
            message: str = "Log that the pointer Ids are not what would be expected or Android has more than what I set my stuff to support pointerId: "
            ForcedLogUtil.log(message + str(pointerId), self)
            return False
        else:
            return True
    

    def process(self, motionEvent: MotionEvent) -> None:
        from android.view.MotionEvent import MotionEvent
        from org.allbinary.graphics.displayable.ScalableListener import ScalableListener
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        try:
            action: int = motionEvent.getAction()
            total: int = len(self.motionRecognizerArray)
            if total > motionEvent.getPointerCount():
                total = motionEvent.getPointerCount()
            else:
                message: str = "Log that Android has more pointers than I have expected so increase it motionEvent.getPointerCount(): "
                ForcedLogUtil.log(message + str(motionEvent.getPointerCount()), self)
            totalMinusOne: int = total - 1
            if action == MotionEvent.ACTION_DOWN:
                for pointerIndex in range(totalMinusOne, 0 - 1, -1):
                    pointerId: int = motionEvent.getPointerId(pointerIndex)
                    if self.isValid(pointerId):
                        scalableListener: ScalableListener = self.displayInfo.getScalableListener()
                        x: int = int((java_divide((motionEvent.getX(pointerIndex) - self.displayInfo.getLeft()), scalableListener.getRatio(self.displayInfo.getRatio()))
            ))
                        y: int = int((java_divide((motionEvent.getY(pointerIndex) - self.displayInfo.getTop()), scalableListener.getRatio(self.displayInfo.getRatio()))
            ))
                        self.motionRecognizerArray[pointerId].processStartMotionEvent(x, y, motionEvent.getDeviceId(), 0)
            elif action == MotionEvent.ACTION_UP or action == MotionEvent.ACTION_CANCEL:
                for pointerIndex in range(totalMinusOne, 0 - 1, -1):
                    pointerId: int = motionEvent.getPointerId(pointerIndex)
                    if self.isValid(pointerId):
                        scalableListener: ScalableListener = self.displayInfo.getScalableListener()
                        x: int = int((java_divide((motionEvent.getX(pointerIndex) - self.displayInfo.getLeft()), scalableListener.getRatio(self.displayInfo.getRatio()))
            ))
                        y: int = int((java_divide((motionEvent.getY(pointerIndex) - self.displayInfo.getTop()), scalableListener.getRatio(self.displayInfo.getRatio()))
            ))
                        self.motionRecognizerArray[pointerId].processEndMotionEvent(x, y, motionEvent.getDeviceId(), 0)
            elif action == MotionEvent.ACTION_MOVE:
                for pointerIndex in range(totalMinusOne, 0 - 1, -1):
                    pointerId: int = motionEvent.getPointerId(pointerIndex)
                    if self.isValid(pointerId):
                        scalableListener: ScalableListener = self.displayInfo.getScalableListener()
                        x: int = int((java_divide((motionEvent.getX(pointerIndex) - self.displayInfo.getLeft()), scalableListener.getRatio(self.displayInfo.getRatio()))
            ))
                        y: int = int((java_divide((motionEvent.getY(pointerIndex) - self.displayInfo.getTop()), scalableListener.getRatio(self.displayInfo.getRatio()))
            ))
                        self.motionRecognizerArray[pointerId].processDraggedMotionEvent(x, y, motionEvent.getDeviceId(), 0)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
# from android.view.MotionEvent import MotionEvent
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.displayable.ScalableListener import ScalableListener
# from org.allbinary.input.motion.AllMotionRecognizer import AllMotionRecognizer
# from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _GameInputMotionEventProcessorAPI5_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(GameInputMotionEventProcessorAPI5, "instance", _GameInputMotionEventProcessorAPI5_instance)

