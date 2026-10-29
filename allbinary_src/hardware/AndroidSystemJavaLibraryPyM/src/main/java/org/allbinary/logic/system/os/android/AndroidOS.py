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

from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem


class AndroidOS(GenericOperatingSystem):

    def _init_fields(self) -> None:
        self.stringBuffer: StringMaker = StringMaker()
        self.DEVICE_ID: str = "DeviceId"
        self.DEVICE_SOFTWARE_VERSION: str = "DeviceSoftwareVersion"
        self.LINE_1_NUMBER: str = "Line1Number"
        self.OUYA: str = "ouya"
    

    def __init__(self) -> None:
        from org.allbinary.logic.system.os.android.AndroidSystemProperties import AndroidSystemProperties
        super().__init__()
        self._init_fields()
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        if SDK_VERSION > 10:
            self.scalable = True
        properties: AndroidSystemProperties = AndroidSystemProperties.getInstance()
        commonStrings: CommonSeps = CommonSeps.getInstance()
        self.stringBuffer.append(self.DEVICE_ID)
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getDeviceId())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append(self.DEVICE_SOFTWARE_VERSION)
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getDeviceSoftwareVersion())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append(self.LINE_1_NUMBER)
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getLine1Number())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("NetworkCountryIso")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getNetworkCountryIso())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("NetworkOperator")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getNetworkOperator())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("NetworkOperatorName")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getNetworkOperatorName())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("NetworkType")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.appendint(int(properties.getNetworkType()))
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("PhoneType")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.appendint(int(properties.getPhoneType()))
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("SimCountryIso")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getSimCountryIso())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("SimOperator")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getSimOperator())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("SimOperatorName")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getSimOperatorName())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("SimSerialNumber")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getSimSerialNumber())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("SubscriberId")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getSubscriberId())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("VoiceMailAlphaTag")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getVoiceMailAlphaTag())
        self.stringBuffer.append(commonStrings.SPACE)
        self.stringBuffer.append("VoiceMailNumber")
        self.stringBuffer.append(commonStrings.EQUALS)
        self.stringBuffer.append(properties.getVoiceMailNumber())
        self.stringBuffer.append(commonStrings.SPACE)
    

    def isOverScan(self) -> bool:
        from org.allbinary.logic.system.os.android.AndroidSystemProperties import AndroidSystemProperties
        properties: AndroidSystemProperties = AndroidSystemProperties.getInstance()
        if properties.getDevice().toLowerCase().find(self.OUYA) >= 0:
            return True
        return False
    

    def getOverScanXPercent(self) -> int:
        return 90
    

    def getOverScanYPercent(self) -> int:
        return 90
    

    def toString(self) -> str:
        osBuffer: StringMaker = StringMaker()
        osBuffer.append(str(super()))
        osBuffer.append(CommonSeps.getInstance().SPACE)
        osBuffer.append("Other System Info: \n")
        osBuffer.append(str(self.stringBuffer))
        return str(osBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.android.AndroidInfoFactory import AndroidInfoFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


