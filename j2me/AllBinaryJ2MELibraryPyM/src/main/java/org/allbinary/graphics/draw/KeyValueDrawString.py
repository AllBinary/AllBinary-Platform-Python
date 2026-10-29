#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.graphics.draw

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class KeyValueDrawString(UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.LABEL: str = None
        self.labelX: int = None
        self.valueX: int = 0
        self.value: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, label: str, x: int) -> None:
        self._init_fields()
        self.LABEL = label
        self.labelX = x
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        labelWidth: int = graphics.getFont().stringWidth(self.LABEL) - len(self.LABEL)
        self.valueX = labelWidth + self.labelX
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics, y: int) -> None:
        self.myFontProcessor.process(graphics)
        graphics.drawString(self.LABEL, self.labelX, y, 0)
        graphics.drawString(self.value, self.valueX, y, 0)
    

    def update(self, value: str) -> None:
        if value is not None:
            self.value = value
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.string.StringUtil import StringUtil


