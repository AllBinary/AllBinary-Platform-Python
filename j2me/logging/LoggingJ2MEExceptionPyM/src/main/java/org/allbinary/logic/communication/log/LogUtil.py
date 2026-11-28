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

from java.lang.System import System
from java.lang.JavaRuntimeStatic import lazy_static


#ActualPlatform
class LogUtil:
    instance: LogUtil = None

    def _init_fields(self) -> None:
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        self.LOG_SUCCESS: str = "org.allbinary: "
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def putL(self, log: Log) -> None:
        from org.allbinary.logic.communication.log.LogFactory import LogFactory
        if log == LogFactory.LOG:
            return
        exception: object = log.getThrowable()
        if exception is None:
            return
        specialMessage: str = log.getSpecialMessage()
        anyType: object = log.getObject()
        functionName: str = log.getFunctionName()
        self.put(specialMessage, anyType, functionName, exception)
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        pass
    

    def putFS(self, specialMessage: str, className: str, functionName: str) -> None:
        pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        className: str = CommonStrings.getInstance().EMPTY
        if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)) is not None:
            className = str(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)))
        message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
        print(self.LOG_SUCCESS, end="")
        print(message)
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


def _LogUtil_instance() -> object:
    return LogUtil()

lazy_static(LogUtil, "instance", _LogUtil_instance)

