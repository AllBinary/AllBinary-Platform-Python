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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class PressStartMenuPaintable(*java_bases(Paintable, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("displayInfo", None)
        vars(self).setdefault("PRESS_START", None)
        vars(self).setdefault("KEY_START", None)
        vars(self).setdefault("MENU_START", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("startString", None)
        vars(self).setdefault("timeDelayHelper", None)
        vars(self).setdefault("flash", False)
        vars(self).setdefault("anchor", 0)
        vars(self).setdefault("beginWidth", 0)
        vars(self).setdefault("line", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.PRESS_START: str = "Press Screen To Start"
        self.KEY_START: str = "Press or Click F2 To Begin"
        self.MENU_START: str = "Press Start From The Menu To Begin"
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.startString: str = StringUtil.getInstance().EMPTY_STRING
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(1100)
        if "flash" not in vars(self): self.flash: bool = False
        self.anchor: int = Anchor.TOP_LEFT
        if "beginWidth" not in vars(self): self.beginWidth: int = 0
        if "line" not in vars(self): self.line: int = 0
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.AppletUtil import AppletUtil
        from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
        super().__init__()
        __class__._init_fields(self)
        if java_predicate(TouchScreenFactory.getInstance(), "isTouch"):
            self.startString = self.PRESS_START
        elif AppletUtil.isAppletLoader(self):
            self.startString = self.KEY_START
        else:
            self.startString = self.MENU_START
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.beginWidth = (graphics.getFont().stringWidth(self.startString) >> 1)
        self.line = (4 * MyFontProcessor.defaultCharWidth(font)) + (font.getHeight() >> 1)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        if java_predicate(self.timeDelayHelper, "isTimeTNT"):
            if java_predicate(self, "isFlash"):
                self.setFlash(False)
            else:
                self.setFlash(True)
        if java_predicate(self, "isFlash"):
            self.myFontProcessor.process(graphics)
            graphics.drawString(self.startString, self.displayInfo.getLastHalfWidth() - self.beginWidth, self.displayInfo.getLastHeight() - self.line, self.anchor)
    

    def setFlash(self, flash: bool) -> None:
        self.flash = flash
    

    def isFlash(self) -> bool:
        return self.flash
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.AppletUtil import AppletUtil
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


