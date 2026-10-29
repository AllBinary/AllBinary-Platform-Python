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
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        self.LABEL: str = "org.allbinary"
    

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
        self.put(specialMessage, anyType, functionName, exception)
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        self.put(specialMessage, anyType, functionName, NullUtil.getInstance().NULL_OBJECT)
    

    def putFS(self, specialMessage: str, string: str, functionName: str) -> None:
        self.putS(specialMessage, string, functionName, NullUtil.getInstance().NULL_OBJECT)
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        className: str = self.LABEL
        className = str(str(StringMaker().append(type(anyType).__module__ + "." + type(anyType).__qualname__).append(self.commonSeps.COLON).append(format(TsUtil.getInstance().hashCode(anyType), "x"))))
        message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
        android.util.Log.i(self.LABEL, message)
    

    def putS(self, specialMessage: str, string: str, functionName: str, exception: object) -> None:
        className: str = self.LABEL
        className = str(str(StringMaker().append(string).append(self.commonSeps.COLON).append(format(TsUtil.getInstance().hashCode(string), "x"))))
        message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
        android.util.Log.i(self.LABEL, message)
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


LogUtil.instance = LogUtil()

