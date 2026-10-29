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

    def _init_fields(self) -> None:
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        self.LABEL: str = "org.allbinary"
        self.LOG_SUCCESS: str = "org.allbinary: "
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def putL(self, log: Log) -> None:
        specialMessage: str = log.getSpecialMessage()
        anyType: object = log.getObject()
        functionName: str = log.getFunctionName()
        exception: object = log.getThrowable()
        if log is not None:
            self.put(specialMessage, anyType, functionName, exception)
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        pass
    

    def putFS(self, specialMessage: str, className: str, functionName: str) -> None:
        pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        className: str = self.LABEL
        className = type(anyType).__module__ + "." + type(anyType).__qualname__
        message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
        android.util.Log.i(self.LABEL, self.LOG_SUCCESS + message)
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


LogUtil.instance = LogUtil()

