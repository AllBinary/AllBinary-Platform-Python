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

import datetime


class AbeLicenseInterfaceFactory:
    SINGLETON: AbeLicenseInterfaceFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.time: int = 0
        self.check: bool = False
        self.checkPeriod: int = 36000000
        self.abeLicenseInterface: AbeLicenseInterface = None
    

    @staticmethod
    def getInstance() -> AbeLicenseInterfaceFactory:
        return AbeLicenseInterfaceFactory.SINGLETON
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws LicensingException
    def getLicenseInstance(self, abeClientInformation: AbeClientInformationInterface) -> AbeLicenseInterface:
        if self.isTimeToGetKey():
            return self.get(abeClientInformation)
        else:
            return self.abeLicenseInterface
    

    # throws LicensingException
    def get(self, abeClientInformation: AbeClientInformationInterface) -> AbeLicenseInterface:
        from org.allbinary.logic.system.security.licensing.AbeNoLicense import AbeNoLicense
        from org.allbinary.logic.system.security.licensing.AbeClientInformationData import AbeClientInformationData
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        try:
            self.logUtil.putF("Getting Keys", self, self.commonStrings.GET)
            self.abeLicenseInterface = AbeNoLicense.getInstance()
            licenseClient: AbeLicenseClient = AbeLicenseClient()
            self.abeLicenseInterface = licenseClient.get(abeClientInformation)
            if self.abeLicenseInterface is not None:
                self.logUtil.putF("Default Key: " + str(self.abeLicenseInterface.getKey(AbeClientInformationData.getInstance().KEY)), self, self.commonStrings.GET)
            return self.abeLicenseInterface
        except OSError as e:
            self.logUtil.put("Licensing IO Error", self, self.commonStrings.GET, e)
            raise LicensingException("License Server Connection Error")
        except Exception as e:
            self.logUtil.put("Licensing Failure", self, self.commonStrings.GET, e)
            raise LicensingException("Unknown License Failure: " + type(self).__module__ + "." + type(self).__qualname__)
    

    def isTimeToGetKey(self) -> bool:
        from org.allbinary.logic.system.security.licensing.AbeNoLicense import AbeNoLicense
        calendar: datetime.datetime = datetime.datetime.now()
        currentTime: int = calendar.getTimeInMillis()
        if self.abeLicenseInterface is None or self.abeLicenseInterface == AbeNoLicense.getInstance() or not self.abeLicenseInterface.hasKey() or self.isCheck() or currentTime - self.checkPeriod > self.time:
            self.abeLicenseInterface = None
            self.time = currentTime
            return True
        else:
            return False
    

    def setCheck(self, check: bool) -> None:
        self.check = check
    

    def isCheck(self) -> bool:
        return self.check
# from java.io.IOException import IOException
# from java.util.Calendar import Calendar
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.client.AbeLicenseClient import AbeLicenseClient
from org.allbinary.string.CommonStrings import CommonStrings


AbeLicenseInterfaceFactory.SINGLETON = AbeLicenseInterfaceFactory()

