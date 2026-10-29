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

import threading
from org.allbinary.game.input.event.GameKeyEventListenerInterface import GameKeyEventListenerInterface
from org.allbinary.game.input.GameInput import GameInput


class PlayerGameInput(GameInput, GameKeyEventListenerInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()
        self.playerInputId: int = None
    

    def __init__(self, gameKeyEventList: BasicArrayList, removalGameKeyEventList: BasicArrayList, playerInputId: int) -> None:
        super().__init__(gameKeyEventList, removalGameKeyEventList)
        self._init_fields()
        self.playerInputId = playerInputId
    

    def onPressGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onPressGameKeyEvent_unlocked(gameKeyEvent)

    def _onPressGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        self.add(gameKeyEvent)
        self.addForRemoval(gameKeyEvent)
    

    def onDownGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onDownGameKeyEvent_unlocked(gameKeyEvent)

    def _onDownGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        self.add(gameKeyEvent)
    

    def onDownKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onDownKeyEvent_unlocked(gameKeyEvent)

    def _onDownKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        self.add(gameKeyEvent)
        self.addForRemoval(gameKeyEvent)
    

    def onDownKey(self, gameKeyEvent: int) -> None:
        with self._lock:
            return self._onDownKey_unlocked(gameKeyEvent)

    def _onDownKey_unlocked(self, gameKeyEvent: int) -> None:
        PreLogUtil.put(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(str(gameKeyEvent))), self, self.gameInputStrings.ON_DOWN_GAME_KEY)
    

    def onUpGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onUpGameKeyEvent_unlocked(gameKeyEvent)

    def _onUpGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        self.addForRemoval(gameKeyEvent)
    

    def onUpKeyEvent(self, gameKeyEvent: int) -> None:
        with self._lock:
            return self._onUpKeyEvent_unlocked(gameKeyEvent)

    def _onUpKeyEvent_unlocked(self, gameKeyEvent: int) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def getPlayerInputId(self) -> int:
        return self.playerInputId
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.input.GameInputStrings import GameInputStrings


