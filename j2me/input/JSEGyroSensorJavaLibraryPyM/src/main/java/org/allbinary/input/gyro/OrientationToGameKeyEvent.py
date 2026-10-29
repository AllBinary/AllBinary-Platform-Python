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



class OrientationToGameKeyEvent:

    def _init_fields(self) -> None:
        self.allBinaryGyroSensor: AllBinaryOrientationSensor = None
        self.MIN: int = 15
    

    def __init__(self) -> None:
        from org.allbinary.input.gyro.NoGyroSensor import NoGyroSensor
        self._init_fields()
        if Features.getInstance().isFeature(SensorFeatureFactory.getInstance().NO_ORIENTATION):
            self.allBinaryGyroSensor = NoGyroSensor()
        else:
            raise Exception("Not Such Feature")
    

    def setAllBinaryGyroSensor(self, allBinaryGyroSensor: AllBinaryOrientationSensor) -> None:
        self.allBinaryGyroSensor = allBinaryGyroSensor
    

    def getAllBinaryGyroSensor(self) -> AllBinaryOrientationSensor:
        return self.allBinaryGyroSensor
    

    # throws Exception
    def process(self) -> None:
        pass
    

    # throws Exception
    def updateGameKeyEvents(self, orientation: Orientation, yaw: int, pitch: int, roll: int) -> None:
        pass
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory
from org.allbinary.logic.math.Orientation import Orientation


