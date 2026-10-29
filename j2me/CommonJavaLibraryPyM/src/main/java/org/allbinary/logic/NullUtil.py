# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.logic

from __future__ import annotations



#ActualPlatform
class NullUtil:
    instance: NullUtil = None

    def _init_fields(self) -> None:
        self.NULL_OBJECT: object = object()
        self.NULL_CLASS: type = type(self.NULL_OBJECT)
        self.NULL_OBJECT_ARRAY: list[object] = [None] * (0)
        self.NULL_CHAR_ARRAY: list[str] = ['\0'] * (0)
        self.NULL_BYTE_ARRAY: list[int] = [0] * (0)
        self.NULL_SHORT_ARRAY_ARRAY: list[list[int]] = [[0] * (0) for _ in range(0)]
        self.NULL_INT_ARRAY: list[int] = [0] * (0)
        self.NULL_INT_ARRAY_ARRAY: list[list[int]] = [[0] * (0) for _ in range(0)]
        self.NULL_INT_ARRAY_ARRAY_ARRAY: list[list[list[int]]] = [[[0] * (0) for _ in range(0)] for _ in range(0)]
        self.NULL_FLOAT_ARRAY: list[float] = [0.0] * (0)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> NullUtil:
        return NullUtil.instance
from jsinterop.annotations.JsType import JsType


NullUtil.instance = NullUtil()

