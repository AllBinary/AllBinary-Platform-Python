# Generated Code Do Not Modify
# package org.allbinary.util

from __future__ import annotations



class ArrayUtil:
    instance: ArrayUtil = None

    def _init_fields(self) -> None:
        self.mathUtil: MathUtil = MathUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ArrayUtil:
        return ArrayUtil.instance
    

    def copyOf(self, original: list[object], newLength: int) -> list[object]:
        return self.copyOfType(original, newLength, type(original))
    

    def copyOfType(self, original: list[object], newLength: int, newType: type) -> list[object]:
        copy: list[object] = [None] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOfbyte(self, original: list[int], newLength: int) -> list[int]:
        copy: list[int] = [0] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOfshort(self, original: list[int], newLength: int) -> list[int]:
        copy: list[int] = [0] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOfint(self, original: list[int], newLength: int) -> list[int]:
        copy: list[int] = [0] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOflong(self, original: list[int], newLength: int) -> list[int]:
        copy: list[int] = [0] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOfchar(self, original: list[str], newLength: int) -> list[str]:
        copy: list[str] = ['\0'] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOffloat(self, original: list[float], newLength: int) -> list[float]:
        copy: list[float] = [0.0] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOfdouble(self, original: list[float], newLength: int) -> list[float]:
        copy: list[float] = [0.0] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def copyOfboolean(self, original: list[bool], newLength: int) -> list[bool]:
        copy: list[bool] = [False] * (newLength)
        copy[0:0 + self.mathUtil.min(len(original), newLength)] = original[0:0 + self.mathUtil.min(len(original), newLength)]
        return copy
    

    def reverse(self, intArray: list[int]) -> None:
        length: int = len(intArray) - 1
        temp: int = 0
        size: int = int(length / 2)
        for index in range(0, size + 1):
            temp = intArray[index]
            intArray[index] = intArray[length - index]
            intArray[length - index] = temp
    

    def flip(self, intArray: list[int], width: int, height: int) -> None:
        length: int = height - 1
        temp: int = 0
        index: int = 0
        rowIndex: int = 0
        for y in range(0, int(length / 2) + 1):
            for x in range(0, width):
                rowIndex = ((length - y) * width)
                index = x + (y * width)
                temp = intArray[index]
                intArray[index] = intArray[rowIndex + x]
                intArray[rowIndex + x] = temp
    

    def toStringFromTwoDimensionaArray(self, twoDimensionalIntArray: list[list[int]]) -> str:
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        endIndex: int = len(twoDimensionalIntArray)
        endIndex2: int = len(twoDimensionalIntArray[0])
        for index in range(0, endIndex):
            stringBuffer.append(commonSeps.BRACE_OPEN)
            for index2 in range(0, endIndex2):
                stringBuffer.appendint(int(twoDimensionalIntArray[index][index2]))
                stringBuffer.append(commonSeps.COMMA_SEP)
            stringBuffer.append(commonSeps.BRACE_CLOSE)
            stringBuffer.append(commonSeps.NEW_LINE)
        return str(stringBuffer)
    

    def toStringFromObjectArray(self, objectArray: list[object]) -> str:
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        for index in range(0, len(objectArray)):
            stringBuffer.append(StringUtil.getInstance().toString(objectArray[index]))
            stringBuffer.append(commonSeps.COMMA_SEP)
        return str(stringBuffer)
    

    def toStringFromByteArray(self, byteArray: list[int]) -> str:
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        for index in range(0, len(byteArray)):
            stringBuffer.appendbyte(byteArray[index])
            stringBuffer.append(commonSeps.COMMA_SEP)
        return str(stringBuffer)
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from jsinterop.annotations.JsMethod import JsMethod


ArrayUtil.instance = ArrayUtil()

