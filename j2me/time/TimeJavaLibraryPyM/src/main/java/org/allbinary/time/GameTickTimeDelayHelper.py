# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.time

from __future__ import annotations

import time


class GameTickTimeDelayHelper:

    def _init_fields(self) -> None:
        self.timeDelta: int = 0
        self.startTime: int = None
        self.lastStartTime: int = None
    

    def __init__(self, startTime: int) -> None:
        self._init_fields()
        self.startTime = startTime
        self.lastStartTime = 0
    

    def setStartTime(self) -> int:
        self.startTime = int(time.time() * 1000)
        return self.startTime
    

    def loop(self) -> None:
        if self.lastStartTime == -9223372036854775808:
            self.timeDelta = 0
        else:
            self.timeDelta = int(time.time() * 1000) - self.lastStartTime
    

    def getTimeFromStart(self) -> int:
        return self.startTime - self.lastStartTime


