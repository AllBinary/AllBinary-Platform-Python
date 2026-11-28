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

from java.lang.JavaRuntimeStatic import java_predicate
import datetime
from java.lang.JavaRuntimeStatic import lazy_static


class AbeLicenseInterfaceFactory:
    SINGLETON: AbeLicenseInterfaceFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
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
        __class__._init_fields(self)
    

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
        from org.allbinary.logic.system.security.licensing.client.AbeLicenseClient import AbeLicenseClient
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
            raise LicensingException("Unknown License Failure: " + __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self)))
    

    def isTimeToGetKey(self) -> bool:
        from org.allbinary.logic.system.security.licensing.AbeNoLicense import AbeNoLicense
        calendar: datetime.datetime = datetime.datetime.now()
        currentTime: int = calendar.getTimeInMillis()
        if self.abeLicenseInterface is None or self.abeLicenseInterface == AbeNoLicense.getInstance() or not (java_predicate(self.abeLicenseInterface, "hasKey")) or self.isCheck() or currentTime - self.checkPeriod > self.time:
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
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.client.AbeLicenseClient import AbeLicenseClient
# from org.allbinary.string.CommonStrings import CommonStrings


def _AbeLicenseInterfaceFactory_SINGLETON() -> object:
    return AbeLicenseInterfaceFactory()

lazy_static(AbeLicenseInterfaceFactory, "SINGLETON", _AbeLicenseInterfaceFactory_SINGLETON)

