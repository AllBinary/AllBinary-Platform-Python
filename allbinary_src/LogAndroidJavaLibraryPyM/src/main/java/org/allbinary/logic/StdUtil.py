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

from java.lang.JavaRuntimeStatic import lazy_static


#ActualPlatform
class StdUtil:
    instance: StdUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.util.ABHashMap import ABHashMap
        from org.allbinary.util.ABHashtable import ABHashtable
        from org.allbinary.util.ABVector import ABVector
        self.EMPTY_VECTOR: ABVector[object] = self.createVector()
        self.NULL_TABLE: ABHashtable[object, object] = self.createHashtable()
        self.NULL_MAP: ABHashMap[object, object] = self.createHashMap()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> StdUtil:
        return StdUtil.instance
    

    def createStack(self) -> ABStack[object]:
        from org.allbinary.util.ABStack import ABStack
        return ABStack()
    

    def createVector(self) -> ABVector[object]:
        from org.allbinary.util.ABVector import ABVector
        return ABVector()
    

    def createHashtable(self) -> ABHashtable[object, object]:
        from org.allbinary.util.ABHashtable import ABHashtable
        return ABHashtable()
    

    def createHashMap(self) -> ABHashMap[object, object]:
        from org.allbinary.util.ABHashMap import ABHashMap
        return ABHashMap()
# from org.allbinary.util.ABHashMap import ABHashMap
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.ABStack import ABStack
# from org.allbinary.util.ABVector import ABVector


def _StdUtil_instance() -> object:
    return StdUtil()

lazy_static(StdUtil, "instance", _StdUtil_instance)

