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

# from javax.microedition.lcdui.Command import Command
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm
from org.allbinary.logic.string.StringUtil import StringUtil


class InGameOptionsForm(CommandForm):
    DISPLAY: Command = Command("Options In Game", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
    SAVE: Command = Command("Save", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
    DEFAULT: Command = Command("Default", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
    

    def __init__(self, commandListener: CommandListener, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        gameFeatureFormUtil: GameFeatureFormUtil = GameFeatureFormUtil.getInstance()
        gameFeatureFormUtil.addChoiceGroup(self, InGameFeatureChoiceGroups.getExclusiveInstance().get(), Choice.EXCLUSIVE)
        gameFeatureFormUtil.addChoiceGroup(self, InGameFeatureChoiceGroups.getMultipleInstance().get(), Choice.MULTIPLE)
        self.initCommands(commandListener)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.addCommand(InGameOptionsForm.DEFAULT)
        self.setCommandListener(cmdListener)
# from javax.microedition.lcdui.Choice import Choice
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.feature.GameFeatureFormUtil import GameFeatureFormUtil
from org.allbinary.game.configuration.feature.InGameFeatureChoiceGroups import InGameFeatureChoiceGroups
from org.allbinary.graphics.color.BasicColor import BasicColor


