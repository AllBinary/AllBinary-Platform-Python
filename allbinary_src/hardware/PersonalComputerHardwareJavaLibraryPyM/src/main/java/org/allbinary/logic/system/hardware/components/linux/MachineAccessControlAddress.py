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
# package org.allbinary.logic.system.hardware.components.linux

from __future__ import annotations

from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface
from org.allbinary.logic.system.hardware.components.interfaces.MachineAccessControlAddressInterface import MachineAccessControlAddressInterface


class MachineAccessControlAddress(HardwareComponentInterface, MachineAccessControlAddressInterface):
    

    def __init__(self) -> None:
        pass
    

    def compareTo(self, componentInterface: HardwareComponentInterface) -> bool:
        return True
    

    def toString(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringUtil import StringUtil


