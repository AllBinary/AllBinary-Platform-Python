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
from java.util.Vector import Vector


@java_inherited_overloads
class ABVector(Vector):

    def __init__(self) -> None:
        super().__init__()
    

    def ensureCapacity(self, minCapacity: int) -> None:
        java_super_call(super(), "ensureCapacity", minCapacity)
    

    def capacity(self) -> int:
        return java_super_call(super(), "capacity")
    

    def size(self) -> int:
        return java_super_call(super(), "size")
    

    def isEmpty(self) -> bool:
        return java_super_call(super(), "isEmpty")
    

    def contains(self, obj: object) -> bool:
        return java_super_call(super(), "contains", obj)
    

    def indexOf(self, obj: object) -> int:
        return java_super_call(super(), "indexOf", obj)
    

    def lastIndexOf(self, obj: object) -> int:
        return java_super_call(super(), "lastIndexOf", obj)
    

    def elementAt(self, index: int) -> E:
        return java_super_call(super(), "elementAt", index)
    

    def firstElement(self) -> E:
        return java_super_call(super(), "firstElement")
    

    def lastElement(self) -> E:
        return java_super_call(super(), "lastElement")
    

    def setElementAt(self, obj: E, index: int) -> None:
        java_super_call(super(), "setElementAt", obj, index)
    

    def removeElementAt(self, index: int) -> None:
        java_super_call(super(), "removeElementAt", index)
    

    def addElement(self, obj: E) -> None:
        java_super_call(super(), "addElement", obj)
    

    def insertElementAt(self, obj: E, index: int) -> None:
        java_super_call(super(), "insertElementAt", obj, index)
    

    def removeElement(self, obj: object) -> bool:
        return java_super_call(super(), "removeElement", obj)
    

    def removeAllElements(self) -> None:
        java_super_call(super(), "removeAllElements")
    

    def clone(self) -> object:
        return java_super_call(super(), "clone")
    

    def toArray(self) -> list[object]:
        return java_super_call(super(), "toArray")
    

    def set(self, index: int, element: E) -> E:
        return java_super_call(super(), "set", index, element)
    

    def add_j1(self, element: E) -> bool:
        return java_super_call(super(), "add", element)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def remove_j1_1(self, obj: object) -> bool:
        return java_super_call(super(), "remove", obj)
    

    def add_j2(self, index: int, element: E) -> None:
        java_super_call(super(), "add", index, element)

    def add(self, *args):
        implementation = __class__.__dict__.get("add_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().add(*args)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def remove_j1_2(self, index: int) -> E:
        return java_super_call(super(), "remove", index)

    def remove(self, *args):
        if len(args) == 1 and True:
            return __class__.__dict__["remove_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["remove_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("remove_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().remove(*args)
    

    def clear(self) -> None:
        java_super_call(super(), "clear")
    

    def equals(self, obj: object) -> bool:
        return java_super_call(super(), "equals", obj)

    def __eq__(self, other: object) -> bool:
        return self.equals(other)
    

    def hashCode(self) -> int:
        return java_super_call(super(), "hashCode")

    def __hash__(self) -> int:
        return self.hashCode()
    

    def toString(self) -> str:
        return java_super_call(super(), "toString")

    def __str__(self) -> str:
        return self.toString()
    

    def removeRange(self, fromIndex: int, toIndex: int) -> None:
        java_super_call(super(), "removeRange", fromIndex, toIndex)
# from jsinterop.annotations.JsType import JsType


