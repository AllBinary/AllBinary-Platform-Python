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
# package org.allbinary.game.score

from __future__ import annotations



class HighScoreCommands:
    instance: HighScoreCommands = None

    def _init_fields(self) -> None:
        self.DISPLAY: Command = Command("Scores", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.PERSONAL: Command = Command("Personal", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.WORLD: Command = Command("World", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> HighScoreCommands:
        return HighScoreCommands.instance
# from javax.microedition.lcdui.Command import Command
from org.allbinary.logic.string.StringUtil import StringUtil


HighScoreCommands.instance = HighScoreCommands()

