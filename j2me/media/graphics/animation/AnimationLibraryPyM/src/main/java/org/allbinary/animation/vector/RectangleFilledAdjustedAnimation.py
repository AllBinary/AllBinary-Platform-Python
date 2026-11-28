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
# package org.allbinary.animation.vector

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface
from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation


@java_inherited_overloads
class RectangleFilledAdjustedAnimation(*java_bases(RectangleFilledAnimation, ColorCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("offsetX", 0)
        vars(self).setdefault("offsetY", 0)

    def _init_fields(self) -> None:
        if "offsetX" not in vars(self): self.offsetX: int = 0
        if "offsetY" not in vars(self): self.offsetY: int = 0
    

    def __init__(self, width: int, height: int, offsetX: int, offsetY: int, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(width, height, basicColor)
        __class__._init_fields(self)
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.setBasicColorP(basicColor)
    

    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
        java_super_call(super(), "paintXY", graphics, x + self.offsetX, y + self.offsetY)
    

    def setOffsetX(self, offsetX: int) -> None:
        self.offsetX = offsetX
    

    def setOffsetY(self, offsetY: int) -> None:
        self.offsetY = offsetY
    

    def getBasicColorP(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return java_super_call(super(), "getBasicColorP")
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        java_super_call(super(), "setBasicColorP", basicColor)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor


