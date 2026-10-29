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
# package org.allbinary.game.paint.help

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


class HelpPaintable(Paintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.anchor: int = Anchor.TOP_LEFT
        self.title: str = None
        self.inputInfo: list[str] = StringUtil.getInstance().getArrayInstance()
        self.basicColor: BasicColor = None
        self.titleBeginWidth: int = 0
        self.beginWidthArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
        self.charHeight: int = 0
    

    def __init__(self, title: str, backgroundBasicColor: BasicColor, basicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.title = title
        self.basicColor = basicColor
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.titleBeginWidth = (font.stringWidth(self.title) >> 1)
        self.charHeight = font.getHeight()
        size: int = len(self.inputInfo)
        for index in range(0, size):
            self.beginWidthArray[index] = (font.stringWidth(self.inputInfo[index]) >> 1)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def setInputInfoP(self, inputInfo: list[str]) -> None:
        self.inputInfo = inputInfo
        self.beginWidthArray = [0] * (len(self.inputInfo))
        self.myFontProcessor = self.updateMyFontProcessor
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        halfWidth: int = self.displayInfo.getLastHalfWidth()
        graphics.setColor(int(self.basicColor))
        graphics.drawString(self.title, halfWidth - self.titleBeginWidth, self.charHeight, self.anchor)
        size: int = len(self.inputInfo)
        for index in range(0, size):
            graphics.drawString(self.inputInfo[index], halfWidth - self.beginWidthArray[index], (index + 3) * self.charHeight, self.anchor)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringUtil import StringUtil


