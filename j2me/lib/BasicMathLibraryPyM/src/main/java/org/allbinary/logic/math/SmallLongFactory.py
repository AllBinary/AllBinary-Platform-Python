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



class SmallLongFactory:
    instance: SmallLongFactory = None

    def _init_fields(self) -> None:
        self.NEGATIVE_MAX: int = 500
        self.POSITIVE_MAX: int = 0x2D1
        self.INTEGER_ARRAY: list[int] = [None] * (self.NEGATIVE_MAX + self.POSITIVE_MAX)
        self.STRING_ARRAY: list[str] = [None] * (self.NEGATIVE_MAX + self.POSITIVE_MAX)
        self.MIN: int = 0
        self.lastMin: int = 0
        self.lastNegativeMin: int = 0
    

    @staticmethod
    def getInstance() -> SmallLongFactory:
        return SmallLongFactory.instance
    

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
        if self.INTEGER_ARRAY[0] is None:
            if self.lastMin < self.POSITIVE_MAX or self.lastNegativeMin < self.NEGATIVE_MAX:
                for index in range(self.POSITIVE_MAX - 1, self.lastMin - 1, -1):
                    self.INTEGER_ARRAY[index + self.NEGATIVE_MAX] = int(index)
                for index in range(self.NEGATIVE_MAX - 1, self.lastNegativeMin - 1, -1):
                    self.INTEGER_ARRAY[index] = int(-index)
                self.lastMin = self.POSITIVE_MAX
                self.lastNegativeMin = self.NEGATIVE_MAX
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getInstanceNoThrow(self, index: int) -> int:
        if index + self.NEGATIVE_MAX > len(self.INTEGER_ARRAY) - 1:
            return self.INTEGER_ARRAY[-1 + self.NEGATIVE_MAX]
        return self.INTEGER_ARRAY[(index) + self.NEGATIVE_MAX]
    

    def getString(self, index: int) -> str:
        i: int = index + self.NEGATIVE_MAX
        if self.STRING_ARRAY[i] is None:
            self.STRING_ARRAY[i] = str(self.INTEGER_ARRAY[i])
        return self.STRING_ARRAY[i]


SmallLongFactory.instance = SmallLongFactory()

