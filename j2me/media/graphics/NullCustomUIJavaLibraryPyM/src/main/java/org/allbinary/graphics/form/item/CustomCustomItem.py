# Generated Code Do Not Modify
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem


class CustomCustomItem(ABCustomItem, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
    

    def __init__(self, label: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(label, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


