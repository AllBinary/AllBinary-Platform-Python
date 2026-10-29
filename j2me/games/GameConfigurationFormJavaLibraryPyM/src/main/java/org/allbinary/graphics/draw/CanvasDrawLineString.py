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


class CanvasDrawLineString(UpdateMyFontInterface):
    NULL_CANVAS_DRAW_LINE_STRING: CanvasDrawLineString = None

    def _init_fields(self) -> None:
        self.drawStringUtil: DrawStringUtil = DrawStringUtil.getInstance()
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.x: int = None
        self.y: int = None
        self.fontHeight: int = 0
    

    def __init__(self, x: int, y: int) -> None:
        self._init_fields()
        self.x = x
        self.y = y
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics, string: str, line: int) -> None:
        self.myFontProcessor.process(graphics)
        self.drawStringUtil.drawCenterString(graphics, string, 0, len(string), self.x, self.y + (line * self.fontHeight))
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.draw.DrawStringUtil import DrawStringUtil


CanvasDrawLineString.NULL_CANVAS_DRAW_LINE_STRING = CanvasDrawLineString(0, 0)

