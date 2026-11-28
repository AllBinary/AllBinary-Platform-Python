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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class ProgressPaintable(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("progressCanvas", None)

    def _init_fields(self) -> None:
        if "progressCanvas" not in vars(self): self.progressCanvas: ProgressCanvas = None
    

    def __init__(self, progressCanvas: ProgressCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.progressCanvas = progressCanvas
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.progressCanvas.paint2(graphics)
# from javax.microedition.lcdui.Graphics import Graphics


