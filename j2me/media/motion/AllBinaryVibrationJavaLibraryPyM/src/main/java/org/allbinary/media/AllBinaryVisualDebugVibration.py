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
# package org.allbinary.media

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME


@java_inherited_overloads
class AllBinaryVisualDebugVibration(*java_bases(AllBinaryVibrationME, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("displayInfoSingleton", None)
        vars(self).setdefault("timeDelayHelper", None)
        vars(self).setdefault("VIBRATING", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("anchor", 0)
        vars(self).setdefault("width", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(2147483647)
        self.VIBRATING: str = "Vibrating"
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.anchor: int = Anchor.TOP_LEFT
        if "width" not in vars(self): self.width: int = 0

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.width = font.stringWidth(self.VIBRATING)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def vibrate(self, duration: int, type_: int, volume: int) -> None:
        self.timeDelayHelper.delay = duration
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        if java_predicate(self.timeDelayHelper, "isTimeTNT"):
            self.timeDelayHelper.delay = 2147483647
            self.myFontProcessor.process(graphics)
            graphics.drawString(self.VIBRATING, self.displayInfoSingleton.getLastHalfWidth() - (int(self.width) >> (int(1) & 31)), 0, self.anchor)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


