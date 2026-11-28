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
from java.util.Stack import Stack


@java_inherited_overloads
class ABStack(Stack):

    def __init__(self) -> None:
        super().__init__()
    

    def push(self, item: E) -> E:
        return java_super_call(super(), "push", item)
    

    def pop(self) -> E:
        return java_super_call(super(), "pop")
    

    def peek(self) -> E:
        return java_super_call(super(), "peek")
    

    def empty(self) -> bool:
        return java_super_call(super(), "empty")
    

    def search(self, obj: object) -> int:
        return java_super_call(super(), "search", obj)
    

    def removeElement(self, obj: object) -> bool:
        return java_super_call(super(), "removeElement", obj)
# from jsinterop.annotations.JsType import JsType


