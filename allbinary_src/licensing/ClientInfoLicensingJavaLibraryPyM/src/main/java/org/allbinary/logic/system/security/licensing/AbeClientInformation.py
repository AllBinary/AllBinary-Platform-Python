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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations

from org.allbinary.logic.system.security.licensing.ClientInformation import ClientInformation


# This is the information sent to the license server
class AbeClientInformation(ClientInformation):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, name: str, version: str, specialName: str, shortName: str) -> None:
        super().__init__(name, version, specialName, shortName)
        self._init_fields()
    

    def init(self) -> None:
        try:
            self.setOperatingSystemInterface(OperatingSystemFactory.getInstance().getOperatingSystemInstance())
            licenseInitInfo: LicenseInitInfo = LicenseInitInfoUtil.getInstance().read()
            self.setLicenseId(licenseInitInfo.getLicenseId())
            self.setLicenseServers(licenseInitInfo.getServerList())
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if stringValidationUtil.isEmpty(self.getLicenseId()):
                NONE: str = "No License Id"
                self.setLicenseId(NONE)
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.put(str(StringMaker().append("Special Name: ").append(self.getSpecialName())), self, commonStrings.CONSTRUCTOR)
        except Exception as e:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.string.CommonStrings import CommonStrings


