# Generated Code Do Not Modify
# package org.allbinary.graphics.form

from __future__ import annotations

from org.allbinary.graphics.form.CustomScreen import CustomScreen


class ABCustomForm(CustomScreen):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self, title: str, items: list[ABCustomItem], backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
    

    def getAllitems(self) -> list[ABCustomItem]:
        return [None] * (0)
    

    def size(self) -> int:
        return 0
    

    def setSelectedIndex(self, index: int) -> None:
        pass
    

    def getSelectedIndex(self) -> int:
        return 0
    

    def deleteAll(self) -> None:
        pass
    

    def delete(self, itemNum: int) -> None:
        pass
    

    def append(self, item: ABCustomItem) -> int:
        return -1
    

    def insert(self, itemNum: int, item: ABCustomItem) -> None:
        pass
    

    def set(self, itemNum: int, item: ABCustomItem) -> None:
        pass
    

    def get(self, itemNum: int) -> ABCustomItem:
        return ABCustomItem.getNullInstance()
    

    def getWidth(self) -> int:
        raise RuntimeError()
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def getTitle(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


