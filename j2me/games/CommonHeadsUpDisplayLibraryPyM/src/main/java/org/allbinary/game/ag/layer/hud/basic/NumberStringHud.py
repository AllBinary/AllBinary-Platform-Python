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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.graphics.hud.BasicHud import BasicHud
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface


@java_inherited_overloads
class NumberStringHud(*java_bases(BasicHud, PaintableInterface)):
    def _java_defaults(self):
        vars(self).setdefault("primitiveLongUtil", None)
        vars(self).setdefault("prependString", None)
        vars(self).setdefault("PREPEND_STRING", None)
        vars(self).setdefault("value", 0)
        vars(self).setdefault("max", 0)
        vars(self).setdefault("offset", 0)
        vars(self).setdefault("valueString", None)
        vars(self).setdefault("valueTotalDigits", 0)

    def _init_fields(self) -> None:
        if "primitiveLongUtil" not in vars(self): self.primitiveLongUtil: PrimitiveLongUtil = None
        if "prependString" not in vars(self): self.prependString: str = None
        if "PREPEND_STRING" not in vars(self): self.PREPEND_STRING: list[str] = None
        if "value" not in vars(self): self.value: int = 0
        if "max" not in vars(self): self.max: int = 0
        if "offset" not in vars(self): self.offset: int = 0
        if "valueString" not in vars(self): self.valueString: list[str] = None
        if "valueTotalDigits" not in vars(self): self.valueTotalDigits: int = 0
    

    def __init__(self, prependString: str, max: int, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
        from org.allbinary.graphics.color.BasicColor import BasicColor
        from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
        from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
        super().__init__(location, direction, bufferZone, basicColor)
        __class__._init_fields(self)
        self.prependString = prependString
        self.PREPEND_STRING = list(prependString)
        self.valueString = PrimitiveLongSingleton.getInstance().NUMBER_CHAR_ARRAYS[0]
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(max + 1)
        self.max = max
        self.value = 0
        if direction == 0:
            raise RuntimeError(BasicHudFactory.getInstance().DIRECTION_EXCEPTION)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.offset = font.stringWidth(self.prependString) + MyFontProcessor.defaultCharWidth(font)
        java_super_call(super(), "updateMeasurement", graphics)
    

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
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintDX", graphics, self.PREPEND_STRING, 0, len(self.PREPEND_STRING), self.valueString, 0, self.valueTotalDigits, self.offset)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        charArray: list[str] = self.PREPEND_STRING
        len_: int = len(self.PREPEND_STRING)
        charArray2: list[str] = self.valueString
        len2: int = self.valueTotalDigits
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        graphics.drawChars(charArray, 0, len_, x, y, 0)
        graphics.drawChars(charArray2, 0, len2, x - self.offset, y, 0)
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
# from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil


