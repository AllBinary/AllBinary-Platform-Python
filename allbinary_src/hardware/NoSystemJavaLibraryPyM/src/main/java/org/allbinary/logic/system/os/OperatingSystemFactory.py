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
    

    @staticmethod
    def getInstance() -> OperatingSystemFactory:
        return OperatingSystemFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getOperatingSystemInstance(self) -> GenericOperatingSystem:
        with self._lock:
            return self._getOperatingSystemInstance_unlocked()

    def _getOperatingSystemInstance_unlocked(self) -> GenericOperatingSystem:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            osString: str = str(StringMaker().append("OperatingSystem Info: ").append(str(self.genericOperatingSystem)))
            print(osString)
            self.logUtil.putF(osString, self, commonStrings.GET_INSTANCE)
        except Exception as e:
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
        return self.genericOperatingSystem
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem


OperatingSystemFactory.instance = OperatingSystemFactory()

