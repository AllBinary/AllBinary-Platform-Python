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
# package org.allbinary.graphics.displayable.command

from __future__ import annotations



class MyCommandsFactory:
    instance: MyCommandsFactory = None

    def _init_fields(self) -> None:
        self.NO_COMMAND: Command = Command(StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING, -1, -1)
        self.GAUGE_CHANGE: Command = Command("GAUGE_CHANGE", StringUtil.getInstance().EMPTY_STRING, Command.ITEM, 1)
        self.SET_DISPLAYABLE: Command = Command("Display", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 2)
        self.PAUSE_COMMAND: Command = Command("Pause", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 0)
        self.RESUME_COMMAND: Command = Command("Resume", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 0)
    

    @staticmethod
    def getInstance() -> MyCommandsFactory:
        return MyCommandsFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
# from javax.microedition.lcdui.Command import Command
from org.allbinary.logic.string.StringUtil import StringUtil


MyCommandsFactory.instance = MyCommandsFactory()

