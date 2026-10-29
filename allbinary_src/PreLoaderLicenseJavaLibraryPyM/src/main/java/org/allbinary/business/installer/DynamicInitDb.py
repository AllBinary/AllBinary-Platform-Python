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
# package org.allbinary.business.installer

from __future__ import annotations

from org.allbinary.business.installer.InitDb import InitDb


#Warning you must have sql root access
class DynamicInitDb(InitDb):

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, abeClientInformation: AbeClientInformationInterface) -> None:
        super().__init__()
        self.setHelper(InitDbHelperFactory.getInstance(abeClientInformation))
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, databaseConnectionInfoInterface: DatabaseConnectionInfoInterface) -> None:
        super().__init__()
        self.setHelper(InitDbHelperFactory.getInstance(abeClientInformation, databaseConnectionInfoInterface))
from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
from org.allbinary.business.init.db.InitDbHelperFactory import InitDbHelperFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


