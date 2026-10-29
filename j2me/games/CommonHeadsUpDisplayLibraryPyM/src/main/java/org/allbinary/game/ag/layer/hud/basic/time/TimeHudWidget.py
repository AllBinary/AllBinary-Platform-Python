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
# package org.allbinary.game.ag.layer.hud.basic.time

from __future__ import annotations

from org.allbinary.game.graphics.hud.BasicHud import BasicHud


class TimeHudWidget(BasicHud):

    def _init_fields(self) -> None:
        self.TIME_STRING: str = "Time "
        self.TIME_CHAR_ARRAY: list[str] = ['T', 'i', 'm', 'e', ' ']
        self.offset: int = 0
        self.string: list[str] = PrimitiveLongSingleton.getInstance().ZERO
        self.totalDigits: int = 1
        self.timer: Timer = None
    

    # throws Exception
    @staticmethod
    def getInstance(location: int, direction: int, basicColor: BasicColor, timer: Timer) -> TimeHudWidget:
        return TimeHudWidget(location, direction, 2, basicColor, timer)
    

    def __init__(self, location: int, direction: int, bufferZone: int, basicColor: BasicColor, timer: Timer) -> None:
        super().__init__(location, direction, bufferZone, basicColor)
        self._init_fields()
        self.timer = timer
        self.set()
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * 5
        self.offset = font.stringWidth(self.TIME_STRING) + MyFontProcessor.defaultStringWidth(font, 3)
        super().updateMeasurement(graphics)
    

    def update(self) -> None:
        self.timer.update()
        self.set()
    

    def set(self) -> None:
        self.string = self.timer.getTimeChars()
        self.totalDigits = self.timer.getCurrentTotalDigits()
    

    def getTimer(self) -> Timer:
        return self.timer
    

    def paint(self, graphics: Graphics) -> None:
        super().paintDX(graphics, self.TIME_CHAR_ARRAY, 0, len(self.TIME_CHAR_ARRAY), self.string, 0, self.totalDigits, self.offset)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton


