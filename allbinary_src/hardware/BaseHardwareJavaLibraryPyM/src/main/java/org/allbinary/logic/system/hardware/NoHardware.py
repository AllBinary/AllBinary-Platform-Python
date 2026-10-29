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
# package org.allbinary.logic.system.hardware

from __future__ import annotations

from org.allbinary.logic.system.hardware.HardwareInterface import HardwareInterface


class NoHardware(HardwareInterface):
    instance: HardwareInterface = None
    

    @staticmethod
    def getInstance() -> HardwareInterface:
        return NoHardware.instance
    

    def getComponent(self, index: int) -> HardwareComponentInterface:
        return NoHardwareComponent.getInstance()
    

    def toString(self) -> str:
        return "No Hardware"

    def __str__(self) -> str:
        return self.toString()
    

    def compareTo(self, hardwareInterface: HardwareInterface) -> bool:
        return True
    

    def difference(self, hardwareInterface: HardwareInterface) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
from org.allbinary.logic.system.hardware.components.interfaces.NoHardwareComponent import NoHardwareComponent
from org.allbinary.util.ABHashtable import ABHashtable


NoHardware.instance = NoHardware()

