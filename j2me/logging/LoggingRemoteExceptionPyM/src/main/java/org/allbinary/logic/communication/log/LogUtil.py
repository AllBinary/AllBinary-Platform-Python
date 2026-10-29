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

import traceback


#ActualPlatform
class LogUtil:
    instance: LogUtil = None

    def _init_fields(self) -> None:
        self.MESSAGE: str = "message"
        self.isFirstException: bool = True
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(200000)
        self.abeClientInformation: AbeClientInformationInterface = None
        self.stringBuffer: StringMaker = StringMaker()
    

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
        pass
    

    # Java overloaded method: Python keeps the last definition
    def putF(self, specialMessage: str, className: str, functionName: str) -> None:
        pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        from org.allbinary.logic.communication.log.XmlRpcRemoteLogClient import XmlRpcRemoteLogClient
        if exception is not None:
            if type(exception).__module__ + "." + type(exception).__qualname__.compareTo(XmlRpcException.getName()) == 0:
                return
            if type(exception).__module__ + "." + type(exception).__qualname__.compareTo(IOException.getName()) == 0:
                return
            if self.isFirstException or self.timeDelayHelper.isTimeTNT():
                className: str = CommonStrings.getInstance().EMPTY
                self.isFirstException = False
                if anyType is not None and type(anyType).__module__ + "." + type(anyType).__qualname__ is not None:
                    className = str(type(anyType).__module__ + "." + type(anyType).__qualname__)
                message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
                try:
                    print("Eeeek")
                    if self.abeClientInformation is None:
                        raise RuntimeError()
                    hashtable: ABHashtable[object, object] = self.abeClientInformation.toHashtable()
                    self.stringBuffer.delete(0, self.stringBuffer.length())
                    self.stringBuffer.append(message)
                    self.stringBuffer.append(CommonSeps.getInstance().SPACE)
                    self.stringBuffer.append(SpecialMessageUtil.getInstance().get())
                    hashtable.put(self.MESSAGE, str(self.stringBuffer))
                    XmlRpcRemoteLogClient(self.abeClientInformation).get(hashtable)
                except BaseException as e:
                    print("Exception")
                    traceback.print_exception(e)
# from java.io.IOException import IOException
from org.apache.xmlrpc.XmlRpcException import XmlRpcException
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.canvas.SpecialMessageUtil import SpecialMessageUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable


LogUtil.instance = LogUtil()

