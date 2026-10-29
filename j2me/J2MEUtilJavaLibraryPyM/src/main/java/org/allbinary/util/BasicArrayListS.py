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
# package org.allbinary.util

from __future__ import annotations

from org.allbinary.util.BasicArrayList import BasicArrayList


class BasicArrayListS(BasicArrayList):
    

    def __init__(self, size: int) -> None:
        super().__init__(NullUtil.getInstance().NULL_OBJECT_ARRAY)
        if size < 0:
            raise ValueError(str(StringMaker().append("Init Size Exception: ").appendint(size)))
        self.objectArray = [None] * (size)
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from jsinterop.annotations.JsConstructor import JsConstructor


