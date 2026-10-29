# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class ABCustomItem:
    NULL_CUSTOM_ITEM: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getNullInstance() -> ABCustomItem:
        if ABCustomItem.NULL_CUSTOM_ITEM == NullUtil.getInstance().NULL_OBJECT:
            ABCustomItem.NULL_CUSTOM_ITEM = ABCustomItem(StringUtil.getInstance().EMPTY_STRING, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return ABCustomItem.NULL_CUSTOM_ITEM
    

    def __init__(self, label: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        pass
    

    def setOwner(self, owner: Screen) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        pass
    

    def paintUnselected(self, graphics: Graphics, x: int, y: int) -> None:
        pass
    

    def isFocusable(self) -> bool:
        return False
    

    def getLabel(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def setLabel(self, label: str) -> None:
        pass
    

    def getHeight(self) -> int:
        return 0
    

    def setHeight(self, height: int) -> None:
        pass
    

    def getValue(self) -> float:
        return 0.0
    

    def setValue(self, value: float) -> None:
        pass
    

    def getMinimumWidth(self) -> int:
        return 0
    

    def getMinimumHeight(self) -> int:
        return 0
    

    def preMeasurement(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Screen import Screen
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.string.StringUtil import StringUtil


