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
# package org.allbinary.game.midlet

from __future__ import annotations

import threading
from org.allbinary.game.midlet.GameMidlet import GameMidlet


class DemoGameMidlet(GameMidlet):
    _lock = threading.RLock()
    

    def __init__(self, clientInformationFactory: ClientInformationFactory) -> None:
        super().__init__(clientInformationFactory)
    

    # throws Exception
    def isContinue(self) -> bool:
        hashtable: ABHashtable[object, object] = self.getStartStateHashtable()
        if hashtable is not None and hashtable.size() > 0:
            return True
        else:
            return False
    

    def getHighestLevel(self) -> int:
        return 1
    

    # throws Exception
    def createDemoGameCanvasRunnableInterface(self) -> GameCanvasRunnableInterface:
        self.logUtil.putF(self.commonStrings.NOT_IMPLEMENTED, self, self.commonStrings.CREATE)
        return NullGameCanvasRunnable.NULL_GAME_CANVAS_RUNNABLE
    

    # throws Exception
    def createGameCanvasRunnable(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> GameCanvasRunnableInterface:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def createGameCanvasRunnableInterface(self) -> GameCanvasRunnableInterface:
        return self.createGameCanvasRunnable(self.createGameLayerManager())
    

    def demoSetup(self) -> None:
        pass
    

    def postDemoSetup(self) -> None:
        pass
    

    # throws Exception
    def setDemo(self) -> None:
        with self._lock:
            return self._setDemo_unlocked()

    def _setDemo_unlocked(self) -> None:
        from org.allbinary.game.midlet.DemoRunnable import DemoRunnable
        self.logUtil.putF(self.commonStrings.START, self, "setDemo")
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.start()
        PrimaryThreadPool.getInstance().runTask(DemoRunnable(self))
    

    # throws Exception
    def createGame(self) -> None:
        with self._lock:
            return self._createGame_unlocked()

    def _createGame_unlocked(self) -> None:
        from org.allbinary.game.midlet.CreateGameRunnable import CreateGameRunnable
        CREATE_GAME: str = "createGame"
        self.logUtil.putF(self.commonStrings.START, self, CREATE_GAME)
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.start()
        hashtable: ABHashtable[object, object] = self.getStartStateHashtable()
        self.setStartStateHashtable(StdUtil.getInstance().NULL_TABLE)
        PrimaryThreadPool.getInstance().runTask(CreateGameRunnable(self, hashtable))
        self.logUtil.putF(self.commonStrings.END, self, CREATE_GAME)
    

    def isReady(self) -> bool:
        return True
from org.allbinary.game.displayable.canvas.GameCanvasRunnableInterface import GameCanvasRunnableInterface
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.system.security.licensing.ClientInformationFactory import ClientInformationFactory
from org.allbinary.thread.PrimaryThreadPool import PrimaryThreadPool
from org.allbinary.game.displayable.canvas.NullGameCanvasRunnable import NullGameCanvasRunnable
from org.allbinary.util.ABHashtable import ABHashtable


