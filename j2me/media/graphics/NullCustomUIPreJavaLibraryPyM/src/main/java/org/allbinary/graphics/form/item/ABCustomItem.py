# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ABCustomItem:
    NULL_CUSTOM_ITEM: object = None
    

    @staticmethod
    def getNullInstance() -> ABCustomItem:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        if ABCustomItem.NULL_CUSTOM_ITEM == NullUtil.getInstance().NULL_OBJECT:
            ABCustomItem.NULL_CUSTOM_ITEM = ABCustomItem(StringUtil.getInstance().EMPTY_STRING, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return ABCustomItem.NULL_CUSTOM_ITEM
    

    def __init__(self, label: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        pass
    

    def setOwner(self, owner: Screen) -> None:
        from javax.microedition.lcdui.Screen import Screen
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def paintUnselected(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def isFocusable(self) -> bool:
        return False
    

    def getLabel(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
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
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Screen import Screen
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringUtil import StringUtil


def _ABCustomItem_NULL_CUSTOM_ITEM() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(ABCustomItem, "NULL_CUSTOM_ITEM", _ABCustomItem_NULL_CUSTOM_ITEM)

