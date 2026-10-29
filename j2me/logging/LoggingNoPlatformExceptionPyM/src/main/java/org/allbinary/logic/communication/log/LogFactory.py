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

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.communication.log.Log import Log


#NoPlatform
class LogFactory:
    LOG: Log = Log(StringUtil.getInstance().EMPTY_STRING, NullUtil.getInstance().NULL_OBJECT, StringUtil.getInstance().EMPTY_STRING, NullUtil.getInstance().NULL_OBJECT)
    

    @staticmethod
    def getInstance(specialMessage: str, anyType: object, functionName: str, exception: object) -> Log:
        raise RuntimeError()
    

    @staticmethod
    def getInstanceF(specialMessage: str, anyType: object, functionName: str) -> Log:
        raise RuntimeError()


