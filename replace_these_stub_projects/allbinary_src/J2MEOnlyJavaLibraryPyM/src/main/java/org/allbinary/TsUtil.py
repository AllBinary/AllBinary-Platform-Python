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

import gc
import threading


#J2ME
class TsUtil:
    instance: TsUtil = None
    _lock = threading.RLock()
    

    @staticmethod
    def getInstance() -> TsUtil:
        return TsUtil.instance
    

    def hashCode(self, anyType: object) -> int:
        return anyType.hashCode()
    

    # throws InterruptedException
    def waitFor(self, any: object, timeoutMillis: int) -> None:
        anyType: object = any
        anyType.wait(timeoutMillis)
    

    # throws RecordStoreNotOpenException, InvalidRecordIDException, RecordStoreException
    def getRecord(self, anyType: object, recordId: int) -> list[int]:
        recordStore: RecordStore = anyType
        data: list[int] = None
        with self._lock:  # synchronized (self)
            data = [0] * (recordStore.getRecordSize(recordId))
            recordStore.getRecord(recordId, data, 0)
        return (NullUtil.getInstance().NULL_BYTE_ARRAY if len(data) < 1 else data)
    

    def compareTo(self, a: str, b: str) -> int:
        return ((a > b) - (a < b))
    

    def equalIgnoreCase(self, a: str, b: str) -> bool:
        return (a.lower() == str(b).lower())
    

    def equalsNotstring(self, anyType: object, object2: object) -> bool:
        return anyType.equals(object2)
    

    def toNumberFromChar(self, value: str) -> int:
        return ord(value)
    

    def toNumber(self, value: int) -> int:
        return value
    

    def getByteArray(self, string: str) -> list[int]:
        return list(string.encode())
    

    def isItemListener(self, owner: Displayable) -> bool:
        if isinstance(owner, Form):
            return True
        else:
            return False
    

    def printAvailableMethods(self, anyType: object) -> None:
        pass
    

    def gc(self) -> None:
        gc.collect()
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.lcdui.Form import Form
# from javax.microedition.rms.InvalidRecordIDException import InvalidRecordIDException
# from javax.microedition.rms.RecordStore import RecordStore
# from javax.microedition.rms.RecordStoreException import RecordStoreException
# from javax.microedition.rms.RecordStoreNotOpenException import RecordStoreNotOpenException
from org.allbinary.logic.NullUtil import NullUtil


TsUtil.instance = TsUtil()

