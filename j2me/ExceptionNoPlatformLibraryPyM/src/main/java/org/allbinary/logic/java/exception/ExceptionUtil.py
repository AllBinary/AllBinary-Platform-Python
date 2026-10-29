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
# package org.allbinary.logic.java.exception

from __future__ import annotations



#NoPlatform
class ExceptionUtil:
    instance: ExceptionUtil = None

    def _init_fields(self) -> None:
        self.PRETEND_EXCEPTION: Exception = Exception("Not Really An Exception")
    

    @staticmethod
    def getInstance() -> ExceptionUtil:
        return ExceptionUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getStackTrace(self, e: BaseException) -> str:
        raise RuntimeError()


ExceptionUtil.instance = ExceptionUtil()

