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

from org.allbinary.logic.system.security.licensing.AbeLicenseInterface import AbeLicenseInterface


class AbeClientLicense(AbeLicenseInterface):

    def _init_fields(self) -> None:
        self.hashtable: ABHashtable[object, object] = None
        self.id: str = None
        self.servers: BasicArrayList = None
        self.special: str = None
        self.licenseType: LicenseType = None
    

    def __init__(self, hashtable: ABHashtable[object, object]) -> None:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationData import AbeClientInformationData
        from org.allbinary.logic.system.security.licensing.LicenseTypeFactory import LicenseTypeFactory
        self._init_fields()
        self.hashtable = StdUtil.getInstance().createHashtable()
        abeClientInformationData: AbeClientInformationData = AbeClientInformationData.getInstance()
        keyValue: object = hashtable.get(abeClientInformationData.KEY)
        if keyValue is not None:
            if isinstance(keyValue, str):
                self.hashtable.put(abeClientInformationData.KEY, keyValue)
        self.id = hashtable.get(abeClientInformationData.LICENSEID)
        vector: BasicArrayList = hashtable.get(abeClientInformationData.LICENSESERVERS)
        self.servers = BasicArrayListD()
        size: int = vector.size()
        for index in range(0, size):
            self.servers.add(vector.get(index))
        stringUtil: StringUtil = StringUtil.getInstance()
        self.setSpecial(stringUtil.getNonNull(hashtable.get(abeClientInformationData.SPECIAL)))
        licenseTypeString: str = stringUtil.getNonNull(hashtable.get(abeClientInformationData.LICENSE_TYPE))
        self.licenseType = LicenseTypeFactory.getInstance().getInstance(licenseTypeString)
    

    @staticmethod
    def hasRequiredKeys(resultHashtable: ABHashtable[object, object]) -> bool:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationData import AbeClientInformationData
        abeClientInformationData: AbeClientInformationData = AbeClientInformationData.getInstance()
        if resultHashtable.containsKey(abeClientInformationData.LICENSEID) and resultHashtable.containsKey(abeClientInformationData.LICENSESERVERS) and resultHashtable.containsKey(abeClientInformationData.KEY) and resultHashtable.containsKey(abeClientInformationData.LICENSE_TYPE):
            return True
        else:
            return False
    

    def hasKey(self) -> bool:
        return self.isValid()
    

    def getKey(self, keyName: str) -> str:
        return self.hashtable.get(keyName)
    

    def getLicenseId(self) -> str:
        return self.id
    

    def getServers(self) -> BasicArrayList:
        return self.servers
    

    def isValid(self) -> bool:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationData import AbeClientInformationData
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if not stringValidationUtil.isEmpty(self.getKey(AbeClientInformationData.getInstance().KEY)):
            return True
        return False
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        BREAK: str = "<br/>"
        stringBuffer.append("License Id: ")
        stringBuffer.append(self.getLicenseId())
        stringBuffer.append(BREAK)
        stringBuffer.append("Is Valid: ")
        stringBuffer.appendboolean(self.isValid())
        stringBuffer.append(BREAK)
        stringBuffer.append("Keys: ")
        stringBuffer.append(str(self.hashtable))
        stringBuffer.append(BREAK)
        serverVector: BasicArrayList = self.getServers()
        size: int = serverVector.size()
        for index in range(0, size):
            nextServerString: str = serverVector.get(index)
            stringBuffer.append("Server: ")
            stringBuffer.append(nextServerString)
            stringBuffer.append(BREAK)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def setSpecial(self, special: str) -> None:
        self.special = special
    

    def getSpecial(self) -> str:
        return self.special
    

    def getLicenseType(self) -> LicenseType:
        return self.licenseType
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


