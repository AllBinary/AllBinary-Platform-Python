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

from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


# This is the information sent to the license server
class ClientInformation(AbeClientInformationInterface):

    def _init_fields(self) -> None:
        self.operatingSystemInterface: GenericOperatingSystem = NoOperatingSystem.NO_OPERATING_SYSTEM
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.name: str = None
        self.shortName: str = None
        self.version: str = None
        self.specialName: str = None
        self.hardSale: bool = True
        self.licenseId: str = StringUtil.getInstance().EMPTY_STRING
        self.licenseServers: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
    

    def __init__(self, name: str, version: str, specialName: str, shortName: str) -> None:
        self._init_fields()
        self.name = name
        self.version = version
        self.specialName = specialName
        self.shortName = str(StringMaker().append(shortName).append(CommonSeps.getInstance().UNDERSCORE).append(version))
        self.init()
    

    def init(self) -> None:
        pass
    

    def getOperatingSystemInterface(self) -> GenericOperatingSystem:
        return self.operatingSystemInterface
    

    def getName(self) -> str:
        return self.name
    

    def getSpecialName(self) -> str:
        return self.specialName
    

    def getVersion(self) -> str:
        return self.version
    

    def getLicenseId(self) -> str:
        return self.licenseId
    

    def getLicenseServers(self) -> BasicArrayList:
        return self.licenseServers
    

    def getLicenseServer(self, index: int) -> str:
        return self.licenseServers.objectArray[index]
    

    def getNumberOfLicenseServers(self) -> int:
        return self.licenseServers.size()
    

    def toHashtable(self) -> ABHashtable[object, object]:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationData import AbeClientInformationData
        abeClientInformationData: AbeClientInformationData = AbeClientInformationData.getInstance()
        genericOperatingSystem: GenericOperatingSystem = self.getOperatingSystemInterface()
        clientInfoHashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        clientInfoHashtable.put(abeClientInformationData.NAME, self.name)
        clientInfoHashtable.put(abeClientInformationData.VERSION, self.version)
        clientInfoHashtable.put(abeClientInformationData.SPECIALNAME, self.specialName)
        clientInfoHashtable.put(abeClientInformationData.LICENSEID, self.getLicenseId())
        clientInfoHashtable.put(abeClientInformationData.OSNAME, genericOperatingSystem.getName())
        clientInfoHashtable.put(abeClientInformationData.OSARCH, genericOperatingSystem.getArch())
        clientInfoHashtable.put(abeClientInformationData.OSVERSION, genericOperatingSystem.getVersion())
        clientInfoHashtable.put(abeClientInformationData.OS, str(genericOperatingSystem))
        hardwareInterface: HardwareInterface = SystemHardwareFactory.getInstance().getInstance(genericOperatingSystem)
        hardwareString: str = str(hardwareInterface)
        clientInfoHashtable.put(abeClientInformationData.HARDWARE, hardwareString)
        return clientInfoHashtable
    

    def isSameId(self, alicenseId: str) -> bool:
        if ((self.getLicenseId() > alicenseId) - (self.getLicenseId() < alicenseId)) == 0:
            return True
        else:
            return False
    

    def isLargerOrDifferentServerList(self, list_: BasicArrayList) -> bool:
        size: int = list_.size() - 1
        currentSize: int = self.licenseServers.size() - 1
        if size > currentSize:
            return True
        for index in range(size, 0 - 1, -1):
            newServerName: str = list_.objectArray[index]
            for index2 in range(currentSize, 0 - 1, -1):
                nextOldServerName: str = self.licenseServers.objectArray[index]
                if ((newServerName > nextOldServerName) - (newServerName < nextOldServerName)) != 0:
                    return True
        return False
    

    def setHardSale(self, hardSale: bool) -> None:
        self.hardSale = hardSale
    

    def isHardSale(self) -> bool:
        return self.hardSale
    

    def setOperatingSystemInterface(self, operatingSystemInterface: GenericOperatingSystem) -> None:
        self.operatingSystemInterface = operatingSystemInterface
    

    def setLicenseId(self, licenseId: str) -> None:
        self.licenseId = licenseId
    

    def setLicenseServers(self, licenseServers: BasicArrayList) -> None:
        self.licenseServers = licenseServers
    

    def toShortString(self) -> str:
        return self.shortName
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.hardware.HardwareInterface import HardwareInterface
from org.allbinary.logic.system.hardware.SystemHardwareFactory import SystemHardwareFactory
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.NoOperatingSystem import NoOperatingSystem
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


