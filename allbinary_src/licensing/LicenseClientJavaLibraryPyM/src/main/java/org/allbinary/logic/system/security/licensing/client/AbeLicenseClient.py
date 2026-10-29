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
# package org.allbinary.logic.system.security.licensing.client

from __future__ import annotations

import threading


class AbeLicenseClient:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.MINSERVERS: int = 3
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def get(self, abeClientInformation: AbeClientInformationInterface) -> AbeLicenseInterface:
        with self._lock:
            return self._get_unlocked(abeClientInformation)

    def _get_unlocked(self, abeClientInformation: AbeClientInformationInterface) -> AbeLicenseInterface:
        from org.allbinary.logic.system.security.licensing.client.XmlRpcAbeLicenseRetrievalClient import XmlRpcAbeLicenseRetrievalClient
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.GET)
            xmlRpcAbeLicenseClient: XmlRpcAbeClient = XmlRpcAbeLicenseRetrievalClient(abeClientInformation)
            abeLicenseInterface: AbeLicenseInterface = xmlRpcAbeLicenseClient.get(None)
            licenseId: str = abeLicenseInterface.getLicenseId()
            servers: BasicArrayList = abeLicenseInterface.getServers()
            isNewLicenseId: bool = False
            isBetterServerList: bool = False
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if stringValidationUtil.isEmpty(abeClientInformation.getLicenseId()) and not abeClientInformation.isSameId(licenseId):
                isNewLicenseId = True
            if servers.size() >= self.MINSERVERS and abeClientInformation.isLargerOrDifferentServerList(servers):
                isBetterServerList = True
            if isBetterServerList or isNewLicenseId:
                initInfo: LicenseInitInfo = LicenseInitInfoUtil.getInstance().read()
                initInfo.setLicenseId(licenseId)
                initInfo.setServerList(servers)
                LicenseInitInfoUtil.getInstance().write(initInfo)
                abeClientInformation.init()
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.GET)
            return abeLicenseInterface
        except Exception as e:
            raise e
from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
from org.allbinary.business.init.LicenseInitInfoUtil import LicenseInitInfoUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.xmlrpc.XmlRpcAbeClient import XmlRpcAbeClient
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.AbeLicenseInterface import AbeLicenseInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


