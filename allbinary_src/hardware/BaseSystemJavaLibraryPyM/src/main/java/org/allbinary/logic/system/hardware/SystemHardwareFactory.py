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



class SystemHardwareFactory:
    instance: SystemHardwareFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.hardwareInterface: HardwareInterface = NoHardware.getInstance()
    

    @staticmethod
    def getInstance() -> SystemHardwareFactory:
        return SystemHardwareFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, operatingSystemInterface: GenericOperatingSystem) -> HardwareInterface:
        from org.allbinary.logic.system.hardware.NoHardware import NoHardware
        from org.allbinary.logic.system.hardware.HardwareFactory import HardwareFactory
        try:
            if self.hardwareInterface == NoHardware.getInstance():
                self.hardwareInterface = HardwareFactory.getInstance().getInstance(operatingSystemInterface)
            self.logUtil.putF("Found Hardware", self, self.commonStrings.CONSTRUCTOR)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
        return self.hardwareInterface
    

    @staticmethod
    def static_toString() -> str:
        systemHardwareFactory: SystemHardwareFactory = SystemHardwareFactory.getInstance()
        osBuffer: StringMaker = StringMaker()
        osBuffer.append("Hardware Info: \n")
        if systemHardwareFactory.hardwareInterface is not None:
            osBuffer.append(str(systemHardwareFactory.hardwareInterface))
        else:
            osBuffer.append(StringUtil.getInstance().NULL_STRING)
        return str(osBuffer)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.system.hardware.NoHardware import NoHardware


SystemHardwareFactory.instance = SystemHardwareFactory()

