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



class AbeClientInformationData:
    instance: AbeClientInformationData = None

    def _init_fields(self) -> None:
        self.KEY: str = "KEY"
        self.NAME: str = "NAME"
        self.VERSION: str = "VERSION"
        self.SPECIALNAME: str = "SPECIALNAME"
        self.LICENSEID: str = "LICENSEID"
        self.LICENSE_TYPE: str = "LICENSETYPE"
        self.PREVIOUSLICENSEID: str = "PREVIOUSLICENSEID"
        self.OSNAME: str = "OSNAME"
        self.OSARCH: str = "OSARCH"
        self.OSVERSION: str = "OSVERSION"
        self.OS: str = "OS"
        self.HARDWARE: str = "HARDWARE"
        self.LICENSESERVERS: str = "LICENSESERVERS"
        self.NEWLICENSE: str = "NEWLICENSE"
        self.ISNEW: str = "ISNEW"
        self.SPECIAL: str = "SPECIAL"
    

    @staticmethod
    def getInstance() -> AbeClientInformationData:
        return AbeClientInformationData.instance
    

    def __init__(self) -> None:
        self._init_fields()


AbeClientInformationData.instance = AbeClientInformationData()

