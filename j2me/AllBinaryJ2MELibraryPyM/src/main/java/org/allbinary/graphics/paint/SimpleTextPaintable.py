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
# package org.allbinary.graphics.paint

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


class SimpleTextPaintable(Paintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.text: str = None
        self.basicColor: BasicColor = None
        self.topScoresWidth: int = 0
        self.fontHeight: int = 0
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, text: str, basicColor: BasicColor) -> None:
        super().__init__()
        self._init_fields()
        self.text = text
        self.basicColor = basicColor
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.topScoresWidth = (font.stringWidth(self.text) >> 1)
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        width: int = self.displayInfoSingleton.getLast()[self.displayInfoSingleton.WIDTH]
        graphics.setColor(int(self.getBasicColorP()))
        graphics.drawString(self.text, (width >> 1) - self.topScoresWidth, self.fontHeight, self.anchor)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def setText(self, text: str) -> None:
        self.text = text
        self.myFontProcessor = self.updateMyFontProcessor
    

    def getText(self) -> str:
        return self.text
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


