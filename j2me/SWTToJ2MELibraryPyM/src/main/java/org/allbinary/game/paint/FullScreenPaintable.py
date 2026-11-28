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
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


#SwtToJ2ME
@java_inherited_overloads
class FullScreenPaintable(*java_bases(Paintable, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("displayInfo", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("FULLSCREEN_TEXT", None)
        vars(self).setdefault("anchor", 0)
        vars(self).setdefault("Y", 0)
        vars(self).setdefault("beginWidth", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.FULLSCREEN_TEXT: str = "F11 - Toggle Fullscreen"
        self.anchor: int = Anchor.TOP_LEFT
        if "Y" not in vars(self): self.Y: int = 0
        if "beginWidth" not in vars(self): self.beginWidth: int = 0
    

    @staticmethod
    def getInstance() -> FullScreenPaintable:
        return FullScreenPaintable()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.Y = 4 * font.getHeight()
        self.beginWidth = (font.stringWidth(self.FULLSCREEN_TEXT) >> 1)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        halfWidth: int = self.displayInfo.getLastHalfWidth()
        height: int = self.displayInfo.getLastHeight()
        graphics.drawString(self.FULLSCREEN_TEXT, halfWidth - self.beginWidth, height - self.Y, self.anchor)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


