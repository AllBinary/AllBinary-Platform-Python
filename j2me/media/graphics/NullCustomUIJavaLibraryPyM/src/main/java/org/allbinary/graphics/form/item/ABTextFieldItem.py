# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.form.item.ABTextItem import ABTextItem


@java_inherited_overloads
class ABTextFieldItem(ABTextItem):
    def _java_defaults(self):
        vars(self).setdefault("font", None)

    def _init_fields(self) -> None:
        if "font" not in vars(self): self.font: Font = None
    

    def __init__(self, canvas: Canvas, visitor: Visitor, label: str, value: str, maxSize: int, layout: int, altText: str, font: Font, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Canvas import Canvas
        from javax.microedition.lcdui.Font import Font
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.logic.util.visitor.Visitor import Visitor
        super().__init__(label, layout, altText, backgroundBasicColor, foregroundBasicColor)
        __class__._init_fields(self)
        self.font = font
    

    def getLabel(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
    

    def setLabel(self, label: str) -> None:
        pass
    

    def getString(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        return StringUtil.getInstance().EMPTY_STRING
    

    def setString(self, string: str) -> None:
        pass
    

    def setFocus(self, state: bool) -> None:
        pass
    

    def getFontHeight(self) -> int:
        return self.font.getHeight()
    

    def setBackgroundBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def setForegroundBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Font import Font
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.util.visitor.Visitor import Visitor


