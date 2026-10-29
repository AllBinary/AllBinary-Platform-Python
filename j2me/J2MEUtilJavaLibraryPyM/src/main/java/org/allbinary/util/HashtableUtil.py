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



class HashtableUtil:
    instance: HashtableUtil = None

    def _init_fields(self) -> None:
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> HashtableUtil:
        return HashtableUtil.instance
    

    def putAll(self, fromHashtable: ABHashtable[object, object], hashtable: ABHashtable[object, object]) -> None:
        enumeration: Enumeration = fromHashtable.keys()
        keyCanBeNull: object = None
        valueCanBeNull: object = None
        while self.enumerationUtil.hasMoreElements(enumeration):
            keyCanBeNull = self.enumerationUtil.nextElement(enumeration)
            valueCanBeNull = hashtable.get(keyCanBeNull)
            if valueCanBeNull is None:
                pass
            else:
                hashtable.put(keyCanBeNull, valueCanBeNull)
    

    def getKeysAsArray(self, hashtable: ABHashtable[object, object]) -> list[object]:
        objectArray: list[object] = [None] * (hashtable.size())
        index: int = 0
        enumeration: Enumeration = hashtable.keys()
        while self.enumerationUtil.hasMoreElements(enumeration):
            objectArray[((index := index + 1) - 1)] = self.enumerationUtil.nextElement(enumeration)
        return objectArray
    

    def getKeysAsList(self, hashtable: ABHashtable[object, object]) -> BasicArrayList:
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
        list_: BasicArrayList = BasicArrayListS(hashtable.size())
        enumeration: Enumeration = hashtable.keys()
        while self.enumerationUtil.hasMoreElements(enumeration):
            list_.add(self.enumerationUtil.nextElement(enumeration))
        return list_
# from java.util.Enumeration import Enumeration
from jsinterop.annotations.JsType import JsType
from org.allbinary.util.EnumerationUtil import EnumerationUtil


HashtableUtil.instance = HashtableUtil()

