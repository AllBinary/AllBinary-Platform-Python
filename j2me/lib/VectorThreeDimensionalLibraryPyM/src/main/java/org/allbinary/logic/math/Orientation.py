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
# package org.allbinary.logic.math

from __future__ import annotations



class Orientation:
    NONE: Orientation = None
    SINGLETON: Orientation = None

    def _init_fields(self) -> None:
        self.yaw: BasicDecimal = BasicDecimal(0)
        self.pitch: BasicDecimal = BasicDecimal(0)
        self.roll: BasicDecimal = BasicDecimal(0)
    

    @staticmethod
    def getInstance(yaw: int, pitch: int, roll: int) -> Orientation:
        Orientation.SINGLETON.yaw.setint(yaw)
        Orientation.SINGLETON.pitch.setint(pitch)
        Orientation.SINGLETON.roll.setint(roll)
        return Orientation.SINGLETON
    

    def __init__(self, yaw: int, pitch: int, roll: int) -> None:
        self._init_fields()
        self.yaw.setint(yaw)
        self.pitch.setint(pitch)
        self.roll.setint(roll)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Y: ")
        stringBuffer.append(str(self.yaw))
        stringBuffer.append(" P: ")
        stringBuffer.append(str(self.pitch))
        stringBuffer.append(" R: ")
        stringBuffer.append(str(self.roll))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.math.BasicDecimal import BasicDecimal


Orientation.NONE = Orientation(0, 0, 0)

Orientation.SINGLETON = Orientation(0, 0, 0)

