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

from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface
from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation


class RectangleFilledAdjustedAnimation(RectangleFilledAnimation, ColorCompositeInterface):

    def _init_fields(self) -> None:
        self.offsetX: int = None
        self.offsetY: int = None
    

    def __init__(self, width: int, height: int, offsetX: int, offsetY: int, basicColor: BasicColor) -> None:
        super().__init__(width, height, basicColor)
        self._init_fields()
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.setBasicColorP(basicColor)
    

    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
        super().paintXY(graphics, x + self.offsetX, y + self.offsetY)
    

    def setOffsetX(self, offsetX: int) -> None:
        self.offsetX = offsetX
    

    def setOffsetY(self, offsetY: int) -> None:
        self.offsetY = offsetY
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


