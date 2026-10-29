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
class PreLogUtil:
    LOG_SUCCESS: str = "org.allbinary: "
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def put(specialMessage: str, anyType: object, functionName: str) -> None:
        PreLogUtil.putOE(specialMessage, anyType, functionName, NullUtil.getInstance().NULL_OBJECT)
    

    @staticmethod
    def putOE(specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        className: str = CommonStrings.getInstance().EMPTY
        if type(anyType).__module__ + "." + type(anyType).__qualname__ is not None:
            className = str(type(anyType).__module__ + "." + type(anyType).__qualname__)
        message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
        print(PreLogUtil.LOG_SUCCESS, end="")
        print(message)
    

    @staticmethod
    def putS(specialMessage: str, className: str, functionName: str) -> None:
        PreLogUtil.putSE(specialMessage, className, functionName, NullUtil.getInstance().NULL_OBJECT)
    

    @staticmethod
    def putSE(specialMessage: str, className: str, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
        print(PreLogUtil.LOG_SUCCESS, end="")
        print(message)
    

    @staticmethod
    def getClassName(anyType: object) -> str:
        return type(anyType).__module__ + "." + type(anyType).__qualname__
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


