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
# package org.allbinary.util

from __future__ import annotations



class BasicArrayListUtil:
    instance: BasicArrayListUtil = None

    def _init_fields(self) -> None:
        self.NULL_ARRAY_OF_ARRAY: list[list[BasicArrayList]] = [[None] * (0) for _ in range(0)]
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
        self.immutableInstance: BasicArrayList = ImmutableBasicArrayList("Immutable", 0)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicArrayListUtil:
        return BasicArrayListUtil.instance
    

    def getRandom(self, list_: BasicArrayList) -> object:
        i_random: int = self.getRandomIndex(list_)
        return list_.objectArray[i_random]
    

    def getRandomIndex(self, list_: BasicArrayList) -> int:
        return self.myRandomFactory.getAbsoluteNextInt(list_.size())
    

    def reverse(self, list_: BasicArrayList) -> None:
        lastMinusOneIndex: int = list_.size() - 2
        temp: object = None
        size: int = int(lastMinusOneIndex / 2)
        secondSwapIndex: int = 0
        for index in range(0, size + 1):
            secondSwapIndex = lastMinusOneIndex - index
            temp = list_.removeAt(index)
            list_.addAt(index, list_.removeAt(secondSwapIndex))
            list_.addAt(secondSwapIndex + 1, temp)
    

    def log(self, list_: BasicArrayList) -> str:
        S_LABEL: str = " s: "
        size: int = list_.size()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(CommonLabels.getInstance().TOTAL_LABEL)
        stringBuffer.appendint(size)
        for index in range(size - 1, 0 - 1, -1):
            usedList: BasicArrayList = list_.objectArray[index]
            stringBuffer.append(S_LABEL)
            stringBuffer.appendint(usedList.size())
        return str(stringBuffer)
    

    def getImmutableInstance(self) -> BasicArrayList:
        return self.immutableInstance
    

    @staticmethod
    def main(args: list[str]) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        list_: BasicArrayList = BasicArrayListD()
        list_.add(commonPhoneStrings.ONE)
        list_.add(commonPhoneStrings.TWO)
        list_.add(commonPhoneStrings.THREE)
        list_.add(commonPhoneStrings.FOUR)
        list_.add(commonPhoneStrings.FIVE)
        list_.add(commonPhoneStrings.SIX)
        list_.add(commonPhoneStrings.SEVEN)
        list_.add(commonPhoneStrings.EIGHT)
        list_.add(commonPhoneStrings.NINE)
        BasicArrayListUtil.getInstance().reverse(list_)
        print(str(list_))
from jsinterop.annotations.JsType import JsType
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty
from org.allbinary.util.ImmutableBasicArrayList import ImmutableBasicArrayList


BasicArrayListUtil.instance = BasicArrayListUtil()

