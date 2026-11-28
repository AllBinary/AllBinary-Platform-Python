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
# package org.allbinary.graphics.paint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class SimpleTextPaintable(*java_bases(Paintable, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("displayInfoSingleton", None)
        vars(self).setdefault("updateMyFontProcessor", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("text", None)
        vars(self).setdefault("basicColor", None)
        vars(self).setdefault("topScoresWidth", 0)
        vars(self).setdefault("fontHeight", 0)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        if "text" not in vars(self): self.text: str = None
        if "basicColor" not in vars(self): self.basicColor: BasicColor = None
        self.topScoresWidth: int = 0
        self.fontHeight: int = 0
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, text: str, basicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__()
        __class__._init_fields(self)
        self.text = text
        self.basicColor = basicColor
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.topScoresWidth = (font.stringWidth(self.text) >> 1)
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        width: int = self.displayInfoSingleton.getLast()[self.displayInfoSingleton.WIDTH]
        graphics.setColor(int(self.getBasicColorP()))
        graphics.drawString(self.text, (int(width) >> (int(1) & 31)) - self.topScoresWidth, self.fontHeight, self.anchor)
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return self.basicColor
    

    def setText(self, text: str) -> None:
        self.text = text
        self.myFontProcessor = self.updateMyFontProcessor
    

    def getText(self) -> str:
        return self.text
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor


