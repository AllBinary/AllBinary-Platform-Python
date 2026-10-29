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



#NoPlatform
class LogFormatUtil:
    instance: LogFormatUtil = None
    

    @staticmethod
    def getInstance() -> LogFormatUtil:
        return LogFormatUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def get(self, className: str, functionName: str, specialMessage: str, exception: object) -> str:
        raise RuntimeError()
    

    def getS(self, className: str, functionName: str, specialMessage: str) -> str:
        raise RuntimeError()
    

    def getO(self, exception: object) -> str:
        raise RuntimeError()
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.java.exception.ExceptionUtil import ExceptionUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.time.TimeStampUtil import TimeStampUtil


LogFormatUtil.instance = LogFormatUtil()

