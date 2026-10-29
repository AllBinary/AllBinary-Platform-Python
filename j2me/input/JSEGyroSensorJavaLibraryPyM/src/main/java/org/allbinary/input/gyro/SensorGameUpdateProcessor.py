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



class SensorGameUpdateProcessor:

    def _init_fields(self) -> None:
        self.inputSensor: AllBinarySensor = None

    def __init__(self) -> None:
        self._init_fields()
    

    def setInputSensor(self, inputSensor: AllBinarySensor) -> None:
        self.inputSensor = inputSensor
    

    def getInputSensor(self) -> AllBinarySensor:
        return self.inputSensor
    

    # throws Exception
    def process(self, anyType: object) -> None:
        pass
    

    # throws Exception
    def sendNotifications(self, anyType: object) -> None:
        pass
    

    def isAnySensor(self) -> bool:
        if self.inputSensor == NoAllBinarySensor.getInstance():
            return False
        else:
            return True
    

    def setNoSensors(self) -> None:
        from org.allbinary.input.gyro.GyroSensorFactory import GyroSensorFactory
        GyroSensorFactory.getInstance().setCompleteMotionGestureInputEventListener(NoCompleteMotionGestureInputEventListener.getInstance())
        AccelerometerSensorFactory.getInstance().setCompleteMotionGestureInputEventListener(NoCompleteMotionGestureInputEventListener.getInstance())
        self.setInputSensor(NoAllBinarySensor.getInstance())
from org.allbinary.game.input.motion.action.NoCompleteMotionGestureInputEventListener import NoCompleteMotionGestureInputEventListener
from org.allbinary.input.AllBinarySensor import AllBinarySensor
from org.allbinary.input.NoAllBinarySensor import NoAllBinarySensor
from org.allbinary.input.accelerometer.AccelerometerSensorFactory import AccelerometerSensorFactory


