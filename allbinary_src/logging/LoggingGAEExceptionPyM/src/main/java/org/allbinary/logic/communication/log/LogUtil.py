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
        self.logger: Logger = Logger.getLogger(LogUtil.getName())
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        PreLogUtil.put("Loggin Initialized", self, "init()")
    

    def putL(self, log: Log) -> None:
        exception: object = log.getThrowable()
        try:
            if exception is not None:
                specialMessage: str = log.getSpecialMessage()
                anyType: object = log.getObject()
                functionName: str = log.getFunctionName()
                className: str = CommonStrings.getInstance().EMPTY
                clazz: type = type(anyType)
                if clazz.getName() is not None:
                    className = clazz.getName()
                message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
                self.logger.log(Level.INFO, message)
        except Exception as e:
            pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        try:
            className: str = CommonStrings.getInstance().EMPTY
            clazz: type = type(anyType)
            if clazz.getName() is not None:
                className = clazz.getName()
            message: str = self.logFormatUtil.getS(className, functionName, specialMessage)
            if exception is not None:
                self.logger.log(Level.SEVERE, message, exception)
            else:
                self.logger.log(Level.INFO, message)
        except Exception as e:
            pass
# from java.util.logging.Level import Level
from org.allbinary.logic.string.StringMaker import StringMaker
# from java.util.logging.Logger import Logger
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


LogUtil.instance = LogUtil()

