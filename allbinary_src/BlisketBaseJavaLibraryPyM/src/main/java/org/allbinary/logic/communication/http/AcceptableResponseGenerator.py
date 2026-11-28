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

from java.lang.JavaRuntimeStatic import lazy_static


class AcceptableResponseGenerator:
    instance: AcceptableResponseGenerator = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AcceptableResponseGenerator:
        return AcceptableResponseGenerator.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def get(self, httpServletRequest: HttpServletRequest) -> str:
        from org.allbinary.logic.communication.http.AcceptableResponseUtil import AcceptableResponseUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            acceptableResponseUtil: AcceptableResponseUtil = AcceptableResponseUtil.getInstance()
            acceptable: str = httpServletRequest.getHeader("accept")
            result: str = acceptableResponseUtil.getTagName(0)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTP):
                self.logUtil.putF("Request Type: " + acceptable, self, commonStrings.GET)
            if acceptable is not None:
                size: int = acceptableResponseUtil.size()
                for index in range(0, size):
                    if ((acceptable > acceptableResponseUtil.get(index)) - (acceptable < acceptableResponseUtil.get(index))) == 0:
                        result = acceptableResponseUtil.getTagName(index)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTP):
                self.logUtil.putF("Response Type: " + result, self, commonStrings.GET)
            return result
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET, e)
            raise e
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _AcceptableResponseGenerator_instance() -> object:
    return AcceptableResponseGenerator()

lazy_static(AcceptableResponseGenerator, "instance", _AcceptableResponseGenerator_instance)

