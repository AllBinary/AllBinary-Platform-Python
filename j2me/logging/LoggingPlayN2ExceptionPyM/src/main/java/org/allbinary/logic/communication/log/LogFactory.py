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
# package org.allbinary.logic.communication.log

from __future__ import annotations



#ActualPlatform
class LogFactory:
    

    @staticmethod
    def getInstance(specialMessage: str, anyType: object, functionName: str, exception: object) -> Log:
        from org.allbinary.logic.communication.log.Log import Log
        return Log(specialMessage, anyType, functionName, exception)
    

    @staticmethod
    def getInstanceF(specialMessage: str, anyType: object, functionName: str) -> Log:
        return None


