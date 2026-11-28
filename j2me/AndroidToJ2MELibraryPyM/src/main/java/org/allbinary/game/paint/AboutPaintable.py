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


#AndroidToJ2ME
@java_inherited_overloads
class AboutPaintable(*java_bases(Paintable, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("displayInfoSingleton", None)
        vars(self).setdefault("ABOUT", None)
        vars(self).setdefault("info", None)
        vars(self).setdefault("developers", None)
        vars(self).setdefault("paintableArray", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("charHeight", 0)
        vars(self).setdefault("aboutBeginWidth", 0)
        vars(self).setdefault("infoBeginWidth", None)
        vars(self).setdefault("developersBeginWidth", None)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.ABOUT: str = CanvasStrings.getInstance().ABOUT
        if "info" not in vars(self): self.info: list[str] = None
        if "developers" not in vars(self): self.developers: list[str] = None
        self.paintableArray: list[Paintable] = [self]
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        if "charHeight" not in vars(self): self.charHeight: int = 0
        if "aboutBeginWidth" not in vars(self): self.aboutBeginWidth: int = 0
        if "infoBeginWidth" not in vars(self): self.infoBeginWidth: list[int] = None
        if "developersBeginWidth" not in vars(self): self.developersBeginWidth: list[int] = None
        self.anchor: int = Anchor.TOP_LEFT
    

    @staticmethod
    def getInstance(info: list[str], developers: list[str]) -> AboutPaintable:
        return AboutPaintable(info, developers)
    

    def __init__(self, info: list[str], developers: list[str]) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.info = info
        self.infoBeginWidth = [0] * (len(self.info))
        self.developers = developers
        self.developersBeginWidth = [0] * (len(self.developers))
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.charHeight = font.getHeight()
        self.aboutBeginWidth = (font.stringWidth(self.ABOUT) >> 1)
        infoSize: int = len(self.info)
        for index in range(0, infoSize):
            self.infoBeginWidth[index] = (font.stringWidth(self.info[index]) >> 1)
        size: int = len(self.developers)
        for index in range(0, size):
            self.developersBeginWidth[index] = (font.stringWidth(self.developers[index]) >> 1)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def getPaintableArrayInstance(self) -> list[Paintable]:
        return self.paintableArray
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        halfWidth: int = self.displayInfoSingleton.getLastHalfWidth()
        graphics.drawString(self.ABOUT, halfWidth - self.aboutBeginWidth, 2 * self.charHeight, self.anchor)
        infoSize: int = len(self.info)
        for index in range(0, infoSize):
            graphics.drawString(self.info[index], halfWidth - self.infoBeginWidth[index], (4 + index) * self.charHeight, self.anchor)
        size: int = len(self.developers)
        for index in range(0, size):
            graphics.drawString(self.developers[index], halfWidth - self.developersBeginWidth[index], (5 + infoSize + index) * self.charHeight, self.anchor)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


