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

from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable


class ColorFillPaintable(ColorFillBasePaintable):

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
    

    def __init__(self, basicColor: BasicColor) -> None:
        super().__init__(basicColor)
        self._init_fields()
    

    def paint(self, graphics: Graphics) -> None:
        graphics.setColor(self.colorP)
        graphics.fillRect(0, 0, self.displayInfoSingleton.getLastWidth(), self.displayInfoSingleton.getLastHeight())
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


