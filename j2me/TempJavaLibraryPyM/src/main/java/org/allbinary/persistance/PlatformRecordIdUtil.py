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
# package org.allbinary.persistance

from __future__ import annotations



class PlatformRecordIdUtil:
    instance: PlatformRecordIdUtil = None

    def _init_fields(self) -> None:
        self.PLATFORM_SHORT_NAME: str = "AVN"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PlatformRecordIdUtil:
        return PlatformRecordIdUtil.instance
    

    def getRecordId(self, abeClientInformation: AbeClientInformationInterface, baseRecordId: str) -> str:
        return str(StringMaker().append(abeClientInformation.toShortString()).append(CommonSeps.getInstance().UNDERSCORE).append(self.PLATFORM_SHORT_NAME).append(baseRecordId))
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


PlatformRecordIdUtil.instance = PlatformRecordIdUtil()

