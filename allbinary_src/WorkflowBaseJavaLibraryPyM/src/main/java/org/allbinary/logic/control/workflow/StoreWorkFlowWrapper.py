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

from org.allbinary.logic.control.workflow.WorkFlowWrapper import WorkFlowWrapper


class StoreWorkFlowWrapper(WorkFlowWrapper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, anyType: object) -> None:
        super().__init__(anyType)
        self._init_fields()
    

    # throws Exception
    def getStoreName(self) -> str:
        try:
            helperClass: type = type(self.getWorkFlowObject())
            method: Method = helperClass.getMethod("getStoreName", None)
            result: str = method.invoke(self.getWorkFlowObject(), None)
            return result
        except Exception as e:
            error: str = "Reflection Exception"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getStoreName()", e)
            raise Exception(error)
# from java.lang.reflect.Method import Method
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


