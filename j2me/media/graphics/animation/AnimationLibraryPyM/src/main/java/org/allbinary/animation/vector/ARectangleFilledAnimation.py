# Generated Code Do Not Modify
# package org.allbinary.animation.vector

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation


@java_inherited_overloads
class ARectangleFilledAnimation(RectangleFilledAnimation):
    def _java_defaults(self):
        vars(self).setdefault("x", 0)
        vars(self).setdefault("y", 0)

    def _init_fields(self) -> None:
        if "x" not in vars(self): self.x: int = 0
        if "y" not in vars(self): self.y: int = 0
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        super().__init__(0, 0, BasicColorFactory.getInstance().BLACK)
        __class__._init_fields(self)
    

    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, unusedX: int, unusedY: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintXY", graphics, self.x, self.y)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


