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
# package org.allbinary.input.magnetic.field

from __future__ import annotations

from org.allbinary.input.AllBinarySensorListener import AllBinarySensorListener
from org.allbinary.input.magnetic.field.AllBinaryMagneticFieldSensor import AllBinaryMagneticFieldSensor


class NoMagneticFieldSensor(AllBinaryMagneticFieldSensor, AllBinarySensorListener):

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def getOrientation(self) -> Orientation:
        return Orientation.NONE
    

    def onSensorChange(self) -> None:
        pass
from org.allbinary.logic.math.Orientation import Orientation


