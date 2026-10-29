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
# package org.allbinary.logic.math

from __future__ import annotations



class PrimitiveLongUtil:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.powerOfTen: int = None
        self.maxValue: int = None
        self.maxDigits: int = None
        self.charArray: list[str] = None
        self.currentTotalDigits: int = 0
        self.primitiveLongSingleton: PrimitiveLongSingleton = PrimitiveLongSingleton.getInstance()
    

    @staticmethod
    def createPowerOfTen(powerOfTen: int) -> PrimitiveLongUtil:
        primitiveLongUtil: PrimitiveLongUtil = PrimitiveLongUtil(powerOfTen, NullUtil.getInstance().NULL_OBJECT)
        if powerOfTen % 10 != 0:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.put(commonStrings.EXCEPTION, primitiveLongUtil, commonStrings.CONSTRUCTOR, Exception("Max must be power of 10"))
        return primitiveLongUtil
    

    def __init__(self, powerOfTen: int, unused: object) -> None:
        from org.allbinary.logic.math.MathUtil import MathUtil
        self._init_fields()
        self.maxDigits = MathUtil.getInstance().getTotalDigits(powerOfTen)
        self.powerOfTen = powerOfTen
        self.maxValue = (powerOfTen * 10) - 1
        self.charArray = ['\0'] * (self.maxDigits)
    

    def getCharArray(self, value: int) -> list[str]:
        if value < 10:
            self.setCurrentTotalDigits(1)
            return self.primitiveLongSingleton.NUMBER_CHAR_ARRAYS[value]
        if value > self.maxValue:
            self.setCurrentTotalDigits(3)
            return self.primitiveLongSingleton.UNK
        index: int = 0
        div: int = self.powerOfTen
        lastValue: int = 0
        while div >= 1:
            digit: int = int((value - lastValue) / div)
            if digit >= 0 and digit < 10:
                if digit == 0 and index == 0:
                    pass
                else:
                    self.charArray[((index := index + 1) - 1)] = self.primitiveLongSingleton.NUMBER_CHAR_ARRAY[digit]
                lastValue += digit * div
            div = int(div / 10)
        self.setCurrentTotalDigits(index)
        return self.charArray
    

    def setCurrentTotalDigits(self, currentTotalDigits: int) -> None:
        self.currentTotalDigits = currentTotalDigits
    

    def getCurrentTotalDigits(self) -> int:
        return self.currentTotalDigits
    

    def getMaxDigits(self) -> int:
        return self.maxDigits
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton


