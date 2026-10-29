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
# package org.allbinary.game.rand

from __future__ import annotations

import random
import time


#Do not use in client code for money related things.
class MyRandomFactory:
    instance: MyRandomFactory = None

    def _init_fields(self) -> None:
        self.mathUtil: MathUtil = MathUtil.getInstance()
        self.rand: random.Random = None
    

    @staticmethod
    def getInstance() -> MyRandomFactory:
        return MyRandomFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
        self.rand = random.Random(int(time.time() * 1000))
    

    def setSeed(self, seed: int) -> None:
        self.rand = random.Random(seed)
    

    def getNextInt(self, range: int) -> int:
        div: int = (2147483647 / range) + 1
        return int((self.rand.randint(-2147483648, 2147483647) / div))
    

    def getAbsoluteNextInt(self, range: int) -> int:
        return self.mathUtil.abs(self.getNextInt(range))
    

    def getAbsoluteNextIntAllowZero(self, range: int) -> int:
        if range == 0:
            return 0
        else:
            return self.mathUtil.abs(self.getNextInt(range))
    

    def shuffle(self, intArray: list[int]) -> None:
        self.shuffleTotal(intArray, len(intArray) * 7)
    

    def shuffleTotal(self, intArray: list[int], shuffleTotal: int) -> None:
        size: int = len(intArray)
        randomIndex: int = 0
        randomIndex2: int = 0
        value: int = 0
        for index in range(0, shuffleTotal):
            randomIndex = self.getAbsoluteNextIntAllowZero(size)
            randomIndex2 = self.getAbsoluteNextIntAllowZero(size)
            value = intArray[randomIndex]
            intArray[randomIndex] = intArray[randomIndex2]
            intArray[randomIndex2] = value
    

    def shuffle2(self, intArray: list[int], intArray2: list[int]) -> None:
        self.shuffle2Total(intArray, intArray2, len(intArray) * 7)
    

    def shuffle2Total(self, intArray: list[int], intArray2: list[int], shuffleTotal: int) -> None:
        size: int = len(intArray)
        randomIndex: int = 0
        randomIndex2: int = 0
        value: int = 0
        value2: int = 0
        for index in range(0, shuffleTotal):
            randomIndex = self.getAbsoluteNextIntAllowZero(size)
            randomIndex2 = self.getAbsoluteNextIntAllowZero(size)
            value = intArray[randomIndex]
            value2 = intArray2[randomIndex]
            intArray[randomIndex] = intArray[randomIndex2]
            intArray[randomIndex2] = value
            intArray2[randomIndex] = intArray2[randomIndex2]
            intArray2[randomIndex2] = value2
    

    @staticmethod
    def main(args: list[str]) -> None:
        randomFactory: MyRandomFactory = MyRandomFactory.getInstance()
        stringBuilder: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        size2: int = 100
        for index in range(0, size2):
            stringBuilder.appendint(int(randomFactory.getAbsoluteNextInt(3))).append(commonSeps.COMMA)
        print(str(stringBuilder))
        stringBuilder.delete(0, stringBuilder.length())
        intArray: list[int] = [0] * (52)
        intArray2: list[int] = [0] * (52)
        size: int = len(intArray)
        for index in range(0, size):
            intArray[index] = index
            intArray2[index] = index
        randomFactory.shuffle2(intArray, intArray2)
        for index in range(0, size):
            stringBuilder.appendint(intArray[index]).append(commonSeps.COMMA)
        print(str(stringBuilder))
        stringBuilder.delete(0, stringBuilder.length())
        for index in range(0, size):
            stringBuilder.appendint(intArray2[index]).append(commonSeps.COMMA)
        print(str(stringBuilder))
        found: bool = False
        for index in range(0, size):
            found = False
            for index2 in range(0, size):
                if intArray[index2] == index:
                    found = True
            if not found:
                raise RuntimeError()
# from java.util.Random import Random
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


MyRandomFactory.instance = MyRandomFactory()

