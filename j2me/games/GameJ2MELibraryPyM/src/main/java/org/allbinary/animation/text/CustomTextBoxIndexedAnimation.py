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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.game.input.event.RawKeyEventListener import RawKeyEventListener
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.animation.text.TextInterface import TextInterface


@java_inherited_overloads
class CustomTextBoxIndexedAnimation(*java_bases(IndexedAnimation, RawKeyEventListener, UpdateMyFontInterface, TextInterface)):
    def _java_defaults(self):
        vars(self).setdefault("customTextBox", None)
        vars(self).setdefault("lastText", None)
        vars(self).setdefault("hasChanged", False)
        vars(self).setdefault("textChangeListener", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        if "customTextBox" not in vars(self): self.customTextBox: CustomTextBox = None
        self.lastText: str = StringUtil.getInstance().INIT_STRING
        self.hasChanged: bool = True
        self.textChangeListener: TextChangeListener = TextChangeListener.getInstance()
    

    def __init__(self, customTextBox: CustomTextBox) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox
        super().__init__(AnimationBehavior.getInstance())
        __class__._init_fields(self)
        self.customTextBox = customTextBox
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.customTextBox.getTextFieldItem().setForegroundBasicColorP(basicColor)
    

    def setBackgroundBasicColorP(self, basicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.customTextBox.getTextFieldItem().setBackgroundBasicColorP(basicColor)
    

    def setTextWithOnMeasure(self, text: str, textChangeListener: TextChangeListener) -> None:
        self.setText(text)
        self.textChangeListener = textChangeListener
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from org.allbinary.animation.text.TextChangeListener import TextChangeListener
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
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
        from javax.microedition.lcdui.Graphics import Graphics
        self.customTextBox.paintXY(graphics, x, y)
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def getWidth(self) -> int:
        return java_super_call(super(), "getWidth")
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox
# from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.animation.text.TextChangeListener import TextChangeListener


