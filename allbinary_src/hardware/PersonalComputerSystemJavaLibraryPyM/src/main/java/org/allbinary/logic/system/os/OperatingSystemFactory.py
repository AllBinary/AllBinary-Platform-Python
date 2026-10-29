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
# package org.allbinary.logic.system.os

from __future__ import annotations

import threading


class OperatingSystemFactory:
    instance: OperatingSystemFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.genericOperatingSystem: GenericOperatingSystem = NoOperatingSystem.NO_OPERATING_SYSTEM
        self.hasDetected: bool = False
    

    @staticmethod
    def getInstance() -> OperatingSystemFactory:
        return OperatingSystemFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getOperatingSystemInstance(self) -> GenericOperatingSystem:
        with self._lock:
            return self._getOperatingSystemInstance_unlocked()

    def _getOperatingSystemInstance_unlocked(self) -> GenericOperatingSystem:
        from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
        from org.allbinary.logic.system.os.SystemProperties import SystemProperties
        from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem
        try:
            operatingSystems: OperatingSystems = OperatingSystems.getInstance()
            systemProperties: SystemProperties = SystemProperties.getInstance()
            osName: str = systemProperties.getName()
            osArch: str = systemProperties.getArch()
            osVersion: str = systemProperties.getVersion()
            if not self.hasDetected:
                self.logUtil.putF("osName: " + osName, self, self.commonStrings.GET_INSTANCE)
                self.hasDetected = True
                if osName.find(operatingSystems.LINUX) >= 0:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
                        self.logUtil.putF("Found a Linux OS", self, self.commonStrings.GET_INSTANCE)
                    self.genericOperatingSystem = LinuxOperatingSystemFactory.getInstance().getOperatingSystemInstance()
                elif osName.find(operatingSystems.WINDOWS) >= 0:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
                        self.logUtil.putF("Found a Windows OS", self, self.commonStrings.GET_INSTANCE)
                    self.genericOperatingSystem = WindowsOperatingSystemFactory.getInstance().getOperatingSystemInstance()
                elif osName.find(operatingSystems.SOLARIS) >= 0:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
                        self.logUtil.putF("Found a Solaris OS", self, self.commonStrings.GET_INSTANCE)
                    self.genericOperatingSystem = SolarisOperatingSystemFactory.getInstance().getOperatingSystemInstance()
                else:
                    raise Exception(str(StringMaker().append("OS Not Supported: ").append(osName)))
                log: Log = LogFactory.getInstanceF(str(StringMaker().append("OperatingSystem Info: ").append(StringUtil.getInstance().toString(self.genericOperatingSystem))), self, self.commonStrings.GET_INSTANCE)
                print(str(log))
                self.logUtil.putL(log)
            return self.genericOperatingSystem
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            return NoOperatingSystem.NO_OPERATING_SYSTEM
from org.allbinary.logic.communication.log.Log import Log
from org.allbinary.logic.communication.log.LogFactory import LogFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.os.linux.LinuxOperatingSystemFactory import LinuxOperatingSystemFactory
from org.allbinary.logic.system.os.solaris.SolarisOperatingSystemFactory import SolarisOperatingSystemFactory
from org.allbinary.logic.system.os.windows.WindowsOperatingSystemFactory import WindowsOperatingSystemFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem


OperatingSystemFactory.instance = OperatingSystemFactory()

