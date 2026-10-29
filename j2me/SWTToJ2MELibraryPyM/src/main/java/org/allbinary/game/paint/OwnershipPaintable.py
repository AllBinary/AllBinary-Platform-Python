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
# package org.allbinary.game.paint

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


#SWTToJ2ME
class OwnershipPaintable(Paintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.COPYRIGHT: str = "AllBinary Copyright (c) 2011"
        self.basicColor: BasicColor = BasicColorFactory.getInstance().WHITE
        self.color: int = int(self.basicColor)
        self.anchor: int = Anchor.TOP_LEFT
        self.COPYRIGHT_Y: int = 0
        self.beginWidth: int = 0
    

    @staticmethod
    def getInstance() -> OwnershipPaintable:
        return OwnershipPaintable()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.COPYRIGHT_Y = 2 * font.getHeight()
        self.beginWidth = (font.stringWidth(self.COPYRIGHT) >> 1)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
        self.color = int(basicColor)
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        graphics.setColor(self.color)
        halfWidth: int = self.displayInfo.getLastHalfWidth()
        height: int = self.displayInfo.getLastHeight()
        graphics.drawString(self.COPYRIGHT, halfWidth - self.beginWidth, height - self.COPYRIGHT_Y, self.anchor)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.communication.log.LogUtil import LogUtil


