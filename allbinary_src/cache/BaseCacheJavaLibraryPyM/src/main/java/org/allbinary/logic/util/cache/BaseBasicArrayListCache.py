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
# package org.allbinary.logic.util.cache

from __future__ import annotations



class BaseBasicArrayListCache:

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    def log(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("S: ")
        stringBuffer.appendint(self.list_.size())
        return str(stringBuffer)
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty


