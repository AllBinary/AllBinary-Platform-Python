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
# package org.allbinary.game.commands

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class GameCommandsFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.TOGGLE_FULLSCREEN: Command = Command("Toggle FullScreen", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.TOGGLE_KEYBOARD: Command = Command("Keyboard", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.SET_MENU_DISPLAYABLE: Command = Command("Set Menu Displayable", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.APPLICATION_UPDATE: Command = Command(CommonStrings.getInstance().UPDATE, StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.DISPLAY_ABOUT: Command = Command(CanvasStrings.getInstance().ABOUT, StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 2)
        self.OPEN_WEB_URL: Command = Command("Open Web URL", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 2)
        self.CLOSE_OPTIONS: Command = Command("Back", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.DISPLAY_OPTIONS: Command = Command(CanvasStrings.getInstance().OPTIONS, StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 2)
        self.START_TRACE: Command = Command("Start Trace", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.STOP_TRACE: Command = Command("Stop Trace", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.DEFAULT_OPTIONS: Command = Command("Default", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.SHOW_GAME_CANVAS: Command = Command("Back to Game", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.CLOSE_AND_SHOW_GAME_CANVAS: Command = Command("Back", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.QUIT_COMMAND: Command = Command("Quit", StringUtil.getInstance().EMPTY_STRING, Command.STOP, 1)
        self.RESTART_COMMAND: Command = Command("Restart", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 0)
        self.DISPLAY_SAVE_FORM: Command = Command("Save To", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 3)
        self.SAVE: Command = Command("Save", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 3)
        self.DISPLAY_LOAD_FORM: Command = Command("Load", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 3)
        self.LOAD_FILE: Command = Command("Load File", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 3)
        self.DELETE_FILE: Command = Command("Delete File", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.EXIT_COMMAND: Command = Command("Exit", StringUtil.getInstance().EMPTY_STRING, Command.EXIT, 2)
        self.EXIT_WITHOUT_PROGRESS_COMMAND: Command = Command("Exit Without Progress", StringUtil.getInstance().EMPTY_STRING, Command.EXIT, 2)
        self.START_COMMAND: Command = Command(CommonStrings.getInstance().START, StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.CONTINUE_COMMAND: Command = Command("Continue", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.SELECT_COMMAND: Command = Command("Select", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.FEATURE_UPDATE: Command = Command("Feature Update", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
        self.BUY_COMMAND: Command = Command("BUY", StringUtil.getInstance().EMPTY_STRING, Command.SCREEN, 1)
    

    @staticmethod
    def getInstance() -> GameCommandsFactory:
        if GameCommandsFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            GameCommandsFactory.instance = GameCommandsFactory()
        return GameCommandsFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
# from javax.microedition.lcdui.Command import Command
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


