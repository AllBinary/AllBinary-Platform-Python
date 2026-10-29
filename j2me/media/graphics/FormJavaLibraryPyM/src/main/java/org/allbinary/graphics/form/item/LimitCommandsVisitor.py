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

from org.allbinary.logic.util.visitor.Visitor import Visitor


class LimitCommandsVisitor(Visitor):

    def _init_fields(self) -> None:
        self.isNotSmallDisplay: bool = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.isNotSmallDisplay = (displayInfo.isPortrait() and displayInfo.getLastHeight() > ScreenInfo.getInstance().SMALL_WIDTH) or (not displayInfo.isPortrait() and displayInfo.getLastHeight() > ScreenInfo.getInstance().SMALL_HEIGHT)
    

    def visit(self, anyType: object) -> object:
        command: Command = anyType
        booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        if self.isNotSmallDisplay or command.getPriority() == 1 or command == GameCommandsFactory.getInstance().EXIT_COMMAND or command == GameCommandsFactory.getInstance().EXIT_WITHOUT_PROGRESS_COMMAND:
            return booleanFactory.TRUE
        else:
            return booleanFactory.FALSE
# from javax.microedition.lcdui.Command import Command
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.form.ScreenInfo import ScreenInfo
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory


