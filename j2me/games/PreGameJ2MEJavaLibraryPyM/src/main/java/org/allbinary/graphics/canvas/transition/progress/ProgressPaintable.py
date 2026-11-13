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
# package org.allbinary.graphics.canvas.transition.progress

from __future__ import annotations

from org.allbinary.graphics.paint.Paintable import Paintable


#Was a nested class of ProgressCanvas. It paints the gauge of its ProgressCanvas.
class ProgressPaintable(Paintable):

    def _init_fields(self) -> None:
        self.progressCanvas: ProgressCanvas = None
    

    def __init__(self, progressCanvas: ProgressCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.progressCanvas = progressCanvas
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.progressCanvas.paint2(graphics)
# from javax.microedition.lcdui.Graphics import Graphics


