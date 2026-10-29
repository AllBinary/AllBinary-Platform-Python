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
# package org.allbinary.debug

from __future__ import annotations

import time
from org.allbinary.debug.DebugInterface import DebugInterface


class AndroidDebug(DebugInterface):

    def _init_fields(self) -> None:
        self.startTime: int = 9223372036854775807
        self.running: bool = False
        self.bufferSize: int = 32 * 1024 * 1024

    def __init__(self) -> None:
        self._init_fields()
    

    def start(self) -> None:
        self.setStartTime(int(time.time() * 1000))
        Debug.startMethodTracing("trace", self.bufferSize)
        self.setRunning(True)
    

    def stop(self) -> None:
        self.startTime = 9223372036854775807
        Debug.stopMethodTracing()
        self.setRunning(False)
    

    def getMaxTime(self) -> int:
        return 120000
    

    def setStartTime(self, startTime: int) -> None:
        self.startTime = startTime
    

    def getStartTime(self) -> int:
        return self.startTime
    

    def setRunning(self, running: bool) -> None:
        self.running = running
    

    def isRunning(self) -> bool:
        return self.running
from android.os.Debug import Debug


