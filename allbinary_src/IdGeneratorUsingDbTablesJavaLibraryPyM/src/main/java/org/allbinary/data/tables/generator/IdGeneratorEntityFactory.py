# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.data.tables.generator

from __future__ import annotations



class IdGeneratorEntityFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> IdGeneratorEntityInterface:
        from org.allbinary.data.tables.generator.IdGeneratorEntity import IdGeneratorEntity
        try:
            return IdGeneratorEntity()
        except Exception as e:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, "ServerLicenseRequestEntityFactory", commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


