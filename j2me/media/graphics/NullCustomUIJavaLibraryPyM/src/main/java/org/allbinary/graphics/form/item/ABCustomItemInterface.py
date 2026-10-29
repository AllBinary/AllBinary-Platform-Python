# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations



# Java interface
class ABCustomItemInterface:
    

    def getMinimumWidth(self) -> int:
        raise NotImplementedError()
    

    def getMinimumHeight(self) -> int:
        raise NotImplementedError()
    

    def getLabel(self) -> str:
        raise NotImplementedError()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        raise NotImplementedError()
    

    def paintUnselected(self, graphics: Graphics, x: int, y: int) -> None:
        raise NotImplementedError()
# from javax.microedition.lcdui.Graphics import Graphics


