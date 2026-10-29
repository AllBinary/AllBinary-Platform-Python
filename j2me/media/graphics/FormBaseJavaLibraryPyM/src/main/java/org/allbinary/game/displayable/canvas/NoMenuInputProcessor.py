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
from org.allbinary.game.displayable.canvas.BasicMenuInputProcessor import BasicMenuInputProcessor


class NoMenuInputProcessor(BasicMenuInputProcessor):
    SINGLETON: NoMenuInputProcessor = None
    _lock = threading.RLock()
    

    @staticmethod
    def getInstance() -> NoMenuInputProcessor:
        return NoMenuInputProcessor.SINGLETON
    

    def __init__(self) -> None:
        super().__init__(BasicArrayListUtil.getInstance().getImmutableInstance(), -1, NullCanvas.NULL_CANVAS)
    

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
    

    def onMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        pass
# from javax.microedition.lcdui.NullCanvas import NullCanvas
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


NoMenuInputProcessor.SINGLETON = NoMenuInputProcessor()

