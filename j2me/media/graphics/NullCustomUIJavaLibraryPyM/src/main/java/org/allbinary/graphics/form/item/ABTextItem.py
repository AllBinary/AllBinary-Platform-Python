# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.form.item.CustomCustomItem import CustomCustomItem
from org.allbinary.graphics.form.item.ABCustomItemInterface import ABCustomItemInterface


class ABTextItem(CustomCustomItem, ABCustomItemInterface):
    

    def __init__(self, label: str, layout: int, altText: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(label, backgroundBasicColor, foregroundBasicColor)
    

    def keyPressed(self, keyCode: int) -> None:
        pass
    

    def paintUnselected(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def getLabelStringComponent(self) -> ABStringComponent:
        from org.allbinary.graphics.form.item.ABStringComponent import ABStringComponent
        return ABStringComponent.NULL_STRING_COMPONENT
    

    def getMinimumWidth(self) -> int:
        return super().getMinimumWidth()
    

    def getMinimumHeight(self) -> int:
        return super().getMinimumHeight()
    

    def getLabel(self) -> str:
        return super().getLabel()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        super().paintXY(graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor


