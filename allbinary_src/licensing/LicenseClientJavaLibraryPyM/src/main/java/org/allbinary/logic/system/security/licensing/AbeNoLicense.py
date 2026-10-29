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


class AbeNoLicense(AbeLicenseInterface):
    abeNoLicense: AbeNoLicense = None

    def _init_fields(self) -> None:
        self.serverVector: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AbeNoLicense:
        return AbeNoLicense.abeNoLicense
    

    def hasKey(self) -> bool:
        return False
    

    def getKey(self, keyName: str) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getLicenseId(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getSpecial(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def getServers(self) -> BasicArrayList:
        return self.serverVector
    

    def isValid(self) -> bool:
        return False
    

    def getLicenseType(self) -> LicenseType:
        from org.allbinary.logic.system.security.licensing.LicenseTypeFactory import LicenseTypeFactory
        return LicenseTypeFactory.getInstance().UNKNOWN
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


AbeNoLicense.abeNoLicense = AbeNoLicense()

