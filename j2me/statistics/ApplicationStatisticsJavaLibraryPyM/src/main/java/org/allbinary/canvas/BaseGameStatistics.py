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
# package org.allbinary.canvas

from __future__ import annotations



class BaseGameStatistics:

    def _init_fields(self) -> None:
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(2147483647)
        self.updateDelayHelper: TimeDelayHelper = TimeDelayHelper(2000)
        self.totalRefreshes: int = 0
        self.totalFrames: int = 0
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.DEFAULT_SCALE_FACTOR: int = ScaleFactorFactory.getInstance().DEFAULT_SCALE_FACTOR
        self.NOT: str = "Not enough Time to Calculate"
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        self.STRING_ARRAY: list[str] = [" Total Time: ", self.EMPTY_STRING, " Total Frames: ", self.EMPTY_STRING, " Frames/10 Sec: ", self.EMPTY_STRING, " Total Paints: ", self.EMPTY_STRING, " Paints/10 Sec: ", self.EMPTY_STRING]
        self.SPACE_CHAR: str = ' '
        self.PLUS_CHAR: str = '+'
        self.X_CHAR: str = 'X'
        self.CHAR_ARRAY: list[list[str]] = [['F', 'r', 'a', 'm', 'e', 's', '/', '1', '0', ' ', 'S', 'e', 'c', ':'], ['X', 'X'], ['P', 'a', 'i', 'n', 't', 's', '/', '1', '0', ' ', 'S', 'e', 'c', ':'], ['X', 'X']]
        self.primitiveLongSingleton: PrimitiveLongSingleton = PrimitiveLongSingleton.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        self.timeDelayHelper.setStartTimeTNT()
        self.totalRefreshes = 0
        self.totalFrames = 0
    

    def add(self, string: str) -> None:
        pass
    

    def process(self) -> None:
        pass
    

    def nextFrame(self) -> None:
        self.totalFrames += 1
    

    def nextRefresh(self) -> None:
        self.totalRefreshes += 1
    

    def getRefreshRate(self) -> int:
        elapsed: int = self.timeDelayHelper.getElapsed(self.gameTickTimeDelayHelper.startTime)
        if elapsed > 1:
            time: int = ((int((int(self.totalRefreshes / (elapsed >> self.DEFAULT_SCALE_FACTOR)))) + 32768) % 65536 - 32768)
            return time
        else:
            return 0
    

    def getTimeDelayHelper(self) -> TimeDelayHelper:
        return self.timeDelayHelper
    

    def to2DCharArray(self) -> list[list[str]]:
        totalTime: int = self.timeDelayHelper.getElapsed(self.gameTickTimeDelayHelper.startTime)
        totalTime = (totalTime >> self.DEFAULT_SCALE_FACTOR)
        if totalTime > 0 and self.updateDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            framesPerSec: int = (int(self.totalFrames / totalTime))
            if framesPerSec < 10:
                self.CHAR_ARRAY[1][0] = self.SPACE_CHAR
                self.CHAR_ARRAY[1][1] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[framesPerSec]
            elif framesPerSec < 100:
                tens: int = int(framesPerSec / 10)
                removeTens: int = tens * 10
                self.CHAR_ARRAY[1][0] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[tens]
                self.CHAR_ARRAY[1][1] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[framesPerSec - removeTens]
            else:
                self.CHAR_ARRAY[1][0] = self.PLUS_CHAR
                self.CHAR_ARRAY[1][1] = self.PLUS_CHAR
            refreshesPerSec: int = (int(self.totalRefreshes / totalTime))
            if refreshesPerSec < 10:
                self.CHAR_ARRAY[3][0] = self.X_CHAR
                self.CHAR_ARRAY[3][1] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[refreshesPerSec]
            elif refreshesPerSec < 100:
                tens: int = int(refreshesPerSec / 10)
                removeTens: int = tens * 10
                self.CHAR_ARRAY[3][0] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[int(refreshesPerSec / 10)]
                self.CHAR_ARRAY[3][1] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[refreshesPerSec - removeTens]
            else:
                self.CHAR_ARRAY[3][0] = self.PLUS_CHAR
                self.CHAR_ARRAY[3][1] = self.PLUS_CHAR
        return self.CHAR_ARRAY
    

    def toStringArray(self) -> list[str]:
        totalTime: int = self.timeDelayHelper.getElapsed(self.gameTickTimeDelayHelper.startTime)
        totalTime = (int(totalTime / 10000))
        if totalTime > 0:
            self.STRING_ARRAY[1] = str(totalTime)
            self.STRING_ARRAY[3] = str(self.totalFrames)
            self.STRING_ARRAY[5] = str(int(self.totalFrames / totalTime))
            self.STRING_ARRAY[7] = str(self.totalRefreshes)
            self.STRING_ARRAY[9] = str(int(self.totalRefreshes / totalTime))
        else:
            string: str = self.EMPTY_STRING
            self.STRING_ARRAY[1] = string
            self.STRING_ARRAY[3] = string
            self.STRING_ARRAY[5] = string
            self.STRING_ARRAY[7] = string
            self.STRING_ARRAY[9] = string
        return self.STRING_ARRAY
    

    def toStringAt(self, totalTime: int) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.STRING_ARRAY[0])
        stringBuffer.appendlong(totalTime)
        stringBuffer.append(self.STRING_ARRAY[2])
        stringBuffer.appendlong(self.totalFrames)
        stringBuffer.append(self.STRING_ARRAY[4])
        stringBuffer.appendlong(int(self.totalFrames / totalTime))
        if self.totalRefreshes > 0:
            stringBuffer.append(self.STRING_ARRAY[6])
            stringBuffer.appendlong(self.totalRefreshes)
            stringBuffer.append(self.STRING_ARRAY[8])
            stringBuffer.appendlong(int(self.totalRefreshes / totalTime))
            stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        return str(stringBuffer)
    

    def toString(self) -> str:
        totalTime: int = self.timeDelayHelper.getElapsed(self.gameTickTimeDelayHelper.startTime)
        totalTime = (int(totalTime / 1000))
        if totalTime > 0:
            return self.toStringAt(totalTime)
        else:
            return self.NOT

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
from org.allbinary.logic.math.ScaleFactorFactory import ScaleFactorFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


