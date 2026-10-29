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
# package org.allbinary.logic.system.security.licensing.registration

from __future__ import annotations



class RegistrationConfiguration:
    SINGLETON: RegistrationConfiguration = None

    def _init_fields(self) -> None:
        self.registrationCode: str = "No Registration Code"
        self.NAME: str = "registrationid"
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RegistrationConfiguration:
        return RegistrationConfiguration.SINGLETON
    

    # throws Exception
    def read(self) -> None:
        pass
    

    # throws Exception
    def write(self) -> None:
        pass
    

    def toString(self) -> str:
        return str(StringMaker().append("Registration Code: ").append(self.getRegistrationCode()))

    def __str__(self) -> str:
        return self.toString()
    

    def setRegistrationCode(self, registrationCode: str) -> None:
        self.registrationCode = registrationCode
    

    def getRegistrationCode(self) -> str:
        return self.registrationCode
from org.allbinary.logic.string.StringMaker import StringMaker


RegistrationConfiguration.SINGLETON = RegistrationConfiguration()

