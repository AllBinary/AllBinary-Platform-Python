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



class HighScoreCommandsBaseFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.HIGH_SCORE_COMMANDS: list[Command] = None
    

    def __init__(self, HIGH_SCORE_COMMANDS: list[Command]) -> None:
        self._init_fields()
        self.HIGH_SCORE_COMMANDS = HIGH_SCORE_COMMANDS
    

    def isHighScoreCommand(self, command: Command) -> bool:
        for index in range(len(self.HIGH_SCORE_COMMANDS) - 1, 0 - 1, -1):
            if command == self.HIGH_SCORE_COMMANDS[index]:
                return True
        return False
    

    # throws Exception
    def getIndex(self, command: Command) -> int:
        for index in range(len(self.HIGH_SCORE_COMMANDS) - 1, 0 - 1, -1):
            if command == self.HIGH_SCORE_COMMANDS[index]:
                return index
        raise Exception("No Such Command")
# from javax.microedition.lcdui.Command import Command
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


