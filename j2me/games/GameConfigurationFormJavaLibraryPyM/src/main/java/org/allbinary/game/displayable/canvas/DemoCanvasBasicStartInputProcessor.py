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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.game.displayable.canvas.BasicMenuInputProcessor import BasicMenuInputProcessor


class DemoCanvasBasicStartInputProcessor(BasicMenuInputProcessor):
    

    def __init__(self, gameKeyEventList: BasicArrayList, gameCanvas: RunnableCanvas) -> None:
        super().__init__(gameKeyEventList, -1, gameCanvas)
    

    # throws Exception
    def processInputList(self) -> int:
        list_: BasicArrayList = self.getGameKeyEventList()
        size: int = list_.size()
        gameKeyEvent: GameKeyEvent = None
        for index in range(0, size):
            gameKeyEvent = list_.objectArray[index]
            self.logUtil.putF(str(StringMaker().append("Start GameKey: ").append(StringUtil.getInstance().toString(gameKeyEvent))), self, GameInputStrings.getInstance().PROCESS_INPUT)
        self.getCanvas().getCustomCommandListener().commandAction(GameCommandsFactory.getInstance().START_COMMAND, NullCanvas.NULL_CANVAS)
        return size
# from javax.microedition.lcdui.NullCanvas import NullCanvas
from org.allbinary.canvas.RunnableCanvas import RunnableCanvas
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.input.GameInputStrings import GameInputStrings
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList


