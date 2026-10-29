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



class PositionStrings:
    instance: PositionStrings = None

    def _init_fields(self) -> None:
        self.X: str = "x"
        self.Y: str = "y"
        self.X_LABEL: str = "x: "
        self.Y_LABEL: str = "y: "
        self.Z_LABEL: str = "z: "
        self.DX_LABEL: str = "dx: "
        self.DY_LABEL: str = "dy: "
        self.DZ_LABEL: str = "dz: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PositionStrings:
        return PositionStrings.instance
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty


PositionStrings.instance = PositionStrings()

