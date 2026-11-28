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
# package org.allbinary.logic.control.workflow

from __future__ import annotations

from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface


class WorkFlowWrapper(WorkFlowInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "anyType" not in vars(self): self.anyType: object = None
    

    def __init__(self, anyType: object) -> None:
        __class__._init_fields(self)
        self.anyType = anyType
    

    def getWorkFlowObject(self) -> object:
        return self.anyType
    

    # throws Exception
    def getName(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.anyType)
            method: Method = helperClass.getMethod("getName", None)
            result: str = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            error: str = "Reflection Exception"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getName()", e)
            raise Exception(error)
    

    # throws Exception
    def getStoreName(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.anyType)
            method: Method = helperClass.getMethod("getStoreName", None)
            result: str = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            error: str = "Reflection Exception"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getStoreName()", e)
            raise Exception(error)
    

    # throws Exception
    def process(self) -> int:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.anyType)
            method: Method = helperClass.getMethod(self.commonStrings.PROCESS, None)
            result: int = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            error: str = "Reflection Exception"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
            raise Exception(error)
# from java.lang.reflect.Method import Method
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


