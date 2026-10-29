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
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput


class NoPlayerGameInput(PlayerGameInput):
    SINGLETON: NoPlayerGameInput = None
    _lock = threading.RLock()
    

    @staticmethod
    def getInstance() -> NoPlayerGameInput:
        return NoPlayerGameInput.SINGLETON
    

    def __init__(self) -> None:
        super().__init__(BasicArrayListD(), BasicArrayListD(), -1)
    

    def onDownGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onDownGameKeyEvent_unlocked(gameKeyEvent)

    def _onDownGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    def onUpGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onUpGameKeyEvent_unlocked(gameKeyEvent)

    def _onUpGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        pass
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.util.BasicArrayListD import BasicArrayListD


NoPlayerGameInput.SINGLETON = NoPlayerGameInput()

