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
# package org.allbinary.game.configuration

from __future__ import annotations

import time
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm


class SaveGameForm(CommandForm):
    FORM: CommandForm = CommandForm.getNullCommandForm()

    def _init_fields(self) -> None:
        self.meUtil: MEUtil = MEUtil.getInstance()
    

    # throws Exception
    @staticmethod
    def createForm(commandListener: CommandListener, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> CommandForm:
        SaveGameForm.FORM = SaveGameForm(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        return SaveGameForm.FORM
    

    @staticmethod
    def getInstance() -> CommandForm:
        return SaveGameForm.FORM
    

    def __init__(self, commandListener: CommandListener, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        timeString: str = str(ABSystemWrapper.getInstance().currentTimeMillis())
        self.meUtil.appendItem(self, TextField("Name: ", timeString, 30, TextField.ANY))
        self.initCommands(commandListener)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        self.removeAllCommands()
        self.addCommand(gameCommandsFactory.SAVE)
        self.addCommand(gameCommandsFactory.CLOSE_AND_SHOW_GAME_CANVAS)
        self.setCommandListener(cmdListener)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.TextField import TextField
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper
from org.allbinary.logic.MEUtil import MEUtil


