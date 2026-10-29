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
# package org.allbinary.time

from __future__ import annotations

import time


class TimeDelayHelper:

    def _init_fields(self) -> None:
        self.startTime: int = -1
        self.elapsedTimeAtPause: int = -9223372036854775808
        self.delay: int = None
    

    def __init__(self, delay: int) -> None:
        self._init_fields()
        self.delay = delay
        self.setStartTimeTNT()
    

    def isTimeTNT(self) -> bool:
        currentTime: int = int(time.time() * 1000)
        if currentTime - self.startTime > self.delay:
            self.startTime = currentTime
            return True
        return False
    

    def isTimeSinceTNT(self, delay: int) -> bool:
        currentTime: int = int(time.time() * 1000)
        if currentTime - self.startTime > delay:
            self.startTime = currentTime
            return True
        return False
    

    def isTime(self, currentTime: int) -> bool:
        if currentTime - self.startTime > self.delay:
            self.startTime = currentTime
            return True
        return False
    

    def isTimeWithoutReset(self, currentTime: int) -> bool:
        if currentTime - self.startTime > self.delay:
            return True
        return False
    

    def isTimeSince(self, delay: int, currentTime: int) -> bool:
        if currentTime - self.startTime > self.delay:
            self.startTime = currentTime
            return True
        return False
    

    def getElapsedTNT(self) -> int:
        return int(time.time() * 1000) - self.startTime
    

    def getElapsed(self, currentTime: int) -> int:
        return currentTime - self.startTime
    

    def isElapsed(self, currentTime: int, time: int) -> bool:
        if self.getElapsed(currentTime) > time:
            return True
        else:
            return False
    

    def isElapsedTNT(self, time: int) -> bool:
        if self.getElapsedTNT() > time:
            return True
        else:
            return False
    

    def setStartTime(self, startTime: int) -> None:
        self.startTime = startTime
    

    def getStartTime(self) -> int:
        return self.startTime
    

    def setStartTimeTNT(self) -> None:
        self.startTime = int(time.time() * 1000)
    

    def pause(self) -> None:
        self.elapsedTimeAtPause = self.getElapsedTNT()
        self.startTime = 9223372036854775807
    

    def resume(self) -> bool:
        if self.elapsedTimeAtPause != -9223372036854775808:
            self.startTime = int(time.time() * 1000) + self.elapsedTimeAtPause
            self.elapsedTimeAtPause = -9223372036854775808
            self.setStartTimeTNT()
            return True
        return False
    

    def toStringAt(self, currentTime: int) -> str:
        elapsed: int = self.getElapsed(currentTime)
        if elapsed > 0:
            commonLabels: CommonLabels = CommonLabels.getInstance()
            elapsedAsString: str = str(elapsed)
            return str(StringMaker().append(commonLabels.START).appendlong(self.startTime).append(commonLabels.CURRENT).appendlong(currentTime).append(commonLabels.ELAPSED).append(elapsedAsString))
        else:
            return StringUtil.getInstance().EMPTY_STRING
    

    def toString(self) -> str:
        currentTime: int = int(time.time() * 1000)
        elapsed: int = self.getElapsed(currentTime)
        if elapsed > 0:
            commonLabels: CommonLabels = CommonLabels.getInstance()
            elapsedAsString: str = str(elapsed)
            return str(StringMaker().append(commonLabels.START).appendlong(self.startTime).append(commonLabels.CURRENT).appendlong(currentTime).append(commonLabels.ELAPSED).append(elapsedAsString))
        else:
            return StringUtil.getInstance().EMPTY_STRING

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels


