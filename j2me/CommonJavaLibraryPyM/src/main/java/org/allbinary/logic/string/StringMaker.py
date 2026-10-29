# Generated Code Do Not Modify
# package org.allbinary.logic.string

from __future__ import annotations



class StringMaker:

    def _init_fields(self) -> None:
        self.charArray: list[str] = None
        self.currentLength: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
        self.charArray = ['\0'] * (20)
    

    def append(self, string: str) -> StringMaker:
        stringLength: int = len(string)
        self.ensureCapacity(self.currentLength + stringLength)
        self.charArray[self.currentLength:self.currentLength + (stringLength - 0)] = list(string[0:stringLength])
                    
        self.currentLength += stringLength
        return self
    

    def appendchar(self, c: str) -> StringMaker:
        self.ensureCapacity(self.currentLength + 1)
        self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = c
        return self
    

    def appendCharArray(self, charArray: list[str], start: int, end: int) -> StringMaker:
        self.ensureCapacity(self.currentLength + (end - start))
        for index in range(start, end):
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = charArray[index]
        return self
    

    def appendbyte(self, b: int) -> StringMaker:
        self.append(str(b))
        return self
    

    def appendshort(self, b: int) -> StringMaker:
        self.append(str(b))
        return self
    

    def appendint(self, i: int) -> StringMaker:
        self.append(str(i))
        return self
    

    def appendlong(self, l: int) -> StringMaker:
        self.append(str(l))
        return self
    

    def appendfloat(self, f: float) -> StringMaker:
        self.append(str(f))
        return self
    

    def appendboolean(self, bool: bool) -> StringMaker:
        if bool:
            self.ensureCapacity(self.currentLength + 4)
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 't'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'r'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'u'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'e'
        else:
            self.ensureCapacity(self.currentLength + 5)
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'f'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'a'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'l'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 's'
            self.charArray[((setattr(self, "currentLength", self.currentLength + 1) or self.currentLength) - 1)] = 'e'
        return self
    

    def ensureCapacity(self, minSize: int) -> None:
        oldCapacity: int = len(self.charArray)
        if minSize > oldCapacity:
            newCapacity: int = oldCapacity * 3
            if newCapacity < minSize:
                newCapacity = minSize
            copy: list[str] = ['\0'] * (newCapacity)
            min: int = self.min(len(self.charArray), newCapacity)
            copy[0:0 + min] = self.charArray[0:0 + min]
            self.charArray = copy
    

    def min(self, value: int, value2: int) -> int:
        return (value if (value <= value2) else value2)
    

    def delete(self, start: int, end: int) -> StringMaker:
        self.currentLength -= (end - start)
        return self
    

    def length(self) -> int:
        return self.currentLength
    

    def toString(self) -> str:
        return "".join(self.charArray[0:0 + self.currentLength])

    def __str__(self) -> str:
        return self.toString()
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor


