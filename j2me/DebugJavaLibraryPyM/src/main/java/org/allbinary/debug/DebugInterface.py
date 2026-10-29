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



# Java interface
class DebugInterface:
    

    def start(self) -> None:
        raise NotImplementedError()
    

    def stop(self) -> None:
        raise NotImplementedError()
    

    def getStartTime(self) -> int:
        raise NotImplementedError()
    

    def getMaxTime(self) -> int:
        raise NotImplementedError()
    

    def isRunning(self) -> bool:
        raise NotImplementedError()


