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
# package org.allbinary.input.gyro

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.input.AllBinarySensor import AllBinarySensor


class AllBinaryOrientationSensor(AllBinarySensor):
    NULL_ALLBINARY_ORIENTATION_SENSOR: AllBinaryOrientationSensor = None

    def _init_fields(self) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEventListenerInterface import CompleteMotionGestureInputEventListenerInterface
        from org.allbinary.game.input.motion.action.NoCompleteMotionGestureInputEventListener import NoCompleteMotionGestureInputEventListener
        from org.allbinary.logic.math.PrimitiveFloatUtil import PrimitiveFloatUtil
        self.sensorDataFloatArray: list[float] = PrimitiveFloatUtil.getArrayInstance()
        self.listener: CompleteMotionGestureInputEventListenerInterface = NoCompleteMotionGestureInputEventListener.getInstance()
    

    def setCompleteMotionGestureInputEventListener(self, completeMotionGestureInputEventListenerInterface: CompleteMotionGestureInputEventListenerInterface) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEventListenerInterface import CompleteMotionGestureInputEventListenerInterface
        self.listener = completeMotionGestureInputEventListenerInterface
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def getOrientation(self) -> Orientation:
        from org.allbinary.logic.math.Orientation import Orientation
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
# from org.allbinary.game.input.CompleteMotionGestureInputEventListenerInterface import CompleteMotionGestureInputEventListenerInterface
# from org.allbinary.game.input.motion.action.NoCompleteMotionGestureInputEventListener import NoCompleteMotionGestureInputEventListener
# from org.allbinary.logic.math.Orientation import Orientation
# from org.allbinary.logic.math.PrimitiveFloatUtil import PrimitiveFloatUtil


def _AllBinaryOrientationSensor_NULL_ALLBINARY_ORIENTATION_SENSOR() -> object:
    return AllBinaryOrientationSensor()

lazy_static(AllBinaryOrientationSensor, "NULL_ALLBINARY_ORIENTATION_SENSOR", _AllBinaryOrientationSensor_NULL_ALLBINARY_ORIENTATION_SENSOR)

