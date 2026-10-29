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
# package org.allbinary.business.init.db

from __future__ import annotations



class InitDbHelperFactory:
    CLASSNAME: str = "org.allbinary.business.installer.InitDbCrypted"
    

    def __init__(self) -> None:
        pass
    

    # throws LicensingException
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, databaseConnectionInfoInterface: DatabaseConnectionInfoInterface) -> object:
        params: list[object] = [None] * (1)
        classes: list[type] = [None] * (1)
        classes[0] = DatabaseConnectionInfoInterface
        params[0] = databaseConnectionInfoInterface
        anyType: object = AbeFactory.getInstance().getInstance(abeClientInformation, InitDbHelperFactory.CLASSNAME, classes, params)
        return anyType
    

    # throws LicensingException
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface) -> object:
        anyType: object = AbeFactory.getInstance().getInstance(abeClientInformation, InitDbHelperFactory.CLASSNAME, None, None)
        return anyType
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


