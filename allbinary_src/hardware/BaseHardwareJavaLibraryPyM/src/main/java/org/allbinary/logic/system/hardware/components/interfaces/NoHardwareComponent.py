# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.logic.system.hardware.components.interfaces

from __future__ import annotations

from org.allbinary.logic.system.hardware.components.interfaces.HardwareComponentInterface import HardwareComponentInterface


class NoHardwareComponent(HardwareComponentInterface):
    instance: NoHardwareComponent = None
    

    @staticmethod
    def getInstance() -> NoHardwareComponent:
        return NoHardwareComponent.instance
    

    def compareTo(self, componentInterface: HardwareComponentInterface) -> bool:
        if self == componentInterface:
            return True
        return False
    

    def toString(self) -> str:
        return StringUtil.getInstance().NULL_STRING

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringUtil import StringUtil


NoHardwareComponent.instance = NoHardwareComponent()

