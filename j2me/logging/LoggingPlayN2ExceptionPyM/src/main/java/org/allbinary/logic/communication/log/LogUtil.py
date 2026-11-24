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
        self.logFormatUtil: LogFormatUtil = LogFormatUtil.getInstance()
        self.LOG_SUCCESS: str = "org.allbinary: "
    

    @staticmethod
    def getInstance() -> LogUtil:
        from jsinterop.annotations.JsMethod import JsMethod
        return LogUtil.instance
    

    def __init__(self) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        self._init_fields()
    

    def putL(self, log: Log) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        if log is None:
            return
        specialMessage: str = log.getSpecialMessage()
        anyType: object = log.getObject()
        functionName: str = log.getFunctionName()
        exception: object = log.getThrowable()
        self.put(specialMessage, anyType, functionName, exception)
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from playn.core.PlayN import PlayN
        from jsinterop.annotations.JsMethod import JsMethod
        className: str = PreLogUtil.getClassName(anyType)
        if className is None:
            className = CommonStrings.getInstance().EMPTY
        message: str = self.logFormatUtil.getS(className, functionName, specialMessage)
        playN: PlayN = PlayN.getInstance()
        playN.log().debug(self.LOG_SUCCESS + message)
    

    def putFS(self, specialMessage: str, className: str, functionName: str) -> None:
        from playn.core.PlayN import PlayN
        from jsinterop.annotations.JsMethod import JsMethod
        message: str = self.logFormatUtil.getS(className, functionName, specialMessage)
        playN: PlayN = PlayN.getInstance()
        playN.log().debug(self.LOG_SUCCESS + message)
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from playn.core.PlayN import PlayN
        from jsinterop.annotations.JsMethod import JsMethod
        className: str = PreLogUtil.getClassName(anyType)
        if className is None:
            className = CommonStrings.getInstance().EMPTY
        message: str = self.logFormatUtil.get(className, functionName, specialMessage, exception)
        playN: PlayN = PlayN.getInstance()
        if exception is not None:
            playN.log().error(self.LOG_SUCCESS + message, exception)
        else:
            playN.log().debug(self.LOG_SUCCESS + message)
# from jsinterop.annotations.JsType import JsType
# from org.allbinary.string.CommonStrings import CommonStrings
# from playn.core.PlayN import PlayN
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor


def _LogUtil_instance() -> object:
    return LogUtil()

lazy_static(LogUtil, "instance", _LogUtil_instance)

