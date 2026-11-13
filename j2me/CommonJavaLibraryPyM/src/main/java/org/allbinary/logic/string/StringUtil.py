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

from java.lang.JavaRuntimeStatic import lazy_static


class StringUtil:
    instance: StringUtil = None

    def _init_fields(self) -> None:
        from jsinterop.annotations.JsProperty import JsProperty
        self.INIT_STRING: str = str("")
        self.NULL_STRING: str = "null"
        self.EMPTY_STRING: str = ""
        self.ONE_EMPTY_STRING_ARRAY: list[str] = [self.EMPTY_STRING]
        self.ONE_EMPTY_STRING_ARRAY_OF_ARRAYS: list[list[str]] = [[None] * (0) for _ in range(0)]
        self.stringArray: list[str] = [None] * (0)
    

    @staticmethod
    def getInstance() -> StringUtil:
        from jsinterop.annotations.JsMethod import JsMethod
        return StringUtil.instance
    

    def __init__(self) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        self._init_fields()
    

    def getNonNull(self, string: str) -> str:
        from jsinterop.annotations.JsMethod import JsMethod
        return string
    

    def getArrayInstance(self) -> list[str]:
        from jsinterop.annotations.JsMethod import JsMethod
        return self.stringArray
    

    def count(self, string: str, aChar: str) -> int:
        from jsinterop.annotations.JsMethod import JsMethod
        count: int = 0
        size: int = len(string)
        for index in range(0, size):
            if string[index] == aChar:
                count += 1
        return count
    

    def toString(self, anyType: object) -> str:
        from jsinterop.annotations.JsMethod import JsMethod
        if anyType is not None:
            return str(anyType)
        else:
            return self.NULL_STRING
# from jsinterop.annotations.JsType import JsType
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor
# from jsinterop.annotations.JsProperty import JsProperty


def _StringUtil_instance() -> object:
    return StringUtil()

lazy_static(StringUtil, "instance", _StringUtil_instance)

