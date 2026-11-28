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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class PaintableLayerComposite(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("paintableArray", None)

    def _init_fields(self) -> None:
        if "paintableArray" not in vars(self): self.paintableArray: list[Layer] = None
    

    def __init__(self, paintableArray: list[Layer]) -> None:
        __class__._java_defaults(self)
        from org.allbinary.layer.Layer import Layer
        super().__init__()
        __class__._init_fields(self)
        self.paintableArray = paintableArray
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        index = len(self.paintableArray)
        while (index := index - 1) >= 0:
            self.paintableArray[index].paint(graphics)
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
        paintableInterface: PaintableInterface = None
        index = len(self.paintableArray)
        while (index := index - 1) >= 0:
            paintableInterface = self.paintableArray[index]
            paintableInterface.paintThreed(graphics)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
# from org.allbinary.layer.Layer import Layer


