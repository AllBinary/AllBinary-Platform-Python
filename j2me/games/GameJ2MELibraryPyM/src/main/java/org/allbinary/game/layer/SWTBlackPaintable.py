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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.graphics.paint.Paintable import Paintable


class SWTBlackPaintable(Paintable):

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.BLACK: BasicColor = BasicColorFactory.getInstance().BLACK

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.basicSetColorUtil.setBasicColorP(graphics, self.BLACK)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil


