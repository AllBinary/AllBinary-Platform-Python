# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary

from __future__ import annotations

from java.lang.JavaMonitor import java_monitor, java_wait
from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_predicate
import gc
from java.lang.JavaRuntimeStatic import lazy_static


#None - Do not use
class TsUtil:
    instance: TsUtil = None
    

    @staticmethod
    def getInstance() -> TsUtil:
        return TsUtil.instance
    

    def hashCode(self, anyType: object) -> int:
        return java_predicate(anyType, "hashCode")
    

    # throws InterruptedException
    def waitFor(self, any: object, timeoutMillis: int) -> None:
        anyType: object = any
        java_wait(anyType, timeoutMillis)
    

    def getRecord(self, anyType: object, recordId: int) -> list[int]:
        return [0] * (0)
    

    def compareTo(self, a: str, b: str) -> int:
        return ((a > b) - (a < b))
    

    def equalIgnoreCase(self, a: str, b: str) -> bool:
        return (a.lower() == str(b).lower())
    

    def equalsNotstring(self, anyType: object, object2: object) -> bool:
        return java_equals(anyType, object2)
    

    def toNumberFromChar(self, value: str) -> int:
        return ord(value)
    

    def toNumber(self, value: int) -> int:
        return value
    

    def getByteArray(self, string: str) -> list[int]:
        return list(string.encode())
    

    def isItemListener(self, owner: object) -> bool:
        return False
    

    def printAvailableMethods(self, anyType: object) -> None:
        pass
    

    def gc(self) -> None:
        gc.collect()


def _TsUtil_instance() -> object:
    return TsUtil()

lazy_static(TsUtil, "instance", _TsUtil_instance)

