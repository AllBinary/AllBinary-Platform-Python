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

from org.allbinary.game.paint.ColorFillPaintable import ColorFillPaintable


class OverScanColorFillPaintable(ColorFillPaintable):
    

    def __init__(self, basicColor: BasicColor) -> None:
        super().__init__(basicColor)
    

    def paint(self, graphics: Graphics) -> None:
        graphics.setColor(self.colorP)
        graphics.fillRect(-graphics.getClipX(), -graphics.getClipY(), self.displayInfoSingleton.getLastWidth() + (graphics.getClipX() * 2), self.displayInfoSingleton.getLastHeight() + (graphics.getClipY() * 2))
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor


