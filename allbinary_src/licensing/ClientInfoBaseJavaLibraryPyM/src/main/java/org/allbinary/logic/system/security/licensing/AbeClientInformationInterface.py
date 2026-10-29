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



# Java interface
class AbeClientInformationInterface:
    

    def init(self) -> None:
        raise NotImplementedError()
    

    def getOperatingSystemInterface(self) -> GenericOperatingSystem:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getSpecialName(self) -> str:
        raise NotImplementedError()
    

    def getVersion(self) -> str:
        raise NotImplementedError()
    

    def getLicenseId(self) -> str:
        raise NotImplementedError()
    

    def getLicenseServers(self) -> BasicArrayList:
        raise NotImplementedError()
    

    def getLicenseServer(self, index: int) -> str:
        raise NotImplementedError()
    

    def getNumberOfLicenseServers(self) -> int:
        raise NotImplementedError()
    

    def toHashtable(self) -> ABHashtable[object, object]:
        raise NotImplementedError()
    

    def isSameId(self, alicenseId: str) -> bool:
        raise NotImplementedError()
    

    def isLargerOrDifferentServerList(self, vector: BasicArrayList) -> bool:
        raise NotImplementedError()
    

    def isHardSale(self) -> bool:
        raise NotImplementedError()
    

    def toShortString(self) -> str:
        raise NotImplementedError()
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


