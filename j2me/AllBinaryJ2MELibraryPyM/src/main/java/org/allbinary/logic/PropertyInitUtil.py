# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.logic

from __future__ import annotations



class PropertyInitUtil:
    instance: PropertyInitUtil = None
    

    @staticmethod
    def getInstance(value: int) -> PropertyInitUtil:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil: LogUtil = LogUtil.getInstance()
        logUtil.putF(str(StringMaker().append("PropertyInitUtil: ").appendint(value)), logUtil, commonStrings.CONSTRUCTOR)
        return PropertyInitUtil.instance
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


PropertyInitUtil.instance = PropertyInitUtil()

