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



class BasicColorArrayIndexer:

    def _init_fields(self) -> None:
        self.basicColorArray: list[BasicColor] = None
        self.circularIndexUtil: CircularIndexUtil = None
    

    def __init__(self, basicColorArray: list[BasicColor]) -> None:
        self._init_fields()
        self.basicColorArray = basicColorArray
        self.circularIndexUtil = CircularIndexUtil.createInstance(len(self.basicColorArray))
    

    def next(self) -> None:
        self.circularIndexUtil.next()
    

    def get(self) -> BasicColor:
        return self.basicColorArray[self.circularIndexUtil.getIndex()]
    

    def getBasicColorArray(self) -> list[BasicColor]:
        return self.basicColorArray
from jsinterop.annotations.JsType import JsType
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor


