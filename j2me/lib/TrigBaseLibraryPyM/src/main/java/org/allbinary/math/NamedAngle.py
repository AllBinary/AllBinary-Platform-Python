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
# package org.allbinary.math

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.math.Angle import Angle


@java_inherited_overloads
class NamedAngle(Angle):
    def _java_defaults(self):
        vars(self).setdefault("name", None)

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
    

    def __init__(self, angle: int, name: str) -> None:
        __class__._java_defaults(self)
        from jsinterop.annotations.JsConstructor import JsConstructor
        super().__init__(angle)
        __class__._init_fields(self)
        self.name = name
# from jsinterop.annotations.JsType import JsType
# from jsinterop.annotations.JsProperty import JsProperty
# from jsinterop.annotations.JsConstructor import JsConstructor


