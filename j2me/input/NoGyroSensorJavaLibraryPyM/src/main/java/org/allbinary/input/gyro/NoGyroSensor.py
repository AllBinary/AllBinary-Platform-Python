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

from org.allbinary.input.AllBinarySensorListener import AllBinarySensorListener
from org.allbinary.input.gyro.AllBinaryOrientationSensor import AllBinaryOrientationSensor


class NoGyroSensor(AllBinaryOrientationSensor, AllBinarySensorListener):
    

    def __init__(self) -> None:
        super().__init__()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def getOrientation(self) -> Orientation:
        return Orientation.NONE
    

    def onSensorChange(self) -> None:
        pass
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.Orientation import Orientation


