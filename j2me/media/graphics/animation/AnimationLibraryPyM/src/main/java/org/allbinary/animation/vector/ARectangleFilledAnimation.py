# Generated Code Do Not Modify
# package org.allbinary.animation.vector

from __future__ import annotations

from org.allbinary.animation.vector.RectangleFilledAnimation import RectangleFilledAnimation


class ARectangleFilledAnimation(RectangleFilledAnimation):

    def _init_fields(self) -> None:
        self.x: int = 0
        self.y: int = 0
    

    def __init__(self) -> None:
        super().__init__(0, 0, BasicColorFactory.getInstance().BLACK)
        self._init_fields()
    

    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, unusedX: int, unusedY: int) -> None:
        super().paintXY(graphics, self.x, self.y)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


