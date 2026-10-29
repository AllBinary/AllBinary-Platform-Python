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
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.game.displayable.canvas.GameCommandCanvas import GameCommandCanvas
from org.allbinary.game.input.event.RawKeyEventListener import RawKeyEventListener


class CustomTextBox(GameCommandCanvas, RawKeyEventListener):

    def _init_fields(self) -> None:
        self.textFieldItem: ABTextFieldItem = None
        self.inputFactory: InputFactory = InputFactory.getInstance()
    

    def __init__(self, cmdListener: CommandListener, label: str, text: str, maxSize: int, constraints: int, font: Font, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.form.item.ABTextFieldItem import ABTextFieldItem
        super().__init__(cmdListener, label, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        stringUtil: StringUtil = StringUtil.getInstance()
        textFieldItem: ABTextFieldItem = ABTextFieldItem(self, TextItemVisitor(), stringUtil.EMPTY_STRING, stringUtil.EMPTY_STRING, maxSize, 0, stringUtil.EMPTY_STRING, font, backgroundBasicColor, foregroundBasicColor)
        textFieldItem.setString(text)
        self.textFieldItem = textFieldItem
        self.setTitle(label)
    

    def submit(self) -> None:
        pass
    

    def onEventRaw(self, keyCode: int, deviceId: int, repeated: bool) -> None:
        self.logUtil.putF(str(StringMaker().append(self.commonStrings.START).appendint(keyCode)), self, "onEvent")
        self.keyPressedByDevice(keyCode, deviceId)
    

    def keyPressed(self, keyCode: int) -> None:
        self.keyPressedByDevice(keyCode, 0)
    

    def keyReleased(self, keyCode: int) -> None:
        self.keyReleasedByDevice(keyCode, 0)
    

    def keyRepeated(self, keyCode: int) -> None:
        self.keyRepeatedByDevice(keyCode, 0)
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        try:
            self.logUtil.putF(str(StringMaker().append(CommonSeps.getInstance().SPACE).appendint(keyCode)), self, self.gameInputStrings.KEY_PRESSED)
            platformKeyFactory: PlatformKeyFactory = PlatformKeyFactory.getInstance()
            input: Input = self.inputFactory.getInstanceById(keyCode)
            if platformKeyFactory.isSubmission(input):
                self.submit()
            else:
                self.textFieldItem.keyPressed(keyCode)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.KEY_PRESSED, e)
    

    def keyReleasedByDevice(self, keyCode: int, deviceId: int) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        graphics.setColor(self.backgroundColor)
        graphics.fillRect(0, 0, self.displayInfo.getLastWidth(), self.displayInfo.getLastHeight())
        graphics.setColor(self.foregroundColor)
        if not J2MEUtil.isJ2ME():
            graphics.drawString(self.getTitle(), 8, 1, 0)
        self.paintXY(graphics, 8, graphics.getFont().getHeight() + 2)
        super().paint(graphics)
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.textFieldItem.paintXY(graphics, x, y)
    

    def getTextFieldItem(self) -> ABTextFieldItem:
        return self.textFieldItem
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.game.input.PlatformKeyFactory import PlatformKeyFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.form.item.validation.TextItemVisitor import TextItemVisitor
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps


