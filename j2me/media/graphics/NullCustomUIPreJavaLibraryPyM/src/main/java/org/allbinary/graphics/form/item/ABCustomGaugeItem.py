# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


class ABCustomGaugeItem(ABCustomItem):
    NULL_GAUGE_ITEM: ABCustomGaugeItem = None
    

    def __init__(self, label: str, maxValue: int, initialValue: int, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(label, backgroundBasicColor, foregroundBasicColor)
from org.allbinary.graphics.color.BasicColor import BasicColor


ABCustomGaugeItem.NULL_GAUGE_ITEM = ABCustomGaugeItem(StringUtil.getInstance().EMPTY_STRING, 1, 0, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)

