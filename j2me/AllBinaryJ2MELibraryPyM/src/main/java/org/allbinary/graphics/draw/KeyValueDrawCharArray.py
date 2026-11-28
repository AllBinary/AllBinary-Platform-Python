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


class KeyValueDrawCharArray(UpdateMyFontInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.java.character.CharArrayFactory import CharArrayFactory
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        if "LABEL" not in vars(self): self.LABEL: str = None
        if "labelX" not in vars(self): self.labelX: int = 0
        if "valueX" not in vars(self): self.valueX: int = 0
        self.value: list[str] = CharArrayFactory.getInstance().getZeroCharArray()
        if "len_" not in vars(self): self.len_: int = 0
    

    def __init__(self, label: str, x: int) -> None:
        __class__._init_fields(self)
        self.LABEL = label
        self.labelX = x
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        labelWidth: int = graphics.getFont().stringWidth(self.LABEL) - len(self.LABEL)
        self.valueX = labelWidth + self.labelX
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        graphics.drawString(self.LABEL, self.labelX, y, 0)
        graphics.drawChars(self.value, 0, self.len_, self.valueX, y, 0)
    

    def update(self, value: list[str], len_: int) -> None:
        self.value = value
        self.len_ = len_
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.logic.java.character.CharArrayFactory import CharArrayFactory
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


