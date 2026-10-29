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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.graphics.paint.Paintable import Paintable


class GameCanvasNonBotPaintable(Paintable):

    def _init_fields(self) -> None:
        self.gameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.gameCanvas = gameCanvas
    

    def paint(self, graphics: Graphics) -> None:
        self.gameCanvas.nonBotPaint(graphics)
# from javax.microedition.lcdui.Graphics import Graphics


