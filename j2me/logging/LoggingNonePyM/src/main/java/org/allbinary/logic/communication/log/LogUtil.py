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
class LogUtil:
    instance: LogUtil = None
    

    @staticmethod
    def getInstance() -> LogUtil:
        return LogUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def putP(self, log: Log) -> None:
        pass
    

    def putF(self, specialMessage: str, anyType: object, functionName: str) -> None:
        pass
    

    # Java overloaded method: Python keeps the last definition
    def putF(self, specialMessage: str, className: str, functionName: str) -> None:
        pass
    

    def put(self, specialMessage: str, anyType: object, functionName: str, exception: object) -> None:
        pass


LogUtil.instance = LogUtil()

