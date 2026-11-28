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

from java.lang.JavaRuntimeStatic import java_divide


class BasicColor:

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "value" not in vars(self): self.value: int = 0
        if "redComponent" not in vars(self): self.redComponent: float = 0.0
        if "greenComponent" not in vars(self): self.greenComponent: float = 0.0
        if "blueComponent" not in vars(self): self.blueComponent: float = 0.0
        if "alphaComponent" not in vars(self): self.alphaComponent: float = 0.0
        if "red" not in vars(self): self.red: int = 0
        if "green" not in vars(self): self.green: int = 0
        if "blue" not in vars(self): self.blue: int = 0
        if "alpha" not in vars(self): self.alpha: int = 0
    

    def __init__(self, alphaValue: int, value: int, name: str) -> None:
        from org.allbinary.graphics.color.BasicColorUtil import BasicColorUtil
        from jsinterop.annotations.JsConstructor import JsConstructor
        __class__._init_fields(self)
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
        alphaInt: int = ((int(tempValue) >> (int(24) & 31)) & 255)
        self.alpha = ((int(alphaInt) + 32768) % 65536 - 32768)
        self.alphaComponent = (float(alphaInt)) / 255.0
        redInt: int = ((int(tempValue) >> (int(16) & 31)) & 255)
        self.red = ((int(redInt) + 32768) % 65536 - 32768)
        self.redComponent = (float(redInt)) / 255.0
        greenInt: int = ((int(tempValue) >> (int(8) & 31)) & 255)
        self.green = ((int(greenInt) + 32768) % 65536 - 32768)
        self.greenComponent = (float(greenInt)) / 255.0
        blueInt: int = ((tempValue) & 255)
        self.blue = ((int(blueInt) + 32768) % 65536 - 32768)
        self.blueComponent = (float(blueInt)) / 255.0
        self.value = tempValue
    

    def intValue(self) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.value
    __int__ = intValue
    

    def toInt(self) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.value
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from jsinterop.annotations.JsMethod import JsMethod
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
        from jsinterop.annotations.JsMethod import JsMethod
        return self.name
    

    def getRedComponent(self) -> float:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.redComponent
    

    def getGreenComponent(self) -> float:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.greenComponent
    

    def getBlueComponent(self) -> float:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.blueComponent
    

    def getAlphaComponent(self) -> float:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.alphaComponent
# from jsinterop.annotations.JsType import JsType
# from org.allbinary.logic.string.StringMaker import StringMaker
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor
# from jsinterop.annotations.JsProperty import JsProperty


