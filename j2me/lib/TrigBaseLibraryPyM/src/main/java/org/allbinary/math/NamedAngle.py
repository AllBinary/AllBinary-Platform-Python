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

from org.allbinary.math.Angle import Angle


class NamedAngle(Angle):

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, angle: int, name: str) -> None:
        super().__init__(angle)
        self._init_fields()
        self.name = name
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsProperty import JsProperty
from jsinterop.annotations.JsConstructor import JsConstructor


