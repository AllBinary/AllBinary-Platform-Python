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
# package org.allbinary.game.configuration.feature

from __future__ import annotations



class SensorFeatureFactory:
    instance: SensorFeatureFactory = None

    def _init_fields(self) -> None:
        self.NO_ORIENTATION: SensorFeature = SensorFeature("No Orientation")
        self.ORIENTATION_SENSORS: SensorFeature = SensorFeature("Orientation Sensors")
        self.SIMULATED_ORIENTATION_SENSORS: SensorFeature = SensorFeature("Simulated Orientation Sensors")
        self.YAW: SensorFeature = SensorFeature("Yaw")
        self.YAW_MINUS_RIGHT_PLUS_LEFT: SensorFeature = SensorFeature("Yaw -Right +Left")
        self.YAW_MINUS_LEFT_PLUS_RIGHT: SensorFeature = SensorFeature("Yaw -Left +Right ")
        self.PITCH: SensorFeature = SensorFeature("Pitch")
        self.ROLL: SensorFeature = SensorFeature("Roll")
    

    @staticmethod
    def getInstance() -> SensorFeatureFactory:
        return SensorFeatureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.game.configuration.feature.SensorFeature import SensorFeature


SensorFeatureFactory.instance = SensorFeatureFactory()

