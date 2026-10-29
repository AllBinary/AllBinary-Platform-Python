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
        self.LOG_SUCCESS: str = "org.allbinary: "
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def putL(self, log: Log) -> None:
        if log is None:
            return
        specialMessage: str = log.getSpecialMessage()
        anyType: object = log.getObject()
        functionName: str = log.getFunctionName()
        exception: object = log.getThrowable()
        self.put(specialMessage, anyType, functionName, exception)
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        className: str = PreLogUtil.getClassName(anyType)
        if className is None:
            className = CommonStrings.getInstance().EMPTY
        message: str = self.logFormatUtil.getS(className, functionName, specialMessage)
        PlayN.log().debug(self.LOG_SUCCESS + message)
    

    def putFS(self, specialMessage: str, className: str, functionName: str) -> None:
        message: str = self.logFormatUtil.getS(className, functionName, specialMessage)
        PlayN.log().debug(self.LOG_SUCCESS + message)
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        className: str = PreLogUtil.getClassName(anyType)
        if className is None:
            className = CommonStrings.getInstance().EMPTY
        message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
        if exception is not None:
            PlayN.log().error(self.LOG_SUCCESS + message, exception)
        else:
            PlayN.log().debug(self.LOG_SUCCESS + message)
from org.allbinary.string.CommonStrings import CommonStrings
from playn.core.PlayN import PlayN
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


LogUtil.instance = LogUtil()

