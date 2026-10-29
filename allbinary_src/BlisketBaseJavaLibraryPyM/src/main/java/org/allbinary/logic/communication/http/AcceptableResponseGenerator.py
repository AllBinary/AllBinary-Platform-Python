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
# package org.allbinary.logic.communication.http

from __future__ import annotations



class AcceptableResponseGenerator:
    instance: AcceptableResponseGenerator = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AcceptableResponseGenerator:
        return AcceptableResponseGenerator.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def get(self, httpServletRequest: HttpServletRequest) -> str:
        from org.allbinary.logic.communication.http.AcceptableResponseUtil import AcceptableResponseUtil
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            acceptableResponseUtil: AcceptableResponseUtil = AcceptableResponseUtil.getInstance()
            acceptable: str = httpServletRequest.getHeader("accept")
            result: str = acceptableResponseUtil.getTagName(0)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTP):
                self.logUtil.putF("Request Type: " + acceptable, self, commonStrings.GET)
            if acceptable is not None:
                size: int = acceptableResponseUtil.size()
                for index in range(0, size):
                    if ((acceptable > acceptableResponseUtil.get(index)) - (acceptable < acceptableResponseUtil.get(index))) == 0:
                        result = acceptableResponseUtil.getTagName(index)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTP):
                self.logUtil.putF("Response Type: " + result, self, commonStrings.GET)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET, e)
            raise e
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


AcceptableResponseGenerator.instance = AcceptableResponseGenerator()

