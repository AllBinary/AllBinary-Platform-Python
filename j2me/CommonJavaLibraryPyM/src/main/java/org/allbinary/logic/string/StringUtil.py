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
# package org.allbinary.logic.string

from __future__ import annotations



class StringUtil:
    instance: StringUtil = None

    def _init_fields(self) -> None:
        self.INIT_STRING: str = str("")
        self.NULL_STRING: str = "null"
        self.EMPTY_STRING: str = ""
        self.ONE_EMPTY_STRING_ARRAY: list[str] = [self.EMPTY_STRING]
        self.stringArray: list[str] = [None] * (0)
    

    @staticmethod
    def getInstance() -> StringUtil:
        return StringUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getNonNull(self, string: str) -> str:
        if string is None:
            return self.EMPTY_STRING
        else:
            return string
    

    def getArrayInstance(self) -> list[str]:
        return self.stringArray
    

    def count(self, string: str, aChar: str) -> int:
        count: int = 0
        size: int = len(string)
        for index in range(0, size):
            if string[index] == aChar:
                count += 1
        return count
    

    def toString(self, anyType: object) -> str:
        if anyType is not None:
            return str(anyType)
        else:
            return self.NULL_STRING
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty


StringUtil.instance = StringUtil()

