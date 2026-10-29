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

# from java.util.Vector import Vector


class ABVector(list):

    def __init__(self) -> None:
        super().__init__()
    

    def ensureCapacity(self, minCapacity: int) -> None:
        super().ensureCapacity(minCapacity)
    

    def capacity(self) -> int:
        return super().capacity()
    

    def size(self) -> int:
        return super().size()
    

    def isEmpty(self) -> bool:
        return super().isEmpty()
    

    def contains(self, obj: object) -> bool:
        return super().contains(obj)
    

    def indexOf(self, obj: object) -> int:
        return super().indexOf(obj)
    

    def lastIndexOf(self, obj: object) -> int:
        return super().lastIndexOf(obj)
    

    def elementAt(self, index: int) -> E:
        return super().elementAt(index)
    

    def firstElement(self) -> E:
        return super().firstElement()
    

    def lastElement(self) -> E:
        return super().lastElement()
    

    def setElementAt(self, obj: E, index: int) -> None:
        super().setElementAt(obj, index)
    

    def removeElementAt(self, index: int) -> None:
        super().removeElementAt(index)
    

    def addElement(self, obj: E) -> None:
        super().addElement(obj)
    

    def insertElementAt(self, obj: E, index: int) -> None:
        super().insertElementAt(obj, index)
    

    def removeElement(self, obj: object) -> bool:
        return super().removeElement(obj)
    

    def removeAllElements(self) -> None:
        super().removeAllElements()
    

    def clone(self) -> object:
        return super().clone()
    

    def toArray(self) -> list[object]:
        return super().toArray()
    

    def set(self, index: int, element: E) -> E:
        return super().set(index, element)
    

    def add(self, element: E) -> bool:
        return super().add(element)
    

    def remove(self, obj: object) -> bool:
        return super().remove(obj)
    

    # Java overloaded method: Python keeps the last definition
    def add(self, index: int, element: E) -> None:
        super().add(index, element)
    

    # Java overloaded method: Python keeps the last definition
    def remove(self, index: int) -> E:
        return super().remove(index)
    

    def clear(self) -> None:
        super().clear()
    

    def equals(self, obj: object) -> bool:
        return super().equals(obj)

    def __eq__(self, other: object) -> bool:
        return self.equals(other)
    

    def hashCode(self) -> int:
        return super().hashCode()

    def __hash__(self) -> int:
        return self.hashCode()
    

    def toString(self) -> str:
        return str(super())

    def __str__(self) -> str:
        return self.toString()
    

    def removeRange(self, fromIndex: int, toIndex: int) -> None:
        super().removeRange(fromIndex, toIndex)
from jsinterop.annotations.JsType import JsType


