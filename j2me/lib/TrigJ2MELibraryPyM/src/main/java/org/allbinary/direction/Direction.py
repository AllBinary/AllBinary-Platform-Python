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
# package org.allbinary.direction

from __future__ import annotations



class Direction:
    directionArray: list[Direction] = None

    def _init_fields(self) -> None:
        self.name: str = None
        self.otherName: str = None
        self.value: int = None
        self.frameFactor: int = None
    

    def __init__(self, name: str, otherName: str, value: int, frameFactor: int) -> None:
        self._init_fields()
        self.name = name
        self.otherName = otherName
        self.value = value
        self.frameFactor = frameFactor
        Direction.directionArray[value] = self
    

    @staticmethod
    def getInstance(direction: int) -> Direction:
        return Direction.directionArray[direction]
    

    def getValue(self) -> int:
        return self.value
    

    def getFrameFactor(self) -> int:
        return self.frameFactor
    

    def getOtherName(self) -> str:
        return self.otherName
    

    def getName(self) -> str:
        return self.name
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Direction: ")
        stringBuffer.append(self.getName())
        stringBuffer.append(" Or: ")
        stringBuffer.append(self.getOtherName())
        stringBuffer.append(" Value: ")
        stringBuffer.appendint(self.value)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker


Direction.directionArray = [None] * (13)

