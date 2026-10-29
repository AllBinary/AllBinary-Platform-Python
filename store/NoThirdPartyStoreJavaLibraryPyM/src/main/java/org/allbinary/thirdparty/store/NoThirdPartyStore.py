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
# package org.allbinary.thirdparty.store

from __future__ import annotations

from org.allbinary.thirdparty.store.ThirdPartyStore import ThirdPartyStore


class NoThirdPartyStore(ThirdPartyStore):
    

    def __init__(self) -> None:
        super().__init__(StringUtil.getInstance().EMPTY_STRING)
    

    def authorize(self, clientInformationInterface: AbeClientInformationInterface) -> None:
        self.setAuthorized(True)
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


