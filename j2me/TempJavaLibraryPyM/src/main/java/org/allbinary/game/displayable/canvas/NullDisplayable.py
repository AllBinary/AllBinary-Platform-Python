# Generated Code Do Not Modify
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

# from javax.microedition.lcdui.Canvas import Canvas


#Temp should not be in any build
class NullDisplayable(Canvas):
    SINGLETON: NullDisplayable = None
    

    @staticmethod
    def getInstance() -> NullDisplayable:
        return NullDisplayable.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
    

    def paint(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics


NullDisplayable.SINGLETON = NullDisplayable()

