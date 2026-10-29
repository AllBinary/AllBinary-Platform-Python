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
class LogFormatUtil:
    instance: LogFormatUtil = None

    def _init_fields(self) -> None:
        self.timeStampUtil: TimeStampUtil = TimeStampUtil.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.LOG_ERROR: str = "\nLog-Error: "
        self.EMPTY: str = "Empty"
        self.STACK_TRACE: str = "\nStack Trace: "
        self.TIME: str = "Time: "
        self.CLASS_NAME: str = self.commonSeps.SPACE
        self.FUNCTION_CALL: str = CommonLabels.getInstance().COLON_SEP
        self.SPECIAL_MESSAGE: str = "> "
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.exceptionUtil: ExceptionUtil = ExceptionUtil.getInstance()
        self.nullUtil: NullUtil = NullUtil.getInstance()
    

    @staticmethod
    def getInstance() -> LogFormatUtil:
        return LogFormatUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def get(self, className: str, functionName: str, specialMessage: str, exception: object) -> str:
        stringBuffer: StringMaker = self.getF(className, functionName)
        stringBuffer.append(self.getO(exception))
        stringBuffer.append(self.SPECIAL_MESSAGE)
        stringBuffer.append(specialMessage)
        stringBuffer.append(self.commonSeps.NEW_LINE)
        return str(stringBuffer)
    

    def getS(self, className: str, functionName: str, specialMessage: str) -> str:
        stringBuffer: StringMaker = self.getF(className, functionName)
        stringBuffer.append(self.SPECIAL_MESSAGE)
        stringBuffer.append(specialMessage)
        stringBuffer.append(self.commonSeps.NEW_LINE)
        return str(stringBuffer)
    

    def getF(self, className: str, functionName: str) -> StringMaker:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.TIME)
        stringBuffer.append(self.timeStampUtil.getAsString())
        stringBuffer.append(self.CLASS_NAME)
        stringBuffer.append(className)
        stringBuffer.append(self.FUNCTION_CALL)
        stringBuffer.append(functionName)
        return stringBuffer
    

    def getO(self, exception: object) -> str:
        if exception != self.nullUtil.NULL_OBJECT:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.LOG_ERROR)
            exceptionAsString: str = str(exception)
            if exceptionAsString is not None:
                stringBuffer.append(exceptionAsString)
            else:
                stringBuffer.append(self.EMPTY)
            stringBuffer.append(self.STACK_TRACE)
            if exception != self.nullUtil.NULL_OBJECT:
                stringBuffer.append(self.exceptionUtil.getStackTrace(exception))
            else:
                stringBuffer.append(self.stringUtil.NULL_STRING)
            return str(stringBuffer)
        else:
            return StringUtil.getInstance().EMPTY_STRING
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.time.TimeStampUtil import TimeStampUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.java.exception.ExceptionUtil import ExceptionUtil
from org.allbinary.string.CommonLabels import CommonLabels


LogFormatUtil.instance = LogFormatUtil()

