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

from java.lang.JavaRuntimeStatic import lazy_static


class CircularIndexUtil:
    NULL_CIRCULAR_INDEX_UTIL: CircularIndexUtil = None

    def _init_fields(self) -> None:
        self.index: int = 0
        self.lastIndex: int = 0
        self.size: int = 0
    

    def __init__(self, index: int, size: int) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        self._init_fields()
        self.setSize(size)
        self.setIndex(index)
    

    def next(self) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        if self.index >= self.lastIndex:
            self.index = 0
        else:
            self.index += 1
        return self.index
    

    def previous(self) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        if self.index < 1:
            self.index = self.lastIndex
        else:
            self.index -= 1
        return self.index
    

    def setIndex(self, index: int) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        if index > self.lastIndex:
            return
        self.index = index
    

    def getIndex(self) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.index
    

    @staticmethod
    def createInstance(max: int) -> CircularIndexUtil:
        from jsinterop.annotations.JsMethod import JsMethod
        return CircularIndexUtil(0, max)
    

    @staticmethod
    def createInstanceAt(index: int, max: int) -> CircularIndexUtil:
        from jsinterop.annotations.JsMethod import JsMethod
        return CircularIndexUtil(index, max)
    

    def setSize(self, size: int) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        self.size = size
        self.lastIndex = size - 1
        self.index = 0
    

    def getSize(self) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.size
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonLabels import CommonLabels
        from jsinterop.annotations.JsMethod import JsMethod
        return str(StringMaker().append(CommonLabels.getInstance().INDEX_LABEL).appendint(self.index).append("lastIndex: ").appendint(self.lastIndex).append("size: ").appendint(self.size))

    def __str__(self) -> str:
        return self.toString()
# from jsinterop.annotations.JsType import JsType
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonLabels import CommonLabels
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor
# from jsinterop.annotations.JsProperty import JsProperty


def _CircularIndexUtil_NULL_CIRCULAR_INDEX_UTIL() -> object:
    return CircularIndexUtil(0, 0)

lazy_static(CircularIndexUtil, "NULL_CIRCULAR_INDEX_UTIL", _CircularIndexUtil_NULL_CIRCULAR_INDEX_UTIL)

