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


class GyroSensorFactory:
    allBinaryGyroSensor: AllBinaryOrientationSensor = None
    

    # throws Exception
    @staticmethod
    def init() -> None:
        from org.allbinary.input.gyro.NoGyroSensor import NoGyroSensor
        GyroSensorFactory.allBinaryGyroSensor = NoGyroSensor()
    

    @staticmethod
    def getInstance() -> AllBinaryOrientationSensor:
        return GyroSensorFactory.allBinaryGyroSensor


def _GyroSensorFactory_allBinaryGyroSensor() -> object:
    from org.allbinary.input.gyro.AllBinaryOrientationSensor import AllBinaryOrientationSensor
    return AllBinaryOrientationSensor.NULL_ALLBINARY_ORIENTATION_SENSOR

lazy_static(GyroSensorFactory, "allBinaryGyroSensor", _GyroSensorFactory_allBinaryGyroSensor)

