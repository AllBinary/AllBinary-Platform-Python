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

import threading
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas


class NullGameCanvas(AllBinaryGameCanvas):
    instance: object = NullUtil.getInstance().NULL_OBJECT
    NO_GAME: str = "No Background Game"
    TYPE: int = 1
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.runningNull: bool = True
    

    @staticmethod
    def createNull() -> NullGameCanvas:
        try:
            return NullGameCanvas(AllBinaryGameLayerManager.getNullInstance())
        except Exception as e:
            LogUtil.getInstance().put(CommonStrings.getInstance().EXCEPTION, "NullGameCanvas", CommonStrings.getInstance().GET_INSTANCE, e)
            raise RuntimeError()
    

    @staticmethod
    def getInstance() -> NullGameCanvas:
        if NullGameCanvas.instance == NullUtil.getInstance().NULL_OBJECT:
            NullGameCanvas.instance = NullGameCanvas.createNull()
        return NullGameCanvas.instance
    

    # throws Exception
    @staticmethod
    def createCanvas(gameLayerManager: AllBinaryGameLayerManager) -> NullGameCanvas:
        nullGameCanvas: NullGameCanvas = NullGameCanvas(gameLayerManager)
        nullGameCanvas.setInitialized(True)
        nullGameCanvas.setTitle(NullGameCanvas.NO_GAME)
        return nullGameCanvas
    

    def __init__(self, gameLayerManager: AllBinaryGameLayerManager) -> None:
        super().__init__(NullCommandListener.NULL_COMMAND_LISTENER, gameLayerManager, NoHighScoresFactory.getInstance(), BasicBuildGameInitializerFactory.NULL_BASE_BUILD_GMAE_INITIALIZER_FACTORY, False)
        self._init_fields()
        super().setWait(1200)
    

    def isGameOver(self) -> bool:
        with self._lock:
            return self._isGameOver_unlocked()

    def _isGameOver_unlocked(self) -> bool:
        return False
    

    def setRunning(self, running: bool) -> None:
        self.runningNull = running
    

    def isRunning(self) -> bool:
        with self._lock:
            return self._isRunning_unlocked()

    def _isRunning_unlocked(self) -> bool:
        return self.runningNull
    

    def pause(self) -> None:
        with self._lock:
            return self._pause_unlocked()

    def _pause_unlocked(self) -> None:
        self.setPaused(True)
    

    def unPause(self) -> None:
        with self._lock:
            return self._unPause_unlocked()

    def _unPause_unlocked(self) -> None:
        self.setPaused(False)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        self.removeAllCommands()
        self.setCommandListener(cmdListener)
    

    # throws Exception
    def buildGameInit(self, isProgress: bool) -> None:
        pass
    

    def draw(self, graphics: Graphics) -> None:
        pass
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START_RUNNABLE, self, self.commonStrings.RUN)
            self.logUtil.putF(self.commonStrings.END_RUNNABLE, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
    

    def getType(self) -> int:
        return NullGameCanvas.TYPE
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
from org.allbinary.game.init.BasicBuildGameInitializerFactory import BasicBuildGameInitializerFactory
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


