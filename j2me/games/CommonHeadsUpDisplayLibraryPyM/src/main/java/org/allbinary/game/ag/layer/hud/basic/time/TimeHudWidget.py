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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.graphics.hud.BasicHud import BasicHud


@java_inherited_overloads
class TimeHudWidget(BasicHud):
    def _java_defaults(self):
        vars(self).setdefault("TIME_STRING", None)
        vars(self).setdefault("TIME_CHAR_ARRAY", None)
        vars(self).setdefault("offset", 0)
        vars(self).setdefault("string", None)
        vars(self).setdefault("totalDigits", 0)
        vars(self).setdefault("timer", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton
        self.TIME_STRING: str = "Time "
        self.TIME_CHAR_ARRAY: list[str] = ['T', 'i', 'm', 'e', ' ']
        if "offset" not in vars(self): self.offset: int = 0
        self.string: list[str] = PrimitiveLongSingleton.getInstance().ZERO
        self.totalDigits: int = 1
        if "timer" not in vars(self): self.timer: HudTimer = None
    

    # throws Exception
    @staticmethod
    def getInstance(location: int, direction: int, basicColor: BasicColor, timer: HudTimer) -> TimeHudWidget:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return TimeHudWidget(location, direction, 2, basicColor, timer)
    

    def __init__(self, location: int, direction: int, bufferZone: int, basicColor: BasicColor, timer: HudTimer) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(location, direction, bufferZone, basicColor)
        __class__._init_fields(self)
        self.timer = timer
        self.set()
        self.updateMaxHeight = 14
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.updateMaxWidth = font.getSize() * 5
        self.offset = font.stringWidth(self.TIME_STRING) + MyFontProcessor.defaultStringWidth(font, 3)
        java_super_call(super(), "updateMeasurement", graphics)
    

    def update(self) -> None:
        self.timer.update()
        self.set()
    

    def set(self) -> None:
        self.string = self.timer.getTimeChars()
        self.totalDigits = self.timer.getCurrentTotalDigits()
    

    def getTimer(self) -> HudTimer:
        return self.timer
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        java_super_call(super(), "paintDX", graphics, self.TIME_CHAR_ARRAY, 0, len(self.TIME_CHAR_ARRAY), self.string, 0, self.totalDigits, self.offset)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.logic.math.PrimitiveLongSingleton import PrimitiveLongSingleton


