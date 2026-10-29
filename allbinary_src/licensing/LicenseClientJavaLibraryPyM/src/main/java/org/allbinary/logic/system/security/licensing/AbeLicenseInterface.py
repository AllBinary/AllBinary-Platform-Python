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
class AbeLicenseInterface:
    

    def hasKey(self) -> bool:
        raise NotImplementedError()
    

    def getKey(self, keyName: str) -> str:
        raise NotImplementedError()
    

    def getLicenseId(self) -> str:
        raise NotImplementedError()
    

    def getServers(self) -> BasicArrayList:
        raise NotImplementedError()
    

    def getSpecial(self) -> str:
        raise NotImplementedError()
    

    def getLicenseType(self) -> LicenseType:
        raise NotImplementedError()
    

    def isValid(self) -> bool:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList


