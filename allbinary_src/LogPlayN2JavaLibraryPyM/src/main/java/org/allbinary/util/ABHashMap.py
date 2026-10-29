# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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

# from java.util.HashMap import HashMap


class ABHashMap(dict):

    def __init__(self) -> None:
        super().__init__()
    

    def size(self) -> int:
        return super().size()
    

    def isEmpty(self) -> bool:
        return super().isEmpty()
    

    def get(self, key: object) -> V:
        return super().get(key)
    

    def containsKey(self, key: object) -> bool:
        return super().containsKey(key)
    

    def put(self, key: K, value: V) -> V:
        return super().put(key, value)
    

    def putAll(self, map: Map[object, object]) -> None:
        super().putAll(map)
    

    def remove(self, key: object) -> V:
        return super().remove(key)
    

    def clear(self) -> None:
        super().clear()
    

    def containsValue(self, value: object) -> bool:
        return super().containsValue(value)
    

    def keySet(self) -> Set[K]:
        return super().keySet()
    

    def entrySet(self) -> Set[Entry[K, V]]:
        return super().entrySet()
    

    def getOrDefault(self, key: object, defaultValue: V) -> V:
        return super().getOrDefault(key, defaultValue)
    

    def putIfAbsent(self, key: K, value: V) -> V:
        return super().putIfAbsent(key, value)
    

    def clone(self) -> object:
        return super().clone()
# from java.util.Map import Map
# from java.util.Set import Set
from jsinterop.annotations.JsType import JsType


