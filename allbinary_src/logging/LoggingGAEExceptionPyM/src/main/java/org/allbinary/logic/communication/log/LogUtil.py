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

from java.lang.JavaRuntimeStatic import lazy_static


#ActualPlatform
class LogUtil:
    instance: LogUtil = None

    def _init_fields(self) -> None:
        self.logger: Logger = Logger.getLogger(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(LogUtil))
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def init(self) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        PreLogUtil.put("Loggin Initialized", self, "init()")
    

    def putL(self, log: Log) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        exception: object = log.getThrowable()
        try:
            if exception is not None:
                specialMessage: str = log.getSpecialMessage()
                anyType: object = log.getObject()
                functionName: str = log.getFunctionName()
                className: str = CommonStrings.getInstance().EMPTY
                clazz: type = type(anyType)
                if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(clazz) is not None:
                    className = __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(clazz)
                message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
                self.logger.log(Level.INFO, message)
        except Exception as e:
            pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            className: str = CommonStrings.getInstance().EMPTY
            clazz: type = type(anyType)
            if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(clazz) is not None:
                className = __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(clazz)
            message: str = self.logFormatUtil.getS(className, functionName, specialMessage)
            if exception is not None:
                self.logger.log(Level.SEVERE, message, exception)
            else:
                self.logger.log(Level.INFO, message)
        except Exception as e:
            pass
# from java.util.logging.Level import Level
# from org.allbinary.logic.string.StringMaker import StringMaker
# from java.util.logging.Logger import Logger
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


def _LogUtil_instance() -> object:
    return LogUtil()

lazy_static(LogUtil, "instance", _LogUtil_instance)

