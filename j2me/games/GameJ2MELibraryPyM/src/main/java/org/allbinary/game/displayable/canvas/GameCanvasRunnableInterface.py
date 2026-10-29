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

# from javax.microedition.lcdui.ItemStateListener import ItemStateListener
from org.allbinary.game.state.GameStateCompositeInterface import GameStateCompositeInterface
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.thread.RunnableInterface import RunnableInterface


# Java interface
class GameCanvasRunnableInterface(RunnableInterface, PaintableInterface, ItemStateListener, GameStateCompositeInterface):
    

    def getTitle(self) -> str:
        raise NotImplementedError()
    

    def isInitialized(self) -> bool:
        raise NotImplementedError()
    

    def isPaused(self) -> bool:
        raise NotImplementedError()
    

    def unPause(self) -> None:
        raise NotImplementedError()
    

    def pause(self) -> None:
        raise NotImplementedError()
    

    def isHighScoreSubmitted(self) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def setHighScoreSubmitted(self, highScoreSubmitted: bool) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def processGameOver(self) -> None:
        raise NotImplementedError()
    

    def isGameOver(self) -> bool:
        raise NotImplementedError()
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getCurrentStateHashtable(self) -> ABHashtable[object, object]:
        raise NotImplementedError()
    

    # throws Exception
    def getLoadStateHashtable(self) -> ABHashtable[object, object]:
        raise NotImplementedError()
    

    # throws Exception
    def setLoadStateHashtable(self, hashtable: ABHashtable[object, object]) -> None:
        raise NotImplementedError()
    

    def getType(self) -> int:
        raise NotImplementedError()
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.util.ABHashtable import ABHashtable


