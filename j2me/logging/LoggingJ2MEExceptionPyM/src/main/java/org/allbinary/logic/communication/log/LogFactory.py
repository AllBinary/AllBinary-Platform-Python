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
class LogFactory:
    LOG: Log = None
    

    @staticmethod
    def getInstanceD() -> Log:
        from org.allbinary.logic.communication.log.Log import Log
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringUtil: StringUtil = StringUtil.getInstance()
        nullUtil: NullUtil = NullUtil.getInstance()
        return Log(stringUtil.EMPTY_STRING, nullUtil.NULL_OBJECT, stringUtil.EMPTY_STRING, nullUtil.NULL_OBJECT)
    

    @staticmethod
    def getInstance(specialMessage: str, anyType: object, functionName: str, exception: object) -> Log:
        from org.allbinary.logic.communication.log.Log import Log
        return Log(specialMessage, anyType, functionName, exception)
    

    @staticmethod
    def getInstanceF(specialMessage: str, anyType: object, functionName: str) -> Log:
        return LogFactory.LOG
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringUtil import StringUtil


def _LogFactory_LOG() -> object:
    from org.allbinary.logic.communication.log.Log import Log
    from org.allbinary.logic.NullUtil import NullUtil
    from org.allbinary.logic.string.StringUtil import StringUtil
    return Log(StringUtil.getInstance().EMPTY_STRING, NullUtil.getInstance().NULL_OBJECT, StringUtil.getInstance().EMPTY_STRING, NullUtil.getInstance().NULL_OBJECT)

lazy_static(LogFactory, "LOG", _LogFactory_LOG)

