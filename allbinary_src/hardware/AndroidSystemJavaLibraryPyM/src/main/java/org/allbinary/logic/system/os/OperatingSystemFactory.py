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
        from org.allbinary.logic.system.os.SystemProperties import SystemProperties
        from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
        from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
        from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            systemProperties: SystemProperties = SystemProperties.getInstance()
            osName: str = systemProperties.getName()
            if not self.hasDetected:
                self.hasDetected = True
                if osName.find(OperatingSystems.getInstance().ANDROID) >= 0:
                    self.logUtil.putF("Found a Android OS", self, commonStrings.GET_INSTANCE)
                    self.genericOperatingSystem = AndroidOperatingSystemFactory.getInstance().getOperatingSystemInstance()
                    self.logUtil.putF(str(StringMaker().append("Operating System Info: ").append(str(self.genericOperatingSystem))), self, commonStrings.GET_INSTANCE)
                elif osName.find(OperatingSystems.getInstance().HARMONY) >= 0:
                    self.logUtil.putF("Found a Harmony OS", self, commonStrings.GET_INSTANCE)
                    self.genericOperatingSystem = AndroidOperatingSystemFactory.getInstance().getOperatingSystemInstance()
                    self.logUtil.putF(str(StringMaker().append("Operating System Info: ").append(str(self.genericOperatingSystem))), self, commonStrings.GET_INSTANCE)
                else:
                    raise Exception(str(StringMaker().append("OS Not Supported: ").append(osName)))
        except Exception as e:
            self.genericOperatingSystem = NoOperatingSystem.NO_OPERATING_SYSTEM
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
        return self.genericOperatingSystem
from org.allbinary.logic.system.os.android.AndroidOperatingSystemFactory import AndroidOperatingSystemFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem


OperatingSystemFactory.instance = OperatingSystemFactory()

