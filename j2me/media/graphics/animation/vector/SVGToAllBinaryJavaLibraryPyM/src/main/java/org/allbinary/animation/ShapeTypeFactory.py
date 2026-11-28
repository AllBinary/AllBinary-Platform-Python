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
# package org.allbinary.animation

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ShapeTypeFactory:
    instance: ShapeTypeFactory = None

    def _init_fields(self) -> None:
        self.KEY_LINE: str = "line"
        self.KEY_CIRCLE: str = "circle"
        self.KEY_RECTANGLE: str = "rectangle"
        self.KEY_RECT: str = "rect"
        if "LINE" not in vars(self): self.LINE: ShapeType = None
        if "CIRCLE" not in vars(self): self.CIRCLE: ShapeType = None
        if "RECTANGLE" not in vars(self): self.RECTANGLE: ShapeType = None
    

    @staticmethod
    def getInstance() -> ShapeTypeFactory:
        return ShapeTypeFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.animation.ShapeType import ShapeType
        from org.allbinary.animation.ShapeType import ShapeType
        from org.allbinary.animation.ShapeType import ShapeType
        __class__._init_fields(self)
        self.LINE = ShapeType(self.KEY_LINE)
        self.CIRCLE = ShapeType(self.KEY_CIRCLE)
        self.RECTANGLE = ShapeType(self.KEY_RECTANGLE)


def _ShapeTypeFactory_instance() -> object:
    return ShapeTypeFactory()

lazy_static(ShapeTypeFactory, "instance", _ShapeTypeFactory_instance)

