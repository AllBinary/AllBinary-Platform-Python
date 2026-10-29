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

from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class TextAnimation(IndexedAnimation, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.textArrayP: list[str] = StringUtil.getInstance().ONE_EMPTY_STRING_ARRAY
        self.anchor: int = Anchor.TOP_LEFT
        self.fontHeight: int = 0
        self.offsetY: int = 0
        self.textChangeListener: TextChangeListener = TextChangeListener.getInstance()
    

    def __init__(self, text: str, animationBehavior: AnimationBehavior) -> None:
        super().__init__(animationBehavior)
        self._init_fields()
        self.setText(text)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from org.allbinary.animation.text.TextChangeListener import TextChangeListener
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        adjustedFontHeight: int = int(-(float(self.fontHeight) * 2.00))
        self.offsetY = (adjustedFontHeight if SWTJOGLProcessor.getInstance().isJOGL() else 0)
        self.textChangeListener.onMeasure()
        self.textChangeListener = TextChangeListener.getInstance()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    # throws Exception
    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        self.paintXYNoUpdate(graphics, x, y)
    

    def paintXYNoUpdate(self, graphics: Graphics, x: int, y: int) -> None:
        self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
        size: int = len(self.textArrayP)
        for index in range(0, size):
            graphics.drawString(self.textArrayP[index], x, y + self.offsetY + (index * self.fontHeight), self.anchor)
    

    def setTextWithOnMeasure(self, text: str, textChangeListener: TextChangeListener) -> None:
        self.setText(text)
        self.textChangeListener = textChangeListener
    

    def setText(self, text: str) -> None:
        list_: BasicArrayList = BasicArrayListD()
        if text is not None and len(text) > 0:
            index: int = 0
            startIndex: int = 0
            endIndex: int = 0
            while index >= 0:
                startIndex = index
                index = text.find('\n', startIndex)
                endIndex = index
                if index < 0:
                    endIndex = len(text)
                list_.add(text[startIndex:endIndex])
                if index < 0:
                    break
                index += 1
        if list_.size() > 0:
            textArray: list[str] = [None] * (list_.size())
            size: int = list_.size()
            for index in range(0, size):
                textArray[index] = list_.get(index)
            self.textArrayP = textArray
        else:
            self.textArrayP = StringUtil.getInstance().ONE_EMPTY_STRING_ARRAY
        self.myFontProcessor = self.updateMyFontProcessor
    

    def getTextArray(self) -> list[str]:
        return self.textArrayP
    

    def getFontHeight(self) -> int:
        return self.fontHeight
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.graphics.threed.SWTJOGLProcessor import SWTJOGLProcessor
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.animation.text.TextChangeListener import TextChangeListener


