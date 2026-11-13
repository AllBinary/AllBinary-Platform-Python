# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


class ABCustomGaugeItem(ABCustomItem):
    NULL_GAUGE_ITEM: ABCustomGaugeItem = None
    

    def __init__(self, label: str, maxValue: int, initialValue: int, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(label, backgroundBasicColor, foregroundBasicColor)
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.logic.string.StringUtil import StringUtil


def _ABCustomGaugeItem_NULL_GAUGE_ITEM() -> object:
    from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
    from org.allbinary.logic.string.StringUtil import StringUtil
    return ABCustomGaugeItem(StringUtil.getInstance().EMPTY_STRING, 1, 0, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)

lazy_static(ABCustomGaugeItem, "NULL_GAUGE_ITEM", _ABCustomGaugeItem_NULL_GAUGE_ITEM)

