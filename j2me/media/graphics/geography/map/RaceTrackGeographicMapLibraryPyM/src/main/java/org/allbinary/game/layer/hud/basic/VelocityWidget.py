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
# package org.allbinary.game.layer.hud.basic

from __future__ import annotations

from org.allbinary.game.graphics.hud.BasicHud import BasicHud


class VelocityWidget(BasicHud):

    def _init_fields(self) -> None:
        self.KILOMETERS_PER_HOUR_STR: list[str] = [' ', 'k', 'm', '/', 'h']
        self.totalChars: int = len(self.KILOMETERS_PER_HOUR_STR)
        self.velocity: int = None
        self.maxVelocity: int = None
        self.string: list[str] = PrimitiveLongSingleton.getInstance().ZERO
        self.totalDigits: int = 1
        self.powerOfTenVelocity: int = None
        self.primitiveLongUtil: PrimitiveLongUtil = None
        self.offset: int = 0
        self.offset2: int = 0
    

    def __init__(self, powerOfTenVelocity: int, location: int, direction: int, basicColor: BasicColor) -> None:
        super().__init__(location, direction, 2, basicColor)
        self._init_fields()
        self.powerOfTenVelocity = powerOfTenVelocity
        self.maxVelocity = powerOfTenVelocity
        self.velocity = 0
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(powerOfTenVelocity)
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * (5 + MathUtil.getInstance().getTotalDigits(self.powerOfTenVelocity) + 1)
        super().updateMeasurement(graphics)
        self.offset = MyFontProcessor.defaultStringWidth(font, self.primitiveLongUtil.getMaxDigits()) + MyFontProcessor.defaultStringWidth(font, 2)
        self.offset2 = self.offset - MyFontProcessor.defaultStringWidth(font, self.totalDigits) - MyFontProcessor.defaultStringWidth(font, 2)
    

    def get(self) -> int:
        return self.velocity
    

    def add(self, value: int) -> None:
        self.set(self.velocity + value)
    

    def set(self, value: int) -> None:
        lastVelocity: int = self.velocity
        self.velocity = value
        if self.velocity > self.maxVelocity:
            self.velocity = 0
        if lastVelocity != self.velocity:
            self.string = self.primitiveLongUtil.getCharArray(self.velocity * 18)
            if OpenGLFeatureUtil.getInstance().isAnyThreed():
                self.totalDigits = self.primitiveLongUtil.getCurrentTotalDigits() + 1
            else:
                self.totalDigits = self.primitiveLongUtil.getCurrentTotalDigits()
            self.myFontProcessor = self.updateMyFontProcessor
    

    def reduce(self, value: int) -> None:
        self.set(self.velocity - value)
    

    def paint(self, graphics: Graphics) -> None:
        super().paintDXY(graphics, self.string, 0, self.totalDigits, self.KILOMETERS_PER_HOUR_STR, 0, self.totalChars, self.offset2, self.offset)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


