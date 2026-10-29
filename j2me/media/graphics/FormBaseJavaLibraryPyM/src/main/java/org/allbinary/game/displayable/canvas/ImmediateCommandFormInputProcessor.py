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
from org.allbinary.game.displayable.canvas.CommandFormInputProcessor import CommandFormInputProcessor


class ImmediateCommandFormInputProcessor(CommandFormInputProcessor):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.timeHelper: TimeDelayHelper = TimeDelayHelper(25)
        self.gameCommandCanvas: GameCommandCanvas = None
    

    def __init__(self, gameKeyEventList: BasicArrayList, playerInputId: int, gameCommandCanvas: GameCommandCanvas, form: ScrollSelectionForm) -> None:
        super().__init__(gameKeyEventList, playerInputId, gameCommandCanvas, form)
        self._init_fields()
        self.gameCommandCanvas = gameCommandCanvas
    

    def onPressGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onPressGameKeyEvent_unlocked(gameKeyEvent)

    def _onPressGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        try:
            super().onPressGameKeyEvent(gameKeyEvent)
            if self.timeHelper.isTimeTNT():
                self.processInputList()
                self.gameCommandCanvas.repaintBehavior.onChangeRepaint(self.getCanvas())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.ON_PRESS_GAME_KEY, e)
    

    def onDownGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onDownGameKeyEvent_unlocked(gameKeyEvent)

    def _onDownGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        try:
            super().onDownGameKeyEvent(gameKeyEvent)
            if self.timeHelper.isTimeTNT():
                self.processInputList()
                self.gameCommandCanvas.repaintBehavior.onChangeRepaint(self.getCanvas())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.ON_DOWN_GAME_KEY, e)
    

    def onUpGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        with self._lock:
            return self._onUpGameKeyEvent_unlocked(gameKeyEvent)

    def _onUpGameKeyEvent_unlocked(self, gameKeyEvent: GameKeyEvent) -> None:
        try:
            super().onUpGameKeyEvent(gameKeyEvent)
            if self.timeHelper.isTimeTNT():
                self.processInputList()
                self.gameCommandCanvas.repaintBehavior.onChangeRepaint(self.getCanvas())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.ON_UP_GAME_KEY, e)
    

    def onMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        try:
            super().onMotionGestureEvent(motionGestureEvent)
            if self.timeHelper.isTimeTNT():
                self.processInputList()
                self.gameCommandCanvas.repaintBehavior.onChangeRepaint(self.getCanvas())
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onMotionGestureEvent", e)
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList


