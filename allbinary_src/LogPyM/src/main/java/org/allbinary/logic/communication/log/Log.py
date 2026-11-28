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
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        if "specialMessage" not in vars(self): self.specialMessage: str = None
        if "anyType" not in vars(self): self.anyType: object = None
        if "functionName" not in vars(self): self.functionName: str = None
        if "exception" not in vars(self): self.exception: object = None
    

    def __init__(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        __class__._init_fields(self)
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
        from org.allbinary.string.CommonStrings import CommonStrings
        className: str = CommonStrings.getInstance().EMPTY
        clazz: type = type(self.anyType)
        if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(clazz) is not None:
            className = __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(clazz)
        return self.logFormatUtil.get(className, self.functionName, self.specialMessage, self.exception)

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil


