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

from org.allbinary.logic.system.security.licensing.AbeClientInformation import AbeClientInformation


class MobileClientInformation(AbeClientInformation):
    DESC: str = "Mobile"
    ANDROID_DESC: str = None
    

    def __init__(self, name: str, version: str, specialName: str, shortName: str) -> None:
        from org.allbinary.logic.system.security.licensing.PartnerIdentifierFileUtil import PartnerIdentifierFileUtil
        super().__init__(name, version, str(StringMaker().append(specialName).append(CommonSeps.getInstance().SPACE).append(PartnerIdentifierFileUtil.getInstance().get())), shortName)
        string: str = self.getSpecialName()
        number: str = string[len(string) - 1:]
        if Integer.getInteger(number) is None:
            self.setHardSale(False)
        commonStrings: CommonStrings = CommonStrings.getInstance()
        if self.isHardSale():
            self.logUtil.putF("Use Hard Coded Selling", self, commonStrings.CONSTRUCTOR)
        else:
            self.logUtil.putF("Don't Use Hard Coded Selling", self, commonStrings.CONSTRUCTOR)
    

    def toHashtable(self) -> ABHashtable[object, object]:
        hashtable: ABHashtable[object, object] = super().toHashtable()
        registrationConfiguration: RegistrationConfiguration = RegistrationConfiguration.getInstance()
        hashtable.put(registrationConfiguration.NAME, registrationConfiguration.getRegistrationCode())
        return hashtable
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.registration.RegistrationConfiguration import RegistrationConfiguration
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


MobileClientInformation.ANDROID_DESC = "Android" + str(MobileClientInformation.DESC)

