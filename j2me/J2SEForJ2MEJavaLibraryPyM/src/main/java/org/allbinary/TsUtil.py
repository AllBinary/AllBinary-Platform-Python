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
import gc
import threading
from java.lang.ClassLoader import ClassLoader
from java.lang.JavaRuntimeStatic import lazy_static


#J2SE
class TsUtil:
    instance: TsUtil = None
    _lock = threading.RLock()
    

    @staticmethod
    def getInstance() -> TsUtil:
        return TsUtil.instance
    

    def longBitsToDouble(self, bits: int) -> float:
        return Double.longBitsToDouble(bits)
    

    def intBitsToFloat(self, bits: int) -> float:
        return Float.intBitsToFloat(bits)
    

    def hashCode(self, anyType: object) -> int:
        return hash(anyType)
    

    # throws InterruptedException
    def waitFor(self, any: object, timeoutMillis: int) -> None:
        anyType: object = any
        java_wait(anyType, timeoutMillis)
    

    # throws RecordStoreNotOpenException, InvalidRecordIDException, RecordStoreException
    def getRecord(self, anyType: object, recordId: int) -> list[int]:
        from javax.microedition.rms.InvalidRecordIDException import InvalidRecordIDException
        from javax.microedition.rms.RecordStore import RecordStore
        from javax.microedition.rms.RecordStoreException import RecordStoreException
        from javax.microedition.rms.RecordStoreNotOpenException import RecordStoreNotOpenException
        from org.allbinary.logic.NullUtil import NullUtil
        recordStore: RecordStore = anyType
        data: list[int] = None
        with java_monitor(self):
            data = [0] * (recordStore.getRecordSize(recordId))
            recordStore.getRecord(recordId, data, 0)
        return (NullUtil.getInstance().NULL_BYTE_ARRAY if len(data) < 1 else data)
    

    def compareTo(self, a: str, b: str) -> int:
        return ((a > b) - (a < b))
    

    def equalIgnoreCase(self, a: str, b: str) -> bool:
        return (a.lower() == str(b).lower())
    

    def equalsNotstring(self, anyType: object, object2: object) -> bool:
        return java_equals(anyType, object2)
    

    def getClassClassLoader(self, anyType: object) -> ClassLoader:
        return __import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.getSystemClassLoader()
    

    def toNumberFromChar(self, value: str) -> int:
        return ord(value)
    

    def toNumber(self, value: int) -> int:
        return value
    

    def getByteArray(self, string: str) -> list[int]:
        return list(string.encode())
    

    def isItemListener(self, owner: Displayable) -> bool:
        from javax.microedition.lcdui.Displayable import Displayable
        from javax.microedition.lcdui.Form import Form
        if isinstance(owner, Form):
            return True
        else:
            return False
    

    def gc(self) -> None:
        gc.collect()
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.lcdui.Form import Form
# from javax.microedition.rms.InvalidRecordIDException import InvalidRecordIDException
# from javax.microedition.rms.RecordStore import RecordStore
# from javax.microedition.rms.RecordStoreException import RecordStoreException
# from javax.microedition.rms.RecordStoreNotOpenException import RecordStoreNotOpenException
# from org.allbinary.logic.NullUtil import NullUtil


def _TsUtil_instance() -> object:
    return TsUtil()

lazy_static(TsUtil, "instance", _TsUtil_instance)

