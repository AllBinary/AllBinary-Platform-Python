# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.form.item.ABTextItem import ABTextItem


class ABTextFieldItem(ABTextItem):

    def _init_fields(self) -> None:
        self.font: Font = None
    

    def __init__(self, canvas: Canvas, visitor: Visitor, label: str, value: str, maxSize: int, layout: int, altText: str, font: Font, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(label, layout, altText, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.font = font
    

    def getLabel(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def setLabel(self, label: str) -> None:
        pass
    

    def getString(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def setString(self, string: str) -> None:
        pass
    

    def setFocus(self, state: bool) -> None:
        pass
    

    def getFontHeight(self) -> int:
        return self.font.getHeight()
    

    def setBackgroundBasicColorP(self, basicColor: BasicColor) -> None:
        pass
    

    def setForegroundBasicColorP(self, basicColor: BasicColor) -> None:
        pass
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Font import Font
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.visitor.Visitor import Visitor


