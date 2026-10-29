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

import threading


class BaseCircularPool:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.NULL_CIRCULAR_INDEX_UTIL
        self.OBJECT_ARRAY: list[object] = NullUtil.getInstance().NULL_OBJECT_ARRAY

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getNextInstance(self) -> object:
        with self._lock:
            return self._getNextInstance_unlocked()

    def _getNextInstance_unlocked(self) -> object:
        anyType: object = self.OBJECT_ARRAY[self.circularIndexUtil.getIndex()]
        self.circularIndexUtil.next()
        return anyType
    

    def init(self, allBinaryObjectFactoryInterface: AllBinaryObjectFactoryInterface) -> None:
        self.circularIndexUtil.setIndex(0)
        size: int = self.circularIndexUtil.getSize()
        for index in range(0, size):
            self.OBJECT_ARRAY[index] = allBinaryObjectFactoryInterface.getInstance()
    

    # throws Exception
    def getInstance(self, index: int) -> object:
        return self.OBJECT_ARRAY[index]
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty


