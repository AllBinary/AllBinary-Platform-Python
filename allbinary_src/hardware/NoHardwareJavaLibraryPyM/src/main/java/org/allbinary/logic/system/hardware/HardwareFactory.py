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

    def _init_fields(self) -> None:
        self.SINGLETON: HardwareInterface = NoHardware.getInstance()
    

    @staticmethod
    def getInstance() -> HardwareFactory:
        return HardwareFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, os: OperatingSystemInterface) -> HardwareInterface:
        try:
            return self.SINGLETON
        except Exception as e:
            raise e
from org.allbinary.logic.system.os.OperatingSystemInterface import OperatingSystemInterface
from org.allbinary.logic.system.hardware.NoHardware import NoHardware


HardwareFactory.instance = HardwareFactory()

