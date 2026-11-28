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
# package org.allbinary.game.paint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class ColorFillBasePaintable(*java_bases(Paintable, ColorCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("basicColor", None)
        vars(self).setdefault("colorP", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        if "colorP" not in vars(self): self.colorP: int = 0
    

    def __init__(self, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__()
        __class__._init_fields(self)
        self.setBasicColorP(basicColor)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.basicColor = basicColor
        self.setColor(int(self.getBasicColorP()))
    

    def getBasicColorP(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return self.basicColor
    

    def getColor(self) -> int:
        return self.colorP
    

    def setColor(self, color: int) -> None:
        self.colorP = color
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


