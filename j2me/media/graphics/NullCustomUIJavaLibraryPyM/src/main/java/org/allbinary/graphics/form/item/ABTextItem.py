# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.form.item.CustomCustomItem import CustomCustomItem
from org.allbinary.graphics.form.item.ABCustomItemInterface import ABCustomItemInterface


@java_inherited_overloads
class ABTextItem(*java_bases(CustomCustomItem, ABCustomItemInterface)):
    

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
        return java_super_call(super(), "getMinimumWidth")
    

    def getMinimumHeight(self) -> int:
        return java_super_call(super(), "getMinimumHeight")
    

    def getLabel(self) -> str:
        return java_super_call(super(), "getLabel")
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintXY", graphics, x, y)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor


