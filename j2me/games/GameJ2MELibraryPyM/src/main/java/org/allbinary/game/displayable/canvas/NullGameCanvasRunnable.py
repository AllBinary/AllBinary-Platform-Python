# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

import threading
from org.allbinary.game.displayable.canvas.GameCanvasRunnableInterface import GameCanvasRunnableInterface


class NullGameCanvasRunnable(GameCanvasRunnableInterface):
    NULL_GAME_CANVAS_RUNNABLE: NullGameCanvasRunnable = None

    def _init_fields(self) -> None:
        self.gameStateFactory: GameStateFactory = GameStateFactory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def getTitle(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def isInitialized(self) -> bool:
        return False
    

    def isPaused(self) -> bool:
        return False
    

    def unPause(self) -> None:
        pass
    

    def pause(self) -> None:
        pass
    

    def isHighScoreSubmitted(self) -> bool:
        return False
    

    # throws Exception
    def setHighScoreSubmitted(self, highScoreSubmitted: bool) -> None:
        pass
    

    # throws Exception
    def processGameOver(self) -> None:
        pass
    

    def isGameOver(self) -> bool:
        return False
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        pass
    

    # throws Exception
    def getCurrentStateHashtable(self) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
    

    # throws Exception
    def getLoadStateHashtable(self) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
    

    # throws Exception
    def setLoadStateHashtable(self, hashtable: ABHashtable[object, object]) -> None:
        pass
    

    def getType(self) -> int:
        return -1
    

    # throws Exception
    def setGameState(self, gameState: GameState) -> None:
        pass
    

    def getGameState(self) -> GameState:
        return self.gameStateFactory.NO_GAME_STATE
    

    def itemStateChanged(self, item: Item) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    def isRunning(self) -> bool:
        return False
    

    def setRunning(self, isRunning: bool) -> None:
        pass
    

    # throws Exception
    def setThread(self, thread: threading.Thread) -> None:
        pass
    

    def run(self) -> None:
        pass
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Item import Item
from org.allbinary.game.state.GameState import GameState
from org.allbinary.game.state.GameStateFactory import GameStateFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.ABHashtable import ABHashtable


NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE = NullGameCanvasRunnable()

