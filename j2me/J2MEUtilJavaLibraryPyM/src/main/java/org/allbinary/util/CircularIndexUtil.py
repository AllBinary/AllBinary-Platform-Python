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



class CircularIndexUtil:
    NULL_CIRCULAR_INDEX_UTIL: CircularIndexUtil = None

    def _init_fields(self) -> None:
        self.index: int = 0
        self.lastIndex: int = 0
        self.size: int = 0
    

    def __init__(self, index: int, size: int) -> None:
        self._init_fields()
        self.setSize(size)
        self.setIndex(index)
    

    def next(self) -> int:
        if self.index >= self.lastIndex:
            self.index = 0
        else:
            self.index += 1
        return self.index
    

    def previous(self) -> int:
        if self.index < 1:
            self.index = self.lastIndex
        else:
            self.index -= 1
        return self.index
    

    def setIndex(self, index: int) -> None:
        if index > self.lastIndex:
            return
        self.index = index
    

    def getIndex(self) -> int:
        return self.index
    

    @staticmethod
    def createInstance(max: int) -> CircularIndexUtil:
        return CircularIndexUtil(0, max)
    

    @staticmethod
    def createInstanceAt(index: int, max: int) -> CircularIndexUtil:
        return CircularIndexUtil(index, max)
    

    def setSize(self, size: int) -> None:
        self.size = size
        self.lastIndex = size - 1
        self.index = 0
    

    def getSize(self) -> int:
        return self.size
    

    def toString(self) -> str:
        return str(StringMaker().append(CommonLabels.getInstance().INDEX_LABEL).appendint(self.index).append("lastIndex: ").appendint(self.lastIndex).append("size: ").appendint(self.size))

    def __str__(self) -> str:
        return self.toString()
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty


CircularIndexUtil.NULL_CIRCULAR_INDEX_UTIL = CircularIndexUtil(0, 0)

