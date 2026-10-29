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



class Log:

    def _init_fields(self) -> None:
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        self.specialMessage: str = None
        self.anyType: object = None
        self.functionName: str = None
        self.exception: object = None
    

    def __init__(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        self._init_fields()
        self.specialMessage = specialMessage
        self.anyType = anyType
        self.functionName = functionName
        self.exception = exception
    

    def getSpecialMessage(self) -> str:
        return self.specialMessage
    

    def getObject(self) -> object:
        return self.anyType
    

    def getFunctionName(self) -> str:
        return self.functionName
    

    def getThrowable(self) -> object:
        return self.exception
    

    def toString(self) -> str:
        className: str = CommonStrings.getInstance().EMPTY
        clazz: type = type(self.anyType)
        if clazz.getName() is not None:
            className = clazz.getName()
        return self.logFormatUtil.get(className, self.functionName, self.specialMessage, self.exception)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


