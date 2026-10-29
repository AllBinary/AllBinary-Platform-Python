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

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME


class AllBinaryVisualDebugVibration(AllBinaryVibrationME, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(2147483647)
        self.VIBRATING: str = "Vibrating"
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.anchor: int = Anchor.TOP_LEFT
        self.width: int = 0

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.width = font.stringWidth(self.VIBRATING)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def vibrate(self, duration: int, type_: int, volume: int) -> None:
        self.timeDelayHelper.delay = duration
    

    def paint(self, graphics: Graphics) -> None:
        if self.timeDelayHelper.isTimeTNT():
            self.timeDelayHelper.delay = 2147483647
            self.myFontProcessor.process(graphics)
            graphics.drawString(self.VIBRATING, self.displayInfoSingleton.getLastHalfWidth() - (self.width >> 1), 0, self.anchor)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


