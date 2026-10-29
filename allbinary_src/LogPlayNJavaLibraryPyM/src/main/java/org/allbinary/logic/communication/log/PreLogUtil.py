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
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        className: str = PreLogUtil.getClassName(anyType)
        if className is None:
            className = CommonStrings.getInstance().EMPTY
        className = str(StringMaker().append(className).append(CommonSeps.getInstance().FORWARD_SLASH).append(StringUtil.getInstance().toString(anyType)))
        message: str = LogFormatUtil.getInstance().getS(className, functionName, specialMessage)
        PlayN.log().debug(str(PreLogUtil.LOG_SUCCESS) + message)
    

    @staticmethod
    def putOE(specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        className: str = PreLogUtil.getClassName(anyType)
        if className is None:
            className = CommonStrings.getInstance().EMPTY
        className = str(StringMaker().append(className).append(CommonSeps.getInstance().FORWARD_SLASH).append(StringUtil.getInstance().toString(anyType)))
        message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
        PlayN.log().error(str(PreLogUtil.LOG_SUCCESS) + message, exception)
    

    @staticmethod
    def putS(specialMessage: str, className: str, functionName: str) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        message: str = LogFormatUtil.getInstance().getS(className, functionName, specialMessage)
        PlayN.log().debug(str(PreLogUtil.LOG_SUCCESS) + message)
    

    @staticmethod
    def putSE(specialMessage: str, className: str, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
        PlayN.log().error(str(PreLogUtil.LOG_SUCCESS) + message, exception)
    

    @staticmethod
    def getClassName(anyType: object) -> str:
        raise NotImplementedError()
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from playn.core.PlayN import PlayN


