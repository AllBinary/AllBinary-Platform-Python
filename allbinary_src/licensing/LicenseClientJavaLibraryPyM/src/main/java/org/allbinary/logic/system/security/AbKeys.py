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
# package org.allbinary.logic.system.security

from __future__ import annotations

import threading


class AbKeys:
    instance: AbKeys = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AbKeys:
        return AbKeys.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws LicensingException
    def getKey(self, abeClientInformation: AbeClientInformationInterface, keyName: str) -> str:
        with self._lock:
            return self._getKey_unlocked(abeClientInformation, keyName)

    def _getKey_unlocked(self, abeClientInformation: AbeClientInformationInterface, keyName: str) -> str:
        try:
            self.logUtil.putF("Getting Key: " + keyName, self, "getKey")
            if ((keyName > "DirectX 8") - (keyName < "DirectX 8")) == 0 or ((keyName > "DirectX") - (keyName < "DirectX")) == 0 or ((keyName > "Low Level") - (keyName < "Low Level")) == 0 or ((keyName > "System Drivers") - (keyName < "System Drivers")) == 0:
                return "Temp For Input Library"
            return AbeLicenseInterfaceFactory.getInstance().getLicenseInstance(abeClientInformation).getKey(keyName)
        except LicensingException as e:
            raise e
        except Exception as e:
            self.logUtil.put("Licensing Failure", self, "getKey()", e)
            raise LicensingException("Unknown License Failure")
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.AbeLicenseInterfaceFactory import AbeLicenseInterfaceFactory
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


AbKeys.instance = AbKeys()

