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
# package org.allbinary.game.input.motion.action

from __future__ import annotations

from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface


class GameKeyCompleteMotionGestureInputEvent(CompleteMotionGestureInputEvent, GameKeyEventSourceInterface):

    def _init_fields(self) -> None:
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.SOURCE_ID: int = self.gameKeyEventFactory.MOTION_GESTURE_SOURCE_ID
        self.gameKey: GameKey = GameKey.NULL_GAME_KEY
        self.gameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
        self.inputToGameKeyMapping: InputToGameKeyMapping = None
    

    def __init__(self, name: str, motionGestureInput: MotionGestureInput, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        from org.allbinary.game.input.motion.action.GameKeyCompleteMotionGestureInputEventFactory import GameKeyCompleteMotionGestureInputEventFactory
        super().__init__(name, motionGestureInput)
        self._init_fields()
        self.inputToGameKeyMapping = inputToGameKeyMapping
        GameKeyCompleteMotionGestureInputEventFactory.getInstance().add(self)
        self.update()
    

    def getSourceId(self) -> int:
        return self.SOURCE_ID
    

    def update(self) -> None:
        try:
            self.setGameKey(self.inputToGameKeyMapping.getInstance(self.getMotionGestureInput().getId()))
            self.setGameKeyEvent(self.gameKeyEventFactory.getInstanceForInput(self, self.getGameKey()))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.UPDATE, e)
    

    def setGameKeyEvent(self, gameKeyEvent: GameKeyEvent) -> None:
        self.gameKeyEvent = gameKeyEvent
    

    def getGameKeyEvent(self) -> GameKeyEvent:
        return self.gameKeyEvent
    

    def setGameKey(self, gameKey: GameKey) -> None:
        self.gameKey = gameKey
    

    def getGameKey(self) -> GameKey:
        return self.gameKey
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.string.CommonStrings import CommonStrings


