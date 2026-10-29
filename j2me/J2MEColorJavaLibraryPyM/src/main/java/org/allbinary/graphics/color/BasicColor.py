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
# package org.allbinary.graphics.color

from __future__ import annotations



class BasicColor:

    def _init_fields(self) -> None:
        self.name: str = None
        self.value: int = None
        self.redComponent: float = None
        self.greenComponent: float = None
        self.blueComponent: float = None
        self.alphaComponent: float = None
        self.red: int = None
        self.green: int = None
        self.blue: int = None
        self.alpha: int = None
    

    def __init__(self, alphaValue: int, value: int, name: str) -> None:
        from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil
        self._init_fields()
        self.name = name
        tempValue: int = 0
        basicColorUtil: BasicColorUtil = BasicColorUtil.getInstance()
        if basicColorUtil.isAlpha:
            if basicColorUtil.ffOpaque:
                tempValue = alphaValue | value
            else:
                tempValue = 0x00000000 | value
        else:
            tempValue = value
        alphaInt: int = ((tempValue >> 24) & 255)
        self.alpha = ((int(alphaInt) + 32768) % 65536 - 32768)
        self.alphaComponent = (float(alphaInt)) / 255.0
        redInt: int = ((tempValue >> 16) & 255)
        self.red = ((int(redInt) + 32768) % 65536 - 32768)
        self.redComponent = (float(redInt)) / 255.0
        greenInt: int = ((tempValue >> 8) & 255)
        self.green = ((int(greenInt) + 32768) % 65536 - 32768)
        self.greenComponent = (float(greenInt)) / 255.0
        blueInt: int = ((tempValue) & 255)
        self.blue = ((int(blueInt) + 32768) % 65536 - 32768)
        self.blueComponent = (float(blueInt)) / 255.0
        self.value = tempValue
    

    def intValue(self) -> int:
        return self.value
    

    def toInt(self) -> int:
        return self.value
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("BasicColor: ")
        stringBuffer.append("Alpha: ")
        stringBuffer.appendshort(self.alpha)
        stringBuffer.append(" Red: ")
        stringBuffer.appendshort(self.red)
        stringBuffer.append(" Green: ")
        stringBuffer.appendshort(self.green)
        stringBuffer.append(" Blue: ")
        stringBuffer.appendshort(self.blue)
        stringBuffer.append(" Value: ")
        stringBuffer.appendint(self.value)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getName(self) -> str:
        return self.name
    

    def getRedComponent(self) -> float:
        return self.redComponent
    

    def getGreenComponent(self) -> float:
        return self.greenComponent
    

    def getBlueComponent(self) -> float:
        return self.blueComponent
    

    def getAlphaComponent(self) -> float:
        return self.alphaComponent
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.string.StringMaker import StringMaker
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty


