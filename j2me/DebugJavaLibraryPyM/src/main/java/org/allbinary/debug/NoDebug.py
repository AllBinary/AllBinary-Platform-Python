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

from org.allbinary.debug.DebugInterface import DebugInterface


class NoDebug(DebugInterface):
    SINGLETON: DebugInterface = None
    

    @staticmethod
    def getInstance() -> DebugInterface:
        return NoDebug.SINGLETON
    

    def start(self) -> None:
        pass
    

    def stop(self) -> None:
        pass
    

    def getMaxTime(self) -> int:
        return 10000
    

    def getStartTime(self) -> int:
        return 0
    

    def isRunning(self) -> bool:
        return False


NoDebug.SINGLETON = NoDebug()

