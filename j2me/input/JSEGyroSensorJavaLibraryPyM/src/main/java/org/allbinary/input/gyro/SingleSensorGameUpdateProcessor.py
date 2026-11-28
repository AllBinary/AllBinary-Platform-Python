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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.input.gyro.SensorGameUpdateProcessor import SensorGameUpdateProcessor


@java_inherited_overloads
class SingleSensorGameUpdateProcessor(SensorGameUpdateProcessor):
    def _java_defaults(self):
        vars(self).setdefault("accelerometerSensorUpdateProcessor", None)
        vars(self).setdefault("gyroSensorUpdateProcessor", None)

    def _init_fields(self) -> None:
        self.accelerometerSensorUpdateProcessor: Processor = AccelerometerSensorUpdateProcessor()
        self.gyroSensorUpdateProcessor: Processor = GyroSensorUpdateProcessor()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws Exception
    def process(self, anyType: object) -> None:
        self.setNoSensors()
    

    # throws Exception
    def sendNotifications(self, anyType: object) -> None:
        pass
# from org.allbinary.canvas.Processor import Processor
from org.allbinary.input.gyro.AccelerometerSensorUpdateProcessor import AccelerometerSensorUpdateProcessor
from org.allbinary.input.gyro.GyroSensorUpdateProcessor import GyroSensorUpdateProcessor


