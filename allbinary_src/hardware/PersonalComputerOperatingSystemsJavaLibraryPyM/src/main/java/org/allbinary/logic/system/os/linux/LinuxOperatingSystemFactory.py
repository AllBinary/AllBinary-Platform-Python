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
# package org.allbinary.logic.system.os.linux

from __future__ import annotations



class LinuxOperatingSystemFactory:
    instance: LinuxOperatingSystemFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> LinuxOperatingSystemFactory:
        return LinuxOperatingSystemFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getOperatingSystemInstance(self) -> GenericOperatingSystem:
        from org.allbinary.logic.system.os.linux.LinuxOS import LinuxOS
        from org.allbinary.logic.system.os.linux.LinuxOS import LinuxOS
        try:
            operatingSystems: OperatingSystems = OperatingSystems.getInstance()
            osName: str = SystemProperties.getInstance().getName()
            operatingSystemInterface: GenericOperatingSystem = None
            if ((osName > operatingSystems.LINUX) - (osName < operatingSystems.LINUX)) == 0:
                operatingSystemInterface = LinuxOS()
            else:
                if operatingSystems.isUnknownSpecificOSAllowed():
                    operatingSystemInterface = LinuxOS()
                else:
                    raise Exception("Specific Linux OS Not Supported: " + osName)
            return operatingSystemInterface
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return NoOperatingSystem.NO_OPERATING_SYSTEM
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem
from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
from org.allbinary.logic.system.os.SystemProperties import SystemProperties
from org.allbinary.string.CommonStrings import CommonStrings


LinuxOperatingSystemFactory.instance = LinuxOperatingSystemFactory()

