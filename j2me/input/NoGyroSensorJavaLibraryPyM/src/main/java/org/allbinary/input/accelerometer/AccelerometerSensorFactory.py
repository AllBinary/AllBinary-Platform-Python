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
# package org.allbinary.input.accelerometer

from __future__ import annotations

from org.allbinary.input.gyro.AllBinaryOrientationSensor import AllBinaryOrientationSensor


class AccelerometerSensorFactory:
    allBinaryAccelerometerSensor: AllBinaryOrientationSensor = AllBinaryOrientationSensor.NULL_ALLBINARY_ORIENTATION_SENSOR
    

    # throws Exception
    @staticmethod
    def init() -> None:
        from org.allbinary.input.accelerometer.NoAccelerometerSensor import NoAccelerometerSensor
        features: Features = Features.getInstance()
        sensorFeatureFactory: SensorFeatureFactory = SensorFeatureFactory.getInstance()
        if features.isFeature(sensorFeatureFactory.ORIENTATION_SENSORS):
            raise Exception("No Orientation Sensors")
        elif features.isFeature(sensorFeatureFactory.SIMULATED_ORIENTATION_SENSORS):
            raise Exception("No Simulation Sensors")
        elif features.isFeature(sensorFeatureFactory.NO_ORIENTATION):
            AccelerometerSensorFactory.allBinaryAccelerometerSensor = NoAccelerometerSensor()
        else:
            raise Exception("Not Such SensorFeature")
    

    @staticmethod
    def getInstance() -> AllBinaryOrientationSensor:
        return AccelerometerSensorFactory.allBinaryAccelerometerSensor
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory


