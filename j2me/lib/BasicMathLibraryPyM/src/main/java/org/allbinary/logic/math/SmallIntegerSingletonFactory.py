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



class SmallIntegerSingletonFactory:
    instance: SmallIntegerSingletonFactory = None

    def _init_fields(self) -> None:
        self.NEGATIVE_MAX: int = 500
        self.POSITIVE_MAX: int = 0x2D1
        self.INTEGER_ARRAY: list[int] = [None] * (self.NEGATIVE_MAX + self.POSITIVE_MAX)
        self.STRING_ARRAY: list[str] = [None] * (self.NEGATIVE_MAX + self.POSITIVE_MAX)
        self.MIN: int = 0
        self.lastMin: int = 0
        self.lastNegativeMin: int = 0
    

    @staticmethod
    def getInstance() -> SmallIntegerSingletonFactory:
        return SmallIntegerSingletonFactory.instance
    

    def getMin(self) -> int:
        minAllowed: int = self.getMinAllowed()
        if self.MIN <= minAllowed:
            if J2MEUtil.isJ2ME():
                pass
            elif AndroidUtil.isAndroid():
                logUtil: LogUtil = LogUtil.getInstance()
                logUtil.putF(str(StringMaker().append("Android InputFactory was initialized before GameMidlet: ").appendint(self.MIN)), self, "getMin")
                self.initWithRange(0x291, 6)
            else:
                logUtil: LogUtil = LogUtil.getInstance()
                logUtil.putF(str(StringMaker().append("InputFactory was initialized before GameMidlet or KeyFactoryInitializer - Currently this is occurs on JS build by TouchMotionGestureFactory constructor: ").appendint(self.MIN)), self, "getMin")
                self.initWithRange(0x2D0, 6)
        if self.MIN <= minAllowed:
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.put("This means you loaded the InputFactory before determining the platform input size requirements.", self, "getMin", Exception())
        return self.MIN
    

    def getMinAllowed(self) -> int:
        if J2MEUtil.isJ2ME():
            return 0
        else:
            if AndroidUtil.isAndroid():
                return 0x101
            else:
                return 23
    

    def initWithRange(self, value: int, negativeValue: int) -> None:
        for index in range(value - 1, self.lastMin - 1, -1):
            self.INTEGER_ARRAY[index + self.NEGATIVE_MAX] = int(index)
        for index in range(negativeValue - 1, self.lastNegativeMin - 1, -1):
            self.INTEGER_ARRAY[index] = int(-index)
        if self.lastMin < value:
            self.lastMin = value
            self.MIN = value
        if self.lastNegativeMin < negativeValue:
            self.lastNegativeMin = negativeValue
    

    def init(self) -> None:
        if self.lastMin < self.POSITIVE_MAX or self.lastNegativeMin < self.NEGATIVE_MAX:
            for index in range(self.POSITIVE_MAX - 1, self.lastMin - 1, -1):
                self.INTEGER_ARRAY[index + self.NEGATIVE_MAX] = int(index)
            for index in range(self.NEGATIVE_MAX - 1, self.lastNegativeMin - 1, -1):
                self.INTEGER_ARRAY[index] = int(-index)
            self.lastMin = self.POSITIVE_MAX
            self.MIN = self.lastMin
            self.lastNegativeMin = self.NEGATIVE_MAX
    

    def __init__(self) -> None:
        self._init_fields()
        self.initWithRange(23, 0)
    

    def getAt(self, index: int) -> int:
        return self.INTEGER_ARRAY[index + self.NEGATIVE_MAX]
    

    def getAtNoThrow(self, index: int) -> int:
        if index + self.NEGATIVE_MAX > len(self.INTEGER_ARRAY) - 1:
            return self.INTEGER_ARRAY[-1 + self.NEGATIVE_MAX]
        return self.INTEGER_ARRAY[index + self.NEGATIVE_MAX]
    

    def createInstance(self, index: int) -> int:
        integer: int = self.getAt(index)
        if integer is None:
            integer = int(index)
        return integer
    

    def getString(self, index: int) -> str:
        i: int = index + self.NEGATIVE_MAX
        if self.STRING_ARRAY[i] is None:
            self.STRING_ARRAY[i] = str(self.INTEGER_ARRAY[i])
        return self.STRING_ARRAY[i]
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


SmallIntegerSingletonFactory.instance = SmallIntegerSingletonFactory()

