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
# package org.allbinary.animation.text

from __future__ import annotations

from org.allbinary.animation.text.TextAnimation import TextAnimation
from org.allbinary.animation.text.TextInterface import TextInterface


class CustomTextAnimation(TextAnimation, TextInterface):

    def _init_fields(self) -> None:
        self.fontDebugFactory: FontDebugFactory = FontDebugFactory.getInstance()
        self.fontSize: int = None
        self.font: Font = None
        self.lastText: str = StringUtil.getInstance().INIT_STRING
        self.hasChanged: bool = True
        self.textWidth: int = 0
    

    def __init__(self, text: str, fontSize: int, animationBehavior: AnimationBehavior) -> None:
        super().__init__(text, animationBehavior)
        self._init_fields()
        self.fontSize = fontSize
        self.font = Font.getFont(Font.FACE_SYSTEM, Font.STYLE_PLAIN, fontSize)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        existingFont: Font = graphics.getFont()
        self.fontDebugFactory.setFont(self.font, graphics)
        super().paintXYNoUpdate(graphics, x, y)
        self.fontDebugFactory.setFont(existingFont, graphics)
    

    def setScale(self, scaleX: float, scaleY: float) -> None:
        if scaleX != scaleY:
            raise RuntimeError()
        self.hasChanged = True
        self.font = Font.getFont(Font.FACE_SYSTEM, Font.STYLE_PLAIN, int((float(self.fontSize) * scaleX)))
    

    def setText(self, text: str) -> None:
        if self.lastText != text:
            self.hasChanged = True
            self.lastText = text
            super().setText(text)
    

    def getText(self) -> str:
        return self.lastText
    

    def getWidth(self) -> int:
        if self.hasChanged:
            self.textWidth = self.font.stringWidth(self.textArrayP[0])
            self.hasChanged = False
        return self.textWidth
    

    def getFontHeight(self) -> int:
        return self.font.getHeight()
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.font.FontDebugFactory import FontDebugFactory
from org.allbinary.logic.string.StringUtil import StringUtil


