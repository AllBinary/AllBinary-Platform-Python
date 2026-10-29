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
# package org.allbinary.game.ag.layer.hud.basic

from __future__ import annotations

from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


class NumberStringHud(BasicHud, PaintableInterface):

    def _init_fields(self) -> None:
        self.primitiveLongUtil: PrimitiveLongUtil = None
        self.prependString: str = None
        self.PREPEND_STRING: list[str] = None
        self.value: int = None
        self.max: int = None
        self.offset: int = 0
        self.valueString: list[str] = None
        self.valueTotalDigits: int = 0
    

    def __init__(self, prependString: str, max: int, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        super().__init__(location, direction, bufferZone, basicColor)
        self._init_fields()
        self.prependString = prependString
        self.PREPEND_STRING = list(prependString)
        self.valueString = PrimitiveLongSingleton.getInstance().NUMBER_CHAR_ARRAYS[0]
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(max + 1)
        self.max = max
        self.value = 0
        if direction == 0:
            raise RuntimeError(BasicHudFactory.getInstance().DIRECTION_EXCEPTION)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.offset = font.stringWidth(self.prependString) + MyFontProcessor.defaultCharWidth(font)
        super().updateMeasurement(graphics)
    

    def get(self) -> int:
        return self.value
    

    def add(self, value: int) -> None:
        self.set(self.value + value)
    

    def set(self, value: int) -> None:
        self.value = value
        if self.value > self.max:
            self.value = 0
        self.valueString = self.primitiveLongUtil.getCharArray(self.value)
        self.valueTotalDigits = self.primitiveLongUtil.getCurrentTotalDigits()
    

    def reduce(self, value: int) -> None:
        self.set(self.value - value)
    

    def paint(self, graphics: Graphics) -> None:
        super().paintDX(graphics, self.PREPEND_STRING, 0, len(self.PREPEND_STRING), self.valueString, 0, self.valueTotalDigits, self.offset)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        charArray: list[str] = self.PREPEND_STRING
        len_: int = len(self.PREPEND_STRING)
        charArray2: list[str] = self.valueString
        len2: int = self.valueTotalDigits
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        graphics.drawChars(charArray, 0, len_, x, y, 0)
        graphics.drawChars(charArray2, 0, len2, x - self.offset, y, 0)
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


