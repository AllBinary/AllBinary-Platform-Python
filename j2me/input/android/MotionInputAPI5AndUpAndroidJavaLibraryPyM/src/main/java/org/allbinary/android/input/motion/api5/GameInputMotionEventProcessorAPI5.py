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

from org.allbinary.android.input.motion.BaseGameInputMotionEventProcessor import BaseGameInputMotionEventProcessor
from org.allbinary.logic.NullUtil import NullUtil


class GameInputMotionEventProcessorAPI5(BaseGameInputMotionEventProcessor):
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.motionRecognizerArray: list[MotionRecognizer] = None
        self.TOTAL_MINUS_ONE: int = None
    

    @staticmethod
    def getInstance() -> GameInputMotionEventProcessorAPI5:
        if GameInputMotionEventProcessorAPI5.instance == NullUtil.getInstance().NULL_OBJECT:
            GameInputMotionEventProcessorAPI5.instance = GameInputMotionEventProcessorAPI5()
        return GameInputMotionEventProcessorAPI5.instance
    

    def __init__(self) -> None:
        from org.allbinary.android.input.motion.api5.GameInputMotionInfoAPI5 import GameInputMotionInfoAPI5
        super().__init__()
        self._init_fields()
        size: int = GameInputMotionInfoAPI5.getInstance().MAX_POINTERS
        self.motionRecognizerArray = [None] * (size)
        self.TOTAL_MINUS_ONE = size
        for index in range(0, size):
            self.motionRecognizerArray[index] = AllMotionRecognizer()
    

    def isValid(self, pointerId: int) -> bool:
        if pointerId > self.TOTAL_MINUS_ONE:
            message: str = "Log that the pointer Ids are not what would be expected or Android has more than what I set my stuff to support pointerId: "
            ForcedLogUtil.log(message + str(pointerId), self)
            return False
        else:
            return True
    

    def process(self, motionEvent: MotionEvent) -> None:
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
                        x: int = int(((motionEvent.getX(pointerIndex) - self.displayInfo.getLeft()) / scalableListener.getRatio(self.displayInfo.getRatio())))
                        y: int = int(((motionEvent.getY(pointerIndex) - self.displayInfo.getTop()) / scalableListener.getRatio(self.displayInfo.getRatio())))
                        self.motionRecognizerArray[pointerId].processStartMotionEvent(x, y, motionEvent.getDeviceId(), 0)
            elif action == MotionEvent.ACTION_UP or action == MotionEvent.ACTION_CANCEL:
                for pointerIndex in range(totalMinusOne, 0 - 1, -1):
                    pointerId: int = motionEvent.getPointerId(pointerIndex)
                    if self.isValid(pointerId):
                        scalableListener: ScalableListener = self.displayInfo.getScalableListener()
                        x: int = int(((motionEvent.getX(pointerIndex) - self.displayInfo.getLeft()) / scalableListener.getRatio(self.displayInfo.getRatio())))
                        y: int = int(((motionEvent.getY(pointerIndex) - self.displayInfo.getTop()) / scalableListener.getRatio(self.displayInfo.getRatio())))
                        self.motionRecognizerArray[pointerId].processEndMotionEvent(x, y, motionEvent.getDeviceId(), 0)
            elif action == MotionEvent.ACTION_MOVE:
                for pointerIndex in range(totalMinusOne, 0 - 1, -1):
                    pointerId: int = motionEvent.getPointerId(pointerIndex)
                    if self.isValid(pointerId):
                        scalableListener: ScalableListener = self.displayInfo.getScalableListener()
                        x: int = int(((motionEvent.getX(pointerIndex) - self.displayInfo.getLeft()) / scalableListener.getRatio(self.displayInfo.getRatio())))
                        y: int = int(((motionEvent.getY(pointerIndex) - self.displayInfo.getTop()) / scalableListener.getRatio(self.displayInfo.getRatio())))
                        self.motionRecognizerArray[pointerId].processDraggedMotionEvent(x, y, motionEvent.getDeviceId(), 0)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
from android.view.MotionEvent import MotionEvent
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.displayable.ScalableListener import ScalableListener
from org.allbinary.input.motion.AllMotionRecognizer import AllMotionRecognizer
from org.allbinary.input.motion.MotionRecognizer import MotionRecognizer
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


