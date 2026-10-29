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
# package org.allbinary.game.input.event

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class GameKeyEventFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.TOUCH_BUTTON_SOURCE_ID: int = 2
        self.MOTION_GESTURE_SOURCE_ID: int = 3
        self.MAX_SOURCES: int = 4
        self.ARRAY: list[list[GameKeyEvent]] = [[None] * (InputFactory.getInstance().MAX) for _ in range(self.MAX_SOURCES)]
    

    @staticmethod
    def getInstance() -> GameKeyEventFactory:
        if GameKeyEventFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            GameKeyEventFactory.instance = GameKeyEventFactory()
        return GameKeyEventFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        nullUtil: NullUtil = NullUtil.getInstance()
        size: int = InputFactory.getInstance().MAX
        index = self.MAX_SOURCES
        while (index := index - 1) >= 0:
            index2 = size
            while (index2 := index2 - 1) >= 0:
                self.ARRAY[index][index2] = GameKeyEvent.createEvent(nullUtil.NULL_OBJECT, index, index2)
    

    # throws Exception
    def getInstanceForKey(self, anyType: GameKeyEventSourceInterface, key: int) -> GameKeyEvent:
        gameKeyEvent: GameKeyEvent = self.ARRAY[anyType.getSourceId()][key]
        return gameKeyEvent
    

    # throws Exception
    def getInstanceForInput(self, anyType: GameKeyEventSourceInterface, input: Input) -> GameKeyEvent:
        gameKeyEvent: GameKeyEvent = self.ARRAY[anyType.getSourceId()][input.getId()]
        return gameKeyEvent
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil


