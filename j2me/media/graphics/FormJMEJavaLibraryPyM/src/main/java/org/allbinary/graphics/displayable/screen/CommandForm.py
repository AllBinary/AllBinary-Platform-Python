# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations

# from javax.microedition.lcdui.Form import Form
from org.allbinary.game.displayable.canvas.MenuListener import MenuListener
from org.allbinary.graphics.displayable.command.MyCommandInterface import MyCommandInterface
from org.allbinary.logic.NullUtil import NullUtil


class CommandForm(Form, MyCommandInterface, MenuListener):
    NULL_COMMAND_FORM: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.repaintProcessor: Processor = ScreenRepaintProcessorFactory.getInstance().create(self)
        self.commandStack: ABStack[object] = None
    

    @staticmethod
    def getNullCommandForm() -> CommandForm:
        if CommandForm.NULL_COMMAND_FORM == NullUtil.getInstance().NULL_OBJECT:
            CommandForm.NULL_COMMAND_FORM = CommandForm(NullCommandListener.NULL_COMMAND_LISTENER, StringUtil.getInstance().EMPTY_STRING, BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE)
        return CommandForm.NULL_COMMAND_FORM
    

    def __init__(self, commandListener: CommandListener, formTitle: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(formTitle)
        self._init_fields()
        self.commandStack = StdUtil.getInstance().createStack()
        try:
            self.repaintProcessor.process()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        pass
    

    def open(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "open")
    

    # throws Exception
    def close(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CLOSE)
    

    # throws Exception
    def update(self) -> None:
        self.repaintProcessor.process()
    

    def getSourceId(self) -> int:
        return 0
    

    def addCommand(self, command: Command) -> None:
        self.commandStack.push(command)
        super().addCommand(command)
    

    def removeAllCommands(self) -> None:
        size: int = self.commandStack.size()
        for index in range(0, size):
            super().removeCommand(self.commandStack.pop())
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
from org.allbinary.canvas.Processor import Processor
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABStack import ABStack
from org.allbinary.graphics.displayable.screen.ScreenRepaintProcessorFactory import ScreenRepaintProcessorFactory


