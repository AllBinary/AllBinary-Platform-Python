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
# package org.allbinary.game.displayable.screen

from __future__ import annotations

# from javax.microedition.lcdui.Command import Command
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.graphics.form.item.CustomTextBox import CustomTextBox


class LicenseRegistrationTextBox(CustomTextBox):
    DISPLAY_COMMAND: Command = Command("Register", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 3)
    SUBMIT_COMMAND: Command = Command("Submit", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 3)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.pleaseWaitPaintable: Paintable = SimpleTextPaintable(self.commonStrings.PLEASE_WAIT, BasicColorFactory.getInstance().WHITE)
        self.paintable: Paintable = NullPaintable.getInstance()
    

    def __init__(self, cmdListener: CommandListener, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(cmdListener, "Enter Registration Code:", StringUtil.getInstance().EMPTY_STRING, 60, TextField.ANY, Font.getDefaultFont(), backgrounBasicColor, foregroundBasicColor)
        self._init_fields()
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.addCommand(GameCommandsFactory.getInstance().TOGGLE_KEYBOARD)
        self.addCommand(LicenseRegistrationTextBox.SUBMIT_COMMAND)
        self.setCommandListener(cmdListener)
    

    def open(self) -> None:
        try:
            virtualKeyboardEventHandler: VirtualKeyboardEventHandler = VirtualKeyboardEventHandler.getInstance()
            virtualKeyboardEventHandler.fireEvent(virtualKeyboardEventHandler.SHOW_EVENT)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "open", e)
        super().open()
        self.paintable = NullPaintable.getInstance()
        self.repaint()
    

    # throws Exception
    def close(self) -> None:
        try:
            virtualKeyboardEventHandler: VirtualKeyboardEventHandler = VirtualKeyboardEventHandler.getInstance()
            virtualKeyboardEventHandler.fireEvent(virtualKeyboardEventHandler.HIDE_EVENT)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "open", e)
        self.paintable = self.pleaseWaitPaintable
        self.repaint()
        super().close()
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        self.paintable.paint(graphics)
    

    def submit(self) -> None:
        commandListener: CommandListener = self.getCustomCommandListener()
        commandListener.commandAction(LicenseRegistrationTextBox.SUBMIT_COMMAND, self)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.TextField import TextField
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.graphics.paint.SimpleTextPaintable import SimpleTextPaintable
from org.allbinary.input.event.VirtualKeyboardEventHandler import VirtualKeyboardEventHandler


