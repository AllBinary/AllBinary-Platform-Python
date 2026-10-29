# Generated Code Do Not Modify
# package org.allbinary.util

from __future__ import annotations



#This is a very fast and simple resizable list.
class BasicArrayList:
    SIZE: str = ", Size: "

    def _init_fields(self) -> None:
        self.arrayUtil: ArrayUtil = ArrayUtil.getInstance()
        self.objectArray: list[object] = None
        self.currentIndex: int = 0
    

    def __init__(self, objectArray: list[object]) -> None:
        self._init_fields()
        self.objectArray = objectArray
    

    def addAt(self, index: int, element: object) -> None:
        if index > self.currentIndex or index < 0:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(CommonLabels.getInstance().INDEX_LABEL)
            stringBuffer.appendint(index)
            stringBuffer.append(BasicArrayList.SIZE)
            stringBuffer.appendint(self.currentIndex)
            raise IndexError(str(stringBuffer))
        self.ensureCapacity(self.currentIndex + 1)
        self.objectArray[index + 1:index + 1 + self.currentIndex - index] = self.objectArray[index:index + self.currentIndex - index]
        self.objectArray[index] = element
        self.currentIndex += 1
    

    def add(self, anyType: object) -> bool:
        self.ensureCapacity(self.currentIndex + 1)
        self.objectArray[((setattr(self, "currentIndex", self.currentIndex + 1) or self.currentIndex) - 1)] = anyType
        return True
    

    def removeAt(self, index: int) -> object:
        if index >= self.currentIndex:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(CommonLabels.getInstance().INDEX_LABEL)
            stringBuffer.appendint(index)
            stringBuffer.append(BasicArrayList.SIZE)
            stringBuffer.appendint(self.currentIndex)
            raise IndexError(str(stringBuffer))
        oldValue: object = self.objectArray[index]
        numMoved: int = self.currentIndex - index - 1
        if numMoved > 0:
            self.objectArray[index:index + numMoved] = self.objectArray[index + 1:index + 1 + numMoved]
        self.objectArray[(setattr(self, "currentIndex", self.currentIndex - 1) or self.currentIndex)] = None
        return oldValue
    

    def remove(self, anyType: object) -> bool:
        if anyType is None:
            for index in range(0, self.currentIndex):
                if self.objectArray[index] is None:
                    numMoved: int = self.currentIndex - index - 1
                    if numMoved > 0:
                        self.objectArray[index:index + numMoved] = self.objectArray[index + 1:index + 1 + numMoved]
                    self.objectArray[(setattr(self, "currentIndex", self.currentIndex - 1) or self.currentIndex)] = None
                    return True
        else:
            for index in range(0, self.currentIndex):
                if anyType == self.objectArray[index] or anyType.equals(self.objectArray[index]):
                    numMoved: int = self.currentIndex - index - 1
                    if numMoved > 0:
                        self.objectArray[index:index + numMoved] = self.objectArray[index + 1:index + 1 + numMoved]
                    self.objectArray[(setattr(self, "currentIndex", self.currentIndex - 1) or self.currentIndex)] = None
                    return True
        return False
    

    def removeAll2(self, list_: BasicArrayList) -> bool:
        result: bool = True
        size: int = list_.size()
        for index in range(0, size):
            if self.remove(list_.get(index)):
                pass
            else:
                result = False
        return result
    

    def addAll2(self, list_: BasicArrayList) -> bool:
        self.ensureCapacity(self.currentIndex + list_.currentIndex)
        listSize: int = list_.currentIndex
        for index in range(0, listSize):
            self.objectArray[((setattr(self, "currentIndex", self.currentIndex + 1) or self.currentIndex) - 1)] = list_.objectArray[index]
        return True
    

    def addAllList(self, list_: BasicArrayList) -> bool:
        newObjectArray: list[object] = list_.toArray()
        return self.addAll(newObjectArray)
    

    def addAll(self, newObjectArray: list[object]) -> bool:
        numSize: int = len(newObjectArray)
        self.ensureCapacity(self.currentIndex + numSize)
        self.objectArray[self.currentIndex:self.currentIndex + numSize] = newObjectArray[0:0 + numSize]
        self.currentIndex += numSize
        return numSize != 0
    

    def ensureCapacity(self, minSize: int) -> None:
        oldCapacity: int = len(self.objectArray)
        if minSize > oldCapacity:
            newCapacity: int = ((oldCapacity * 3) >> 1) + 1
            if newCapacity < minSize:
                newCapacity = minSize
            self.objectArray = self.arrayUtil.copyOf(self.objectArray, newCapacity)
    

    def trimToSize(self) -> None:
        oldCapacity: int = len(self.objectArray)
        if self.currentIndex < oldCapacity:
            self.objectArray = self.arrayUtil.copyOf(self.objectArray, self.currentIndex)
    

    def indexOf(self, anyType: object) -> int:
        if anyType is None:
            for i in range(0, self.currentIndex):
                if self.objectArray[i] is None:
                    return i
        else:
            for i in range(0, self.currentIndex):
                if anyType.equals(self.objectArray[i]):
                    return i
        return -1
    

    def lastIndexOf(self, anyType: object) -> int:
        if anyType is None:
            for i in range(self.currentIndex - 1, 0 - 1, -1):
                if self.objectArray[i] is None:
                    return i
        else:
            for i in range(self.currentIndex - 1, 0 - 1, -1):
                if anyType.equals(self.objectArray[i]):
                    return i
        return -1
    

    def get(self, index: int) -> object:
        if index >= self.currentIndex:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(CommonLabels.getInstance().INDEX_LABEL)
            stringBuffer.appendint(index)
            stringBuffer.append(BasicArrayList.SIZE)
            stringBuffer.appendint(self.currentIndex)
            raise IndexError(str(stringBuffer))
        return self.objectArray[index]
    

    def set(self, index: int, element: object) -> object:
        if index >= self.currentIndex:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(CommonLabels.getInstance().INDEX_LABEL)
            stringBuffer.appendint(index)
            stringBuffer.append(BasicArrayList.SIZE)
            stringBuffer.appendint(self.currentIndex)
            raise IndexError(str(stringBuffer))
        oldValue: object = self.objectArray[index]
        self.objectArray[index] = element
        return oldValue
    

    def clear(self) -> None:
        for i in range(0, self.currentIndex):
            self.objectArray[i] = None
        self.currentIndex = 0
    

    def size(self) -> int:
        return self.currentIndex
    

    def isEmpty(self) -> bool:
        return self.currentIndex == 0
    

    def contains(self, anyType: object) -> bool:
        return self.indexOf(anyType) >= 0
    

    def toArray(self) -> list[object]:
        return self.arrayUtil.copyOf(self.objectArray, self.currentIndex)
    

    def toArrayType(self, objectArray: list[object]) -> list[object]:
        if len(objectArray) < self.currentIndex:
            return self.arrayUtil.copyOfType(self.objectArray, self.currentIndex, type(objectArray))
        objectArray[0:0 + self.currentIndex] = self.objectArray[0:0 + self.currentIndex]
        if len(objectArray) > self.currentIndex:
            objectArray[self.currentIndex] = None
        return objectArray
    

    def clone(self) -> object:
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
        size: int = self.size()
        list_: BasicArrayList = BasicArrayListS(size)
        anyType: object = None
        for index in range(0, size):
            anyType = self.objectArray[index]
            list_.add(anyType)
        return list_
    

    def toString(self) -> str:
        COMMA_SEP: str = CommonSeps.getInstance().COMMA_SEP
        stringBuffer: StringMaker = StringMaker()
        for index in range(0, self.currentIndex):
            stringBuffer.append(str(self.objectArray[index]))
            stringBuffer.append(COMMA_SEP)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty
from org.allbinary.util.ArrayUtil import ArrayUtil


