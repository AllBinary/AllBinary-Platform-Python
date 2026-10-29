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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


class StartIntermissionPaintable(InitUpdatePaintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.fontDebugFactory: FontDebugFactory = FontDebugFactory.getInstance()
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.gameCanvas: AllBinaryGameCanvas = None
        self.stringArray: list[str] = None
        self.fontSize: int = None
        self.font: Font = None
        self.lastWidth: list[int] = None
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.basicColor: BasicColor = BasicColorFactory.getInstance().BLACK
        self.color: int = None
        self.lineYOffsetArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
        self.hasChanged: bool = True
        self.anchor: int = Anchor.TOP_LEFT
        self.fontHeightP: int = 0
        self.BEGIN_LEVEL: str = "Begin Level "
        self.EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas, stringArray: list[str], basicColor: BasicColor, font: Font) -> None:
        super().__init__()
        self._init_fields()
        self.gameCanvas = gameCanvas
        self.stringArray = stringArray
        self.lastWidth = [0] * (len(self.stringArray))
        self.setBasicColorP(basicColor)
        self.color = int(basicColor)
        self.fontSize = font.getSize()
        self.font = font
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.fontHeightP = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        existingFont: Font = graphics.getFont()
        self.fontDebugFactory.setFont(self.font, graphics)
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.basicSetColorUtil.setBasicColorP3(graphics, self.basicColor, self.color)
        beginWidth: int = 0
        for index in range(len(self.lineYOffsetArray) - 1, 0 - 1, -1):
            if self.hasChanged:
                self.lastWidth[index] = (graphics.getFont().stringWidth(self.stringArray[index]) >> 1)
            beginWidth = self.lastWidth[index]
            graphics.drawString(self.stringArray[index], displayInfo.getLastHalfWidth() - beginWidth, displayInfo.getLastHalfHeight() - self.lineYOffsetArray[index], self.anchor)
        self.hasChanged = False
        self.fontDebugFactory.setFont(existingFont, graphics)
    

    def update(self) -> None:
        level: int = self.gameCanvas.getLayerManager().getGameInfo().getCurrentLevel()
        self.stringArray[0] = str(StringMaker().append(self.BEGIN_LEVEL).appendint(level))
        for index in range(len(self.stringArray) - 1, 1 - 1, -1):
            self.stringArray[index] = self.EMPTY_STRING
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.FontDebugFactory import FontDebugFactory
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


