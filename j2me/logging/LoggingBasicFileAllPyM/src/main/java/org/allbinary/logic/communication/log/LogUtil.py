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
class LogUtil:
    instance: LogUtil = None
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def putL(self, log: Log) -> None:
        specialMessage: str = log.getSpecialMessage()
        anyType: object = log.getObject()
        functionName: str = log.getFunctionName()
        exception: object = log.getThrowable()
        self.put(specialMessage, anyType, functionName, exception)
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        FileLog.put(specialMessage, anyType, functionName)
    

    def putFS(self, specialMessage: str, className: str, functionName: str) -> None:
        FileLog.put(specialMessage, className, functionName)
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        FileLog.put(specialMessage, anyType, functionName, exception)
from org.allbinary.log.FileLog import FileLog
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker


LogUtil.instance = LogUtil()

