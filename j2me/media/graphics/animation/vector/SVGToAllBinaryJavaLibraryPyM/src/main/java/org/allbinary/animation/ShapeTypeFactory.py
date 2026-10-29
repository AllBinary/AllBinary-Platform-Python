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



class ShapeTypeFactory:
    instance: ShapeTypeFactory = None

    def _init_fields(self) -> None:
        self.KEY_LINE: str = "line"
        self.KEY_CIRCLE: str = "circle"
        self.KEY_RECTANGLE: str = "rectangle"
        self.KEY_RECT: str = "rect"
        self.LINE: ShapeType = ShapeType(self.KEY_LINE)
        self.CIRCLE: ShapeType = ShapeType(self.KEY_CIRCLE)
        self.RECTANGLE: ShapeType = ShapeType(self.KEY_RECTANGLE)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ShapeTypeFactory:
        return ShapeTypeFactory.instance
from org.allbinary.animation.ShapeType import ShapeType


ShapeTypeFactory.instance = ShapeTypeFactory()

