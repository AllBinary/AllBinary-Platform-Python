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
# package org.allbinary.logic.communication.java.vm.stats

from __future__ import annotations

import threading


class JvmStatistics:

    def _init_fields(self) -> None:
        self.runtime: Runtime = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.runtime = Runtime.getRuntime()
    

    def getFreeMemoryBytes(self) -> int:
        return self.runtime.freeMemory()
    

    def getFreeMemoryKilobytes(self) -> int:
        return int(self.getFreeMemoryBytes() / 1024)
    

    def getFreeMemoryMegabytes(self) -> int:
        return int(self.getFreeMemoryKilobytes() / 1024)
    

    def getMaxMemoryBytes(self) -> int:
        return self.runtime.maxMemory()
    

    def getMaxMemoryKilobytes(self) -> int:
        return int(self.getMaxMemoryBytes() / 1024)
    

    def getMaxMemoryMegabytes(self) -> int:
        return int(self.getMaxMemoryKilobytes() / 1024)
    

    def getTotalMemoryBytes(self) -> int:
        return self.runtime.totalMemory()
    

    def getTotalMemoryKilobytes(self) -> int:
        return int(self.getTotalMemoryBytes() / 1024)
    

    def getTotalMemoryMegabytes(self) -> int:
        return int(self.getTotalMemoryKilobytes() / 1024)
    

    def getFreeMemoryBytesLong(self) -> int:
        return int(self.getFreeMemoryBytes())
    

    def getFreeMemoryKilobytesLong(self) -> int:
        return int(self.getFreeMemoryKilobytes())
    

    def getFreeMemoryMegabytesLong(self) -> int:
        return int(self.getFreeMemoryMegabytes())
    

    def getMaxMemoryBytesLong(self) -> int:
        return int(self.getMaxMemoryBytes())
    

    def getMaxMemoryKilobytesLong(self) -> int:
        return int(self.getMaxMemoryKilobytes())
    

    def getMaxMemoryMegabytesLong(self) -> int:
        return int(self.getMaxMemoryMegabytes())
    

    def getTotalMemoryBytesLong(self) -> int:
        return int(self.getTotalMemoryBytes())
    

    def getTotalMemoryKilobytesLong(self) -> int:
        return int(self.getTotalMemoryKilobytes())
    

    def getTotalMemoryMegabytesLong(self) -> int:
        return int(self.getTotalMemoryMegabytes())
    

    def getFreeMemoryBytesString(self) -> str:
        return str(self.getFreeMemoryBytesLong())
    

    def getFreeMemoryKilobytesString(self) -> str:
        return str(self.getFreeMemoryKilobytesLong())
    

    def getFreeMemoryMegabytesString(self) -> str:
        return str(self.getFreeMemoryMegabytesLong())
    

    def getMaxMemoryBytesString(self) -> str:
        return str(self.getMaxMemoryBytesLong())
    

    def getMaxMemoryKilobytesString(self) -> str:
        return str(self.getMaxMemoryKilobytesLong())
    

    def getMaxMemoryMegabytesString(self) -> str:
        return str(self.getMaxMemoryMegabytesLong())
    

    def getTotalMemoryBytesString(self) -> str:
        return str(self.getTotalMemoryBytesLong())
    

    def getTotalMemoryKilobytesString(self) -> str:
        return str(self.getTotalMemoryKilobytesLong())
    

    def getTotalMemoryMegabytesString(self) -> str:
        return str(self.getTotalMemoryMegabytesLong())
    

    def getNumberOfThreads(self) -> int:
        return Thread.activeCount()
    

    def getNumberOfThreadsLong(self) -> int:
        return int(self.getNumberOfThreads())
    

    def getNumberOfThreadsString(self) -> str:
        return str(self.getNumberOfThreadsLong())
    

    def collectGarbage(self) -> None:
        self.runtime.gc()


