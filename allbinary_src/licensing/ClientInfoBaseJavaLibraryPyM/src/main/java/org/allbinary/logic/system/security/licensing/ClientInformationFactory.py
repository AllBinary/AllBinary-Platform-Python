# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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



class ClientInformationFactory:
    

    def getInstance(self) -> ClientInformation:
        from org.allbinary.logic.system.security.licensing.ClientInformation import ClientInformation
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(commonStrings.NOT_IMPLEMENTED, self, commonStrings.GET_INSTANCE)
        stringUtil: StringUtil = StringUtil.getInstance()
        return ClientInformation(stringUtil.NULL_STRING, stringUtil.NULL_STRING, stringUtil.NULL_STRING, stringUtil.NULL_STRING)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


