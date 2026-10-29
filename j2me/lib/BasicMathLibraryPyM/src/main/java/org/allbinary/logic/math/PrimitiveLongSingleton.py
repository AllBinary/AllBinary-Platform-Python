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



class PrimitiveLongSingleton:
    instance: PrimitiveLongSingleton = None

    def _init_fields(self) -> None:
        self.UNK: list[str] = ['U', 'n', 'k']
        self.NUMBER_ARRAY: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.NUMBER_CHAR_ARRAY: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.NUMBER_CHAR_ARRAYS: list[list[str]] = [['0'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']]
        self.ZERO: list[str] = [self.NUMBER_CHAR_ARRAY[0]]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PrimitiveLongSingleton:
        return PrimitiveLongSingleton.instance
    

    # throws Exception
    def getNumberFromChar(self, numberAsChar: str) -> int:
        size: int = len(self.NUMBER_CHAR_ARRAY)
        for index in range(0, size):
            if self.NUMBER_CHAR_ARRAY[index] == numberAsChar:
                return self.NUMBER_ARRAY[index]
        raise Exception(str(StringMaker().append("numberAsChar was not in array: ").appendchar(numberAsChar)))
from org.allbinary.logic.string.StringMaker import StringMaker


PrimitiveLongSingleton.instance = PrimitiveLongSingleton()

