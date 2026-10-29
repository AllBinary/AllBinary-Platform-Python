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

from org.allbinary.canvas.Processor import Processor
from org.allbinary.game.input.GameInputProcessorInterface import GameInputProcessorInterface
from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface


class PreGameSelectionGameInputProcessor(Processor, GameInputProcessorInterface, PlayerGameInputCompositeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameCanvas: AllBinaryGameCanvas = None
        self.preGameSelectorPaintable: PreGameSelectorPaintable = None
        self.inputTimeHelper: TimeDelayHelper = TimeDelayHelper(650)
        self.nextGameState: GameState = None
        self.playerGameInput: PlayerGameInput = None
        self.lockedIndex: int = None
        self.abRunnable: ABRunnable = (ABRunnable()  # Java anonymous class body:
#         
# 
#         def run(self) -> None:
#             try:
#                 self.setRunning(True)
#                 SecondaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
#                 self.gameCanvas.setGameState(self.nextGameState)
#                 GameKeyEventHandler.getInstance().removeListener(self.getPlayerGameInput())
#                 self.setRunning(False)
#             except Exception as e:
#                 self.setRunning(False)
#                 logUtil: LogUtil = LogUtil.getInstance()
#                 commonStrings: CommonStrings = CommonStrings.getInstance()
#                 logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
)
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas, preGameSelectorPaintable: PreGameSelectorPaintable, nextGameState: GameState, lockedIndex: int) -> None:
        from org.allbinary.game.input.GameInputProcessorComposite import GameInputProcessorComposite
        super().__init__()
        self._init_fields()
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
        size: int = list_.size()
        for index in range(0, size):
            anyType: object = list_.get(index)
            key: int = GameKeyEventUtil.getKey(anyType)
            if key == Canvas.LEFT or key == Canvas.RIGHT or key == Canvas.UP or key == Canvas.DOWN:
                if self.inputTimeHelper.isTimeTNT():
                    SecondaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
                    self.getPreGameSelectorPaintable().getPreGameSelectionForm().processInputKey(key)
                    break
            elif key == Canvas.KEY_NUM0:
                selectedIndex: int = self.preGameSelectorPaintable.getPreGameSelectionForm().getSelectedIndex()
                if selectedIndex < self.lockedIndex or not LockedUtil.getInstance().isLocked():
                    if not self.abRunnable.isRunning():
                        self.abRunnable.setRunning(True)
                        ThreadObjectUtil.getInstance().processThread(self.abRunnable)
                    break
                else:
                    LockedFeatureNotificationUtil.getInstance().fire()
        list_.clear()
    

    def getPreGameSelectorPaintable(self) -> PreGameSelectorPaintable:
        return self.preGameSelectorPaintable
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        pass
    

    def initInputProcessors(self) -> None:
        pass
    

    def getName(self) -> str:
        return str(self)
    

    def getPlayerGameInput(self) -> PlayerGameInput:
        return self.playerGameInput
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.system.security.licensing.LockedFeatureNotificationUtil import LockedFeatureNotificationUtil
from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.displayable.canvas.PreGameSelectorPaintable import PreGameSelectorPaintable
from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
from org.allbinary.game.input.event.GameKeyEventUtil import GameKeyEventUtil
from org.allbinary.game.state.GameState import GameState
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.media.audio.SelectSound import SelectSound
from org.allbinary.thread.ABRunnable import ABRunnable
from org.allbinary.thread.ThreadObjectUtil import ThreadObjectUtil
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


