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
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.canvas.Processor import Processor
from org.allbinary.thread.ABRunnable import ABRunnable
from org.allbinary.game.input.GameInputProcessorInterface import GameInputProcessorInterface
from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface


@java_inherited_overloads
class PreGameSelectionGameInputProcessor(*java_bases(Processor, GameInputProcessorInterface, PlayerGameInputCompositeInterface)):
    @java_inherited_overloads
    class PreGameSelectionRunnable(ABRunnable):
        def _java_defaults(self):
            vars(self).setdefault("inputProcessor", None)

        def _init_fields(self) -> None:
            if "inputProcessor" not in vars(self): self.inputProcessor: PreGameSelectionGameInputProcessor = None
        

        def __init__(self, inputProcessor: PreGameSelectionGameInputProcessor) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.inputProcessor = inputProcessor
        

        def run(self) -> None:
            from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
            from org.allbinary.media.audio.SelectSound import SelectSound
            try:
                self.setRunning(True)
                SecondaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
                self.inputProcessor.gameCanvas.setGameState(self.inputProcessor.nextGameState)
                GameKeyEventHandler.getInstance().removeListener(self.inputProcessor.getPlayerGameInput())
                self.setRunning(False)
            except Exception as e:
                self.setRunning(False)
                logUtil: LogUtil = LogUtil.getInstance()
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("gameCanvas", None)
        vars(self).setdefault("preGameSelectorPaintable", None)
        vars(self).setdefault("inputTimeHelper", None)
        vars(self).setdefault("nextGameState", None)
        vars(self).setdefault("playerGameInput", None)
        vars(self).setdefault("lockedIndex", 0)
        vars(self).setdefault("abRunnable", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "gameCanvas" not in vars(self): self.gameCanvas: AllBinaryGameCanvas = None
        if "preGameSelectorPaintable" not in vars(self): self.preGameSelectorPaintable: PreGameSelectorPaintable = None
        self.inputTimeHelper: TimeDelayHelper = TimeDelayHelper(650)
        if "nextGameState" not in vars(self): self.nextGameState: GameState = None
        if "playerGameInput" not in vars(self): self.playerGameInput: PlayerGameInput = None
        if "lockedIndex" not in vars(self): self.lockedIndex: int = 0
        self.abRunnable: ABRunnable = java_new_inner(self, PreGameSelectionRunnable, self)
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas, preGameSelectorPaintable: PreGameSelectorPaintable, nextGameState: GameState, lockedIndex: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.GameInputProcessorComposite import GameInputProcessorComposite
        from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
        from org.allbinary.game.displayable.canvas.PreGameSelectorPaintable import PreGameSelectorPaintable
        from org.allbinary.game.state.GameState import GameState
        super().__init__()
        __class__._init_fields(self)
        self.gameCanvas = gameCanvas
        self.preGameSelectorPaintable = preGameSelectorPaintable
        self.nextGameState = nextGameState
        self.playerGameInput = GameInputProcessorComposite("Pre Game Selection", self)
        self.lockedIndex = lockedIndex
    

    # throws Exception
    def process(self) -> None:
        self.getPlayerGameInput().update()
    

    # throws Exception
    def onInput(self, list_: BasicArrayList) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.system.security.licensing.LockedFeatureNotificationUtil import LockedFeatureNotificationUtil
        from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
        from org.allbinary.game.input.event.GameKeyEventUtil import GameKeyEventUtil
        from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
        from org.allbinary.media.audio.SelectSound import SelectSound
        from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil
        size: int = list_.size()
        for index in range(0, size):
            anyType: object = list_.get(index)
            key: int = GameKeyEventUtil.getKey(anyType)
            if key == Canvas.LEFT or key == Canvas.RIGHT or key == Canvas.UP or key == Canvas.DOWN:
                if java_predicate(self.inputTimeHelper, "isTimeTNT"):
                    SecondaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
                    self.getPreGameSelectorPaintable().getPreGameSelectionForm().processInputKey(key)
                    break
            elif key == Canvas.KEY_NUM0:
                selectedIndex: int = self.preGameSelectorPaintable.getPreGameSelectionForm().getSelectedIndex()
                if selectedIndex < self.lockedIndex or not (java_predicate(LockedUtil.getInstance(), "isLocked")):
                    if not (java_predicate(self.abRunnable, "isRunning")):
                        self.abRunnable.setRunning(True)
                        ThreadObjectUtil.getInstance().processThread(self.abRunnable)
                    break
                else:
                    LockedFeatureNotificationUtil.getInstance().fire()
        list_.clear()
    

    def getPreGameSelectorPaintable(self) -> PreGameSelectorPaintable:
        from org.allbinary.game.displayable.canvas.PreGameSelectorPaintable import PreGameSelectorPaintable
        return self.preGameSelectorPaintable
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    def initInputProcessors(self) -> None:
        pass
    

    def getName(self) -> str:
        return str(self)
    

    def getPlayerGameInput(self) -> PlayerGameInput:
        return self.playerGameInput
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.logic.system.security.licensing.LockedFeatureNotificationUtil import LockedFeatureNotificationUtil
# from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
# from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
# from org.allbinary.game.displayable.canvas.PreGameSelectorPaintable import PreGameSelectorPaintable
# from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
# from org.allbinary.game.input.event.GameKeyEventUtil import GameKeyEventUtil
# from org.allbinary.game.state.GameState import GameState
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
# from org.allbinary.media.audio.SelectSound import SelectSound
# from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


