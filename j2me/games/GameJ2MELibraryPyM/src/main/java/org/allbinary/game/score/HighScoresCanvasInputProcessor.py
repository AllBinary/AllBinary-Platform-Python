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
# package org.allbinary.game.score

from __future__ import annotations

import threading
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput


class HighScoresCanvasInputProcessor(PlayerGameInput):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.highScoresCanvas: HighScoresCanvas = None
    

    def __init__(self, highScoresCanvas: HighScoresCanvas) -> None:
        super().__init__(BasicArrayListD(), BasicArrayListD(), -1)
        self._init_fields()
        self.highScoresCanvas = highScoresCanvas
    

    def open(self) -> None:
        pass
    

    def close(self) -> None:
        pass
    

    def onPressGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onPressGameKeyEvent_unlocked(gameKeyEvent)

    def _onPressGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        super().onPressGameKeyEvent(gameKeyEvent)
        self.update()
    

    def onDownGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onDownGameKeyEvent_unlocked(gameKeyEvent)

    def _onDownGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        super().onDownGameKeyEvent(gameKeyEvent)
        self.update()
    

    def onUpGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onUpGameKeyEvent_unlocked(gameKeyEvent)

    def _onUpGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        super().onUpGameKeyEvent(gameKeyEvent)
        self.update()
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def getHighScoresCanvas(self) -> HighScoresCanvas:
        return self.highScoresCanvas
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


