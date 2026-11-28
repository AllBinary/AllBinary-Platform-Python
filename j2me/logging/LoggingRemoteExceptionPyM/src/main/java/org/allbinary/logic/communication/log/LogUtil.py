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

from java.lang.System import System
from java.lang.JavaRuntimeStatic import java_predicate
import traceback
from java.lang.JavaRuntimeStatic import lazy_static


#ActualPlatform
class LogUtil:
    instance: LogUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.MESSAGE: str = "message"
        self.isFirstException: bool = True
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(200000)
        if "abeClientInformation" not in vars(self): self.abeClientInformation: AbeClientInformationInterface = None
        self.stringBuffer: StringMaker = StringMaker()
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

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
    

    def putFS(self, specialMessage: str, className: str, functionName: str) -> None:
        pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        from org.allbinary.logic.communication.log.XmlRpcRemoteLogClient import XmlRpcRemoteLogClient
        from org.apache.xmlrpc.XmlRpcException import XmlRpcException
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.canvas.SpecialMessageUtil import SpecialMessageUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.ABHashtable import ABHashtable
        if exception is not None:
            if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(exception)).compareTo(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(XmlRpcException)) == 0:
                return
            if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(exception)).compareTo(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(IOException)) == 0:
                return
            if self.isFirstException or java_predicate(self.timeDelayHelper, "isTimeTNT"):
                className: str = CommonStrings.getInstance().EMPTY
                self.isFirstException = False
                if anyType is not None and __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)) is not None:
                    className = str(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)))
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
# from org.apache.xmlrpc.XmlRpcException import XmlRpcException
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.canvas.SpecialMessageUtil import SpecialMessageUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.util.ABHashtable import ABHashtable


def _LogUtil_instance() -> object:
    return LogUtil()

lazy_static(LogUtil, "instance", _LogUtil_instance)

