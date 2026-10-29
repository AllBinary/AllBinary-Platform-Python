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
# package org.allbinary.math

from __future__ import annotations



class Angle:

    def _init_fields(self) -> None:
        self.value: int = None
    

    def __init__(self, angle: int) -> None:
        self._init_fields()
        self.value = angle
    

    def getValue(self) -> int:
        return self.value
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor


