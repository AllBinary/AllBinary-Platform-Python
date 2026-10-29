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
# package org.allbinary.logic.system.os.android

from __future__ import annotations



class AndroidOperatingSystemFactory:
    instance: AndroidOperatingSystemFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AndroidOperatingSystemFactory:
        return AndroidOperatingSystemFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getOperatingSystemInstance(self) -> GenericOperatingSystem:
        from org.allbinary.logic.system.os.android.AndroidOS import AndroidOS
        from org.allbinary.logic.system.os.android.AndroidOS import AndroidOS
        try:
            GenericOperatingSystem: GenericOperatingSystem = None
            systemProperties: SystemProperties = SystemProperties.getInstance()
            osName: str = systemProperties.getName()
            if ((osName > OperatingSystems.getInstance().ANDROID) - (osName < OperatingSystems.getInstance().ANDROID)) == 0:
                GenericOperatingSystem = AndroidOS()
            else:
                if OperatingSystems.getInstance().isUnknownSpecificOSAllowed():
                    GenericOperatingSystem = AndroidOS()
                else:
                    raise Exception("Specific Android OS Not Supported: " + osName)
            return GenericOperatingSystem
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put("Failed to get OperatingSystem returning NoOperatingSystem", self, commonStrings.GET_INSTANCE, e)
            return NoOperatingSystem.NO_OPERATING_SYSTEM
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem
from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
from org.allbinary.logic.system.os.SystemProperties import SystemProperties
from org.allbinary.string.CommonStrings import CommonStrings


AndroidOperatingSystemFactory.instance = AndroidOperatingSystemFactory()

