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


class GamePerformanceInitUpdatePaintable(InitUpdatePaintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.halfHeight: int = DisplayInfoSingleton.getInstance().getLastHalfHeight()
        self.yArray: list[int] = [self.halfHeight + 30, self.halfHeight + 30, self.halfHeight + 30 + 15, self.halfHeight + 30 + 15, self.halfHeight + 30 + 30, self.halfHeight + 30 + 30, self.halfHeight + 30 + 45, self.halfHeight + 30 + 45]
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.baseRefreshHelperCharArray: list[list[str]] = [['\0'] * (0) for _ in range(0)]
        self.defaultStringWidth: int = 0
        self.RED: int = int(BasicColorFactory.getInstance().RED)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.defaultStringWidth = MyFontProcessor.defaultStringWidth(font, 2)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def init(self) -> None:
        pass
    

    def update(self) -> None:
        self.baseRefreshHelperCharArray = GameStatisticsFactory.getInstance().to2DCharArray()
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
        graphics.setColor(self.RED)
        charArray: list[str] = None
        charArray2: list[str] = None
        size2: int = 0
        size3: int = 0
        size: int = len(self.baseRefreshHelperCharArray) - 2
        for index in range(size, 0 - 1, -2):
            charArray = self.baseRefreshHelperCharArray[index]
            charArray2 = self.baseRefreshHelperCharArray[index + 1]
            size2 = len(charArray)
            size3 = len(charArray2)
            graphics.drawChars(charArray, 0, size2, 0, self.yArray[index], 0)
            graphics.drawChars(charArray2, 0, size3, size2 * self.defaultStringWidth, self.yArray[index + 1], 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.canvas.GameStatisticsFactory import GameStatisticsFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


