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
# package org.allbinary.graphics

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class PointFactory:
    instance: PointFactory = None

    def _init_fields(self) -> None:
        from jsinterop.annotations.JsProperty import JsProperty
        self.ZERO_ZERO: GPoint = self.createXYZ(0, 0, 0)
    

    @staticmethod
    def getInstance() -> PointFactory:
        from jsinterop.annotations.JsMethod import JsMethod
        return PointFactory.instance
    

    def init(self) -> None:
        from jsinterop.annotations.JsMethod import JsMethod
        pass
    

    def __init__(self) -> None:
        from jsinterop.annotations.JsConstructor import JsConstructor
        self._init_fields()
    

    def createXY(self, x: int, y: int) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        from jsinterop.annotations.JsMethod import JsMethod
        return GPoint(x, y, 0)
    

    def createXYZ(self, x: int, y: int, z: int) -> GPoint:
        from org.allbinary.graphics.GPoint import GPoint
        from jsinterop.annotations.JsMethod import JsMethod
        return GPoint(x, y, z)
# from jsinterop.annotations.JsType import JsType
# from jsinterop.annotations.JsMethod import JsMethod
# from jsinterop.annotations.JsConstructor import JsConstructor
# from jsinterop.annotations.JsProperty import JsProperty


def _PointFactory_instance() -> object:
    return PointFactory()

lazy_static(PointFactory, "instance", _PointFactory_instance)

