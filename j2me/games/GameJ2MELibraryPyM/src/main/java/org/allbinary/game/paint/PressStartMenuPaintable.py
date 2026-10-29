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
# package org.allbinary.game.paint

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


class PressStartMenuPaintable(Paintable, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.PRESS_START: str = "Press Screen To Start"
        self.KEY_START: str = "Press or Click F2 To Begin"
        self.MENU_START: str = "Press Start From The Menu To Begin"
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.startString: str = StringUtil.getInstance().EMPTY_STRING
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(1100)
        self.flash: bool = False
        self.anchor: int = Anchor.TOP_LEFT
        self.beginWidth: int = 0
        self.line: int = 0
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        if TouchScreenFactory.getInstance().isTouch():
            self.startString = self.PRESS_START
        elif AppletUtil.isAppletLoader(self):
            self.startString = self.KEY_START
        else:
            self.startString = self.MENU_START
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.beginWidth = (graphics.getFont().stringWidth(self.startString) >> 1)
        self.line = (4 * MyFontProcessor.defaultCharWidth(font)) + (font.getHeight() >> 1)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        if self.timeDelayHelper.isTimeTNT():
            if self.isFlash():
                self.setFlash(False)
            else:
                self.setFlash(True)
        if self.isFlash():
            self.myFontProcessor.process(graphics)
            graphics.drawString(self.startString, self.displayInfo.getLastHalfWidth() - self.beginWidth, self.displayInfo.getLastHeight() - self.line, self.anchor)
    

    def setFlash(self, flash: bool) -> None:
        self.flash = flash
    

    def isFlash(self) -> bool:
        return self.flash
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.AppletUtil import AppletUtil
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


