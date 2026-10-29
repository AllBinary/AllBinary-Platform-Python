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

from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface


class RectangleAdjustedAnimation(Animation, ColorCompositeInterface):

    def _init_fields(self) -> None:
        self.width: int = None
        self.height: int = None
        self.offsetX: int = None
        self.offsetY: int = None
    

    def __init__(self, width: int, height: int, offsetX: int, offsetY: int, basicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.width = width
        self.height = height
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.setBasicColorP(basicColor)
    

    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
        graphics.drawRect(x + self.offsetX, y + self.offsetY, self.width, self.height)
    

    def setWidth(self, width: int) -> None:
        self.width = width
    

    def setHeight(self, height: int) -> None:
        self.height = height
    

    def setOffsetX(self, offsetX: int) -> None:
        self.offsetX = offsetX
    

    def setOffsetY(self, offsetY: int) -> None:
        self.offsetY = offsetY
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


