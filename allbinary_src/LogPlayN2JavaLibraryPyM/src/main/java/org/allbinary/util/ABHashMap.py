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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.util.HashMap import HashMap


@java_inherited_overloads
class ABHashMap(HashMap):

    def __init__(self) -> None:
        super().__init__()
    

    def size(self) -> int:
        return java_super_call(super(), "size")
    

    def isEmpty(self) -> bool:
        return java_super_call(super(), "isEmpty")
    

    def get(self, key: object) -> V:
        return java_super_call(super(), "get", key)
    

    def containsKey(self, key: object) -> bool:
        return java_super_call(super(), "containsKey", key)
    

    def put(self, key: K, value: V) -> V:
        return java_super_call(super(), "put", key, value)
    

    def putAll(self, map: Map[object, object]) -> None:
        from java.util.Map import Map
        java_super_call(super(), "putAll", map)
    

    def remove(self, key: object) -> V:
        return java_super_call(super(), "remove", key)
    

    def clear(self) -> None:
        java_super_call(super(), "clear")
    

    def containsValue(self, value: object) -> bool:
        return java_super_call(super(), "containsValue", value)
    

    def keySet(self) -> Set[K]:
        from java.util.Set import Set
        return java_super_call(super(), "keySet")
    

    def entrySet(self) -> Set[Entry[K, V]]:
        from java.util.Map import Map
        from java.util.Set import Set
        return java_super_call(super(), "entrySet")
    

    def getOrDefault(self, key: object, defaultValue: V) -> V:
        return java_super_call(super(), "getOrDefault", key, defaultValue)
    

    def putIfAbsent(self, key: K, value: V) -> V:
        return java_super_call(super(), "putIfAbsent", key, value)
    

    def clone(self) -> object:
        return java_super_call(super(), "clone")
# from java.util.Map import Map
# from java.util.Set import Set
# from jsinterop.annotations.JsType import JsType


