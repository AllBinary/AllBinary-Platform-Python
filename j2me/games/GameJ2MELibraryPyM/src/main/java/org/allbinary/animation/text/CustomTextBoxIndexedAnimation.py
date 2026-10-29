# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
from org.allbinary.game.input.event.RawKeyEventListener import RawKeyEventListener
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.animation.text.TextInterface import TextInterface


class CustomTextBoxIndexedAnimation(IndexedAnimation, RawKeyEventListener, UpdateMyFontInterface, TextInterface):

    def _init_fields(self) -> None:
        self.customTextBox: CustomTextBox = None
        self.lastText: str = StringUtil.getInstance().INIT_STRING
        self.hasChanged: bool = True
        self.textChangeListener: TextChangeListener = TextChangeListener.getInstance()
    

    def __init__(self, customTextBox: CustomTextBox) -> None:
        super().__init__(AnimationBehavior.getInstance())
        self._init_fields()
        self.customTextBox = customTextBox
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.customTextBox.getTextFieldItem().setForegroundBasicColorP(basicColor)
    

    def setBackgroundBasicColorP(self, basicColor: BasicColor) -> None:
        self.customTextBox.getTextFieldItem().setBackgroundBasicColorP(basicColor)
    

    def setTextWithOnMeasure(self, text: str, textChangeListener: TextChangeListener) -> None:
        self.setText(text)
        self.textChangeListener = textChangeListener
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from org.allbinary.animation.text.TextChangeListener import TextChangeListener
        font: Font = graphics.getFont()
        self.textChangeListener.onMeasure()
        self.textChangeListener = TextChangeListener.getInstance()
    

    def setText(self, text: str) -> None:
        if self.lastText != text:
            self.hasChanged = True
            self.lastText = text
            self.customTextBox.getTextFieldItem().setString(text)
    

    def getText(self) -> str:
        return self.customTextBox.getTextFieldItem().getString()
    

    def onEventRaw(self, keyCode: int, deviceId: int, repeated: bool) -> None:
        self.customTextBox.onEventRaw(keyCode, deviceId, repeated)
    

    def getFontHeight(self) -> int:
        return self.customTextBox.getTextFieldItem().getFontHeight()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.customTextBox.paintXY(graphics, x, y)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        pass
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.AnimationBehavior import AnimationBehavior
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.animation.text.TextChangeListener import TextChangeListener


