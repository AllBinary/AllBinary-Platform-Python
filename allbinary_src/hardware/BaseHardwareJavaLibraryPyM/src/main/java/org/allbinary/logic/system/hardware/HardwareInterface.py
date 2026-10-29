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



# Java interface
class HardwareInterface:
    

    def getComponent(self, index: int) -> HardwareComponentInterface:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
    

    def compareTo(self, hardwareInterface: HardwareInterface) -> bool:
        raise NotImplementedError()
    

    def difference(self, hardwareInterface: HardwareInterface) -> ABHashtable[object, object]:
        raise NotImplementedError()
from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
from org.allbinary.util.ABHashtable import ABHashtable


