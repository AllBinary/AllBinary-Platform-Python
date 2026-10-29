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
# package org.allbinary.logic.communication.log.config

from __future__ import annotations

import threading


class LoggingInitInfo:
    logConfigInfoList: BasicArrayList = None
    hasRead: bool = False
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def write() -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._write_unlocked()

    @staticmethod
    def _write_unlocked() -> None:
        try:
            LoggingInitInfo.hasRead = False
        except Exception as e:
            raise e
    

    # throws Exception
    @staticmethod
    def read() -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._read_unlocked()

    @staticmethod
    def _read_unlocked() -> None:
        try:
            pass
        except Exception as e:
            raise e
    

    @staticmethod
    def setHasRead(value: bool) -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._setHasRead_unlocked(value)

    @staticmethod
    def _setHasRead_unlocked(value: bool) -> None:
        LoggingInitInfo.hasRead = value
    

    # throws Exception
    @staticmethod
    def updateIfNeeded() -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._updateIfNeeded_unlocked()

    @staticmethod
    def _updateIfNeeded_unlocked() -> None:
        if not LoggingInitInfo.hasRead:
            LoggingInitInfo.read()
            LoggingInitInfo.hasRead = True
            if LoggingInitInfo.logConfigInfoList is None:
                raise Exception("Read Failed")
    

    def isValid(self) -> bool:
        try:
            return True
        except Exception as e:
            return False
    

    @staticmethod
    def set(logConfigInfoList: BasicArrayList) -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._set_unlocked(logConfigInfoList)

    @staticmethod
    def _set_unlocked(logConfigInfoList: BasicArrayList) -> None:
        LoggingInitInfo.logConfigInfoList = logConfigInfoList
    

    # throws Exception
    @staticmethod
    def get() -> BasicArrayList:
        LoggingInitInfo.updateIfNeeded()
        return LoggingInitInfo.logConfigInfoList
    

    # throws Exception
    @staticmethod
    def getTypeList() -> BasicArrayList:
        LoggingInitInfo.updateIfNeeded()
        allLogTypeVector: BasicArrayList = BasicArrayListD()
        size: int = LoggingInitInfo.logConfigInfoList.size()
        for index in range(0, size):
            logConfigInfo: LogConfig = LoggingInitInfo.logConfigInfoList.objectArray[index]
            logTypeVector: BasicArrayList = logConfigInfo.getTypeVector()
            if logConfigInfo.isEnabled():
                allLogTypeVector.addAllList(logTypeVector)
        return allLogTypeVector
    

    # throws Exception
    def getNumberOfLogConfigs(self) -> int:
        return LoggingInitInfo.logConfigInfoList.size()
    

    def toString(self) -> str:
        try:
            return None
        except Exception as e:
            return "Error"

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


