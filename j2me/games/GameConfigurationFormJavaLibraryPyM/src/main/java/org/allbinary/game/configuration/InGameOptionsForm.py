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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.displayable.screen.CommandForm import CommandForm


class InGameOptionsForm(CommandForm):
    DISPLAY: Command = None
    SAVE: Command = None
    DEFAULT: Command = None
    

    def __init__(self, commandListener: CommandListener, title: str, backgrounBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        from javax.microedition.lcdui.Choice import Choice
        from javax.microedition.lcdui.CommandListener import CommandListener
        from org.allbinary.game.configuration.feature.GameFeatureFormUtil import GameFeatureFormUtil
        from org.allbinary.game.configuration.feature.InGameFeatureChoiceGroups import InGameFeatureChoiceGroups
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(commandListener, title, backgrounBasicColor, foregroundBasicColor)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        gameFeatureFormUtil: GameFeatureFormUtil = GameFeatureFormUtil.getInstance()
        gameFeatureFormUtil.addChoiceGroup(self, InGameFeatureChoiceGroups.getExclusiveInstance().get(), Choice.EXCLUSIVE)
        gameFeatureFormUtil.addChoiceGroup(self, InGameFeatureChoiceGroups.getMultipleInstance().get(), Choice.MULTIPLE)
        self.initCommands(commandListener)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        from javax.microedition.lcdui.CommandListener import CommandListener
        from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
        self.removeAllCommands()
        self.addCommand(GameCommandsFactory.getInstance().CLOSE_AND_SHOW_GAME_CANVAS)
        self.addCommand(InGameOptionsForm.DEFAULT)
        self.setCommandListener(cmdListener)
# from javax.microedition.lcdui.Choice import Choice
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
# from org.allbinary.game.configuration.feature.GameFeatureFormUtil import GameFeatureFormUtil
# from org.allbinary.game.configuration.feature.InGameFeatureChoiceGroups import InGameFeatureChoiceGroups
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.logic.string.StringUtil import StringUtil


def _InGameOptionsForm_DISPLAY() -> object:
    from javax.microedition.lcdui.Command import Command
    from org.allbinary.logic.string.StringUtil import StringUtil
    return Command("Options In Game", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)

lazy_static(InGameOptionsForm, "DISPLAY", _InGameOptionsForm_DISPLAY)

def _InGameOptionsForm_SAVE() -> object:
    from javax.microedition.lcdui.Command import Command
    from org.allbinary.logic.string.StringUtil import StringUtil
    return Command("Save", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)

lazy_static(InGameOptionsForm, "SAVE", _InGameOptionsForm_SAVE)

def _InGameOptionsForm_DEFAULT() -> object:
    from javax.microedition.lcdui.Command import Command
    from org.allbinary.logic.string.StringUtil import StringUtil
    return Command("Default", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)

lazy_static(InGameOptionsForm, "DEFAULT", _InGameOptionsForm_DEFAULT)

