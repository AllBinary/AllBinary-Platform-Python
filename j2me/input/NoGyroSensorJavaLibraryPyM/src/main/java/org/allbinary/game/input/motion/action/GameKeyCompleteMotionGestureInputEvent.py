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
        self.gameKey: GameKey = GameKey.NULL_GAME_KEY
        self.gameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
    

    def __init__(self, name: str, motionGestureInput: MotionGestureInput, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        super().__init__(name, motionGestureInput)
        self._init_fields()
    

    def getSourceId(self) -> int:
        return 0
    

    def update(self) -> None:
        pass
    

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
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput


