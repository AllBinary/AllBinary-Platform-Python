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

from org.allbinary.canvas.Processor import Processor


class AccelerometerSensorUpdateProcessor(Processor):

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def process(self) -> None:
        sensorFeatureFactory: SensorFeatureFactory = SensorFeatureFactory.getInstance()
        if Features.getInstance().isFeature(sensorFeatureFactory.ORIENTATION_SENSORS):
            AccelerometerSensorFactory.getInstance().setCompleteMotionGestureInputEventListener(SingleKeyPressGameKeyFromMotionGestureEventListener())
        elif Features.getInstance().isFeature(sensorFeatureFactory.SIMULATED_ORIENTATION_SENSORS):
            AccelerometerSensorFactory.getInstance().setCompleteMotionGestureInputEventListener(SingleKeyPressGameKeyFromMotionGestureEventListener())
        elif Features.getInstance().isFeature(sensorFeatureFactory.NO_ORIENTATION):
            AccelerometerSensorFactory.getInstance().setCompleteMotionGestureInputEventListener(NoCompleteMotionGestureInputEventListener.getInstance())
        else:
            raise Exception("Sensor Feature Not Set")
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory
from org.allbinary.game.input.motion.action.NoCompleteMotionGestureInputEventListener import NoCompleteMotionGestureInputEventListener
from org.allbinary.game.input.motion.action.SingleKeyPressGameKeyFromMotionGestureEventListener import SingleKeyPressGameKeyFromMotionGestureEventListener
from org.allbinary.input.accelerometer.AccelerometerSensorFactory import AccelerometerSensorFactory


