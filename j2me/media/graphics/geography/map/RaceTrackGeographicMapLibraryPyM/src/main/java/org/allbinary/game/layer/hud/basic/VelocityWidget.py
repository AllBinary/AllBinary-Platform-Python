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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.graphics.hud.BasicHud import BasicHud


@java_inherited_overloads
class VelocityWidget(BasicHud):
    def _java_defaults(self):
        vars(self).setdefault("KILOMETERS_PER_HOUR_STR", None)
        vars(self).setdefault("totalChars", 0)
        vars(self).setdefault("velocity", 0)
        vars(self).setdefault("maxVelocity", 0)
        vars(self).setdefault("string", None)
        vars(self).setdefault("totalDigits", 0)
        vars(self).setdefault("powerOfTenVelocity", 0)
        vars(self).setdefault("primitiveLongUtil", None)
        vars(self).setdefault("offset", 0)
        vars(self).setdefault("offset2", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
        self.KILOMETERS_PER_HOUR_STR: list[str] = [' ', 'k', 'm', '/', 'h']
        self.totalChars: int = len(self.KILOMETERS_PER_HOUR_STR)
        if "velocity" not in vars(self): self.velocity: int = 0
        if "maxVelocity" not in vars(self): self.maxVelocity: int = 0
        self.string: list[str] = PrimitiveLongSingleton.getInstance().ZERO
        self.totalDigits: int = 1
        if "powerOfTenVelocity" not in vars(self): self.powerOfTenVelocity: int = 0
        if "primitiveLongUtil" not in vars(self): self.primitiveLongUtil: PrimitiveLongUtil = None
        self.offset: int = 0
        self.offset2: int = 0
    

    def __init__(self, powerOfTenVelocity: int, location: int, direction: int, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
        super().__init__(location, direction, 2, basicColor)
        __class__._init_fields(self)
        self.powerOfTenVelocity = powerOfTenVelocity
        self.maxVelocity = powerOfTenVelocity
        self.velocity = 0
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(powerOfTenVelocity)
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        from org.allbinary.logic.math.MathUtil import MathUtil
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * (5 + MathUtil.getInstance().getTotalDigits(self.powerOfTenVelocity) + 1)
        java_super_call(super(), "updateMeasurement", graphics)
        self.offset = MyFontProcessor.defaultStringWidth(font, self.primitiveLongUtil.getMaxDigits()) + MyFontProcessor.defaultStringWidth(font, 2)
        self.offset2 = self.offset - MyFontProcessor.defaultStringWidth(font, self.totalDigits) - MyFontProcessor.defaultStringWidth(font, 2)
    

    def get(self) -> int:
        return self.velocity
    

    def add(self, value: int) -> None:
        self.set(self.velocity + value)
    

    def set(self, value: int) -> None:
        from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
        lastVelocity: int = self.velocity
        self.velocity = value
        if self.velocity > self.maxVelocity:
            self.velocity = 0
        if lastVelocity != self.velocity:
            self.string = self.primitiveLongUtil.getCharArray(self.velocity * 18)
            if java_predicate(OpenGLFeatureUtil.getInstance(), "isAnyThreed"):
                self.totalDigits = self.primitiveLongUtil.getCurrentTotalDigits() + 1
            else:
                self.totalDigits = self.primitiveLongUtil.getCurrentTotalDigits()
            self.myFontProcessor = self.updateMyFontProcessor
    

    def reduce(self, value: int) -> None:
        self.set(self.velocity - value)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintDXY", graphics, self.string, 0, self.totalDigits, self.KILOMETERS_PER_HOUR_STR, 0, self.totalChars, self.offset2, self.offset)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.logic.math.MathUtil import MathUtil
# from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
# from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


