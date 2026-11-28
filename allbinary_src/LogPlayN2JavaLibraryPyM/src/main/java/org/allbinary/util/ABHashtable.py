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

from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.util.Hashtable import Hashtable


@java_inherited_overloads
class ABHashtable(Hashtable):
    

    def __init__(self) -> None:
        super().__init__()
    

    def size(self) -> int:
        return java_super_call(super(), "size")
    

    def isEmpty(self) -> bool:
        return java_super_call(super(), "isEmpty")
    

    def elements(self) -> Enumeration[V]:
        from java.util.Enumeration import Enumeration
        return java_super_call(super(), "elements")
    

    def contains(self, value: object) -> bool:
        return java_super_call(super(), "contains", value)
    

    def containsValue(self, value: object) -> bool:
        return java_super_call(super(), "containsValue", value)
    

    def containsKey(self, key: object) -> bool:
        return java_super_call(super(), "containsKey", key)
    

    def get(self, key: object) -> V:
        return java_super_call(super(), "get", key)
    

    def clear(self) -> None:
        java_super_call(super(), "clear")
    

    def clone(self) -> object:
        return java_super_call(super(), "clone")
    

    def toString(self) -> str:
        return java_super_call(super(), "toString")

    def __str__(self) -> str:
        return self.toString()
    

    def equals(self, obj: object) -> bool:
        return java_super_call(super(), "equals", obj)

    def __eq__(self, other: object) -> bool:
        return self.equals(other)
    

    def hashCode(self) -> int:
        return java_super_call(super(), "hashCode")

    def __hash__(self) -> int:
        return self.hashCode()
# from java.util.Enumeration import Enumeration
# from jsinterop.annotations.JsType import JsType


