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



class HardwareFactory:
    instance: HardwareFactory = None
    

    @staticmethod
    def getInstance() -> HardwareFactory:
        return HardwareFactory.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(os: GenericOperatingSystem) -> HardwareInterface:
        try:
            operatingSystems: OperatingSystems = OperatingSystems.getInstance()
            if os.getName().compareTo(operatingSystems.LINUX) == 0:
                return LinuxHardware()
            elif os.getName().indexOf(operatingSystems.WINDOWS) >= 0:
                return WindowsHardware()
            raise Exception("No Hardware Imp for: " + os.getName())
        except Exception as e:
            raise e
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
from org.allbinary.logic.system.hardware.linux.LinuxHardware import LinuxHardware
from org.allbinary.logic.system.hardware.windows.WindowsHardware import WindowsHardware


HardwareFactory.instance = HardwareFactory()

