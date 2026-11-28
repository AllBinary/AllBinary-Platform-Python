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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput


@java_inherited_overloads
class HighScoresCanvasInputProcessor(PlayerGameInput):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("highScoresCanvas", None)

    def _init_fields(self) -> None:
        if "highScoresCanvas" not in vars(self): self.highScoresCanvas: HighScoresCanvas = None
    

    def __init__(self, highScoresCanvas: HighScoresCanvas) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        super().__init__(BasicArrayListD(), BasicArrayListD(), -1)
        __class__._init_fields(self)
        self.highScoresCanvas = highScoresCanvas
    

    def open(self) -> None:
        pass
    

    def close(self) -> None:
        pass
    

    def onPressGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onPressGameKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onPressGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        java_super_call(super(), "onPressGameKeyEvent", gameKeyEvent)
        self.update()
    

    def onDownGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onDownGameKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onDownGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        java_super_call(super(), "onDownGameKeyEvent", gameKeyEvent)
        self.update()
    

    def onUpGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onUpGameKeyEvent_unlocked"].__get__(self, __class__)(gameKeyEvent)

    def _onUpGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        java_super_call(super(), "onUpGameKeyEvent", gameKeyEvent)
        self.update()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def getHighScoresCanvas(self) -> HighScoresCanvas:
        from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
        return self.highScoresCanvas
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.game.score.displayable.HighScoresCanvas import HighScoresCanvas
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


