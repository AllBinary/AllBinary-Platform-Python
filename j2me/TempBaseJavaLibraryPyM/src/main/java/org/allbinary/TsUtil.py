# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary

from __future__ import annotations



#TempBase
class TsUtil:
    instance: TsUtil = None
    

    @staticmethod
    def getInstance() -> TsUtil:
        return TsUtil.instance
    

    def hashCode(self, anyType: object) -> int:
        return anyType.hashCode()
    

    # throws InterruptedException
    def waitFor(self, any: object, timeoutMillis: int) -> None:
        anyType: object = any
        anyType.wait(timeoutMillis)


TsUtil.instance = TsUtil()

