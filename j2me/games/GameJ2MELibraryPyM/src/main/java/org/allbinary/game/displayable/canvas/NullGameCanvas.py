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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas


@java_inherited_overloads
class NullGameCanvas(AllBinaryGameCanvas):
    instance: object = None
    NO_GAME: str = "No Background Game"
    TYPE: int = 1
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("runningNull", False)

    def _init_fields(self) -> None:
        self.runningNull: bool = True
    

    @staticmethod
    def createNull() -> NullGameCanvas:
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            return NullGameCanvas(AllBinaryGameLayerManager.getNullInstance())
        except Exception as e:
            LogUtil.getInstance().put(CommonStrings.getInstance().EXCEPTION, "NullGameCanvas", CommonStrings.getInstance().GET_INSTANCE, e)
            raise RuntimeError()
    

    @staticmethod
    def getInstance() -> NullGameCanvas:
        from org.allbinary.logic.NullUtil import NullUtil
        if NullGameCanvas.instance == NullUtil.getInstance().NULL_OBJECT:
            NullGameCanvas.instance = NullGameCanvas.createNull()
        return NullGameCanvas.instance
    

    # throws Exception
    @staticmethod
    def createCanvas(gameLayerManager: AllBinaryGameLayerManager) -> NullGameCanvas:
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        nullGameCanvas: NullGameCanvas = NullGameCanvas(gameLayerManager)
        nullGameCanvas.setInitialized(True)
        nullGameCanvas.setTitle(NullGameCanvas.NO_GAME)
        return nullGameCanvas
    

    def __init__(self, gameLayerManager: AllBinaryGameLayerManager) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.NullCommandListener import NullCommandListener
        from org.allbinary.game.init.BasicBuildGameInitializerFactory import BasicBuildGameInitializerFactory
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory
        super().__init__(NullCommandListener.NULL_COMMAND_LISTENER, gameLayerManager, NoHighScoresFactory.getInstance(), BasicBuildGameInitializerFactory.NULL_BASE_BUILD_GMAE_INITIALIZER_FACTORY, False)
        __class__._init_fields(self)
        java_super_call(super(), "setWait", 1200)
    

    def isGameOver(self) -> bool:
        with self._lock:
            return __class__.__dict__["_isGameOver_unlocked"].__get__(self, __class__)()

    def _isGameOver_unlocked(self) -> bool:
        return False
    

    def setRunning(self, running: bool) -> None:
        self.runningNull = running
    

    def isRunning(self) -> bool:
        with self._lock:
            return __class__.__dict__["_isRunning_unlocked"].__get__(self, __class__)()

    def _isRunning_unlocked(self) -> bool:
        return self.runningNull
    

    def pause(self) -> None:
        with self._lock:
            return __class__.__dict__["_pause_unlocked"].__get__(self, __class__)()

    def _pause_unlocked(self) -> None:
        self.setPaused(True)
    

    def unPause(self) -> None:
        with self._lock:
            return __class__.__dict__["_unPause_unlocked"].__get__(self, __class__)()

    def _unPause_unlocked(self) -> None:
        self.setPaused(False)
    

    def initCommands(self, cmdListener: CommandListener) -> None:
        from javax.microedition.lcdui.CommandListener import CommandListener
        self.removeAllCommands()
        self.setCommandListener(cmdListener)
    

    # throws Exception
    def buildGameInit(self, isProgress: bool) -> None:
        pass
    

    def draw(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
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
# from org.allbinary.game.init.BasicBuildGameInitializerFactory import BasicBuildGameInitializerFactory
# from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
# from org.allbinary.game.score.NoHighScoresFactory import NoHighScoresFactory
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


def _NullGameCanvas_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(NullGameCanvas, "instance", _NullGameCanvas_instance)

