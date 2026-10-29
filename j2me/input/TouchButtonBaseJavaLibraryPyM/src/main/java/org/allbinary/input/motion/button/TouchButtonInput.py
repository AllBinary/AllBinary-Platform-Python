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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
from org.allbinary.game.input.Input import Input


class TouchButtonInput(Input, GameKeyEventSourceInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.TOUCH_BUTTON_SOURCE_ID: int = self.gameKeyEventFactory.TOUCH_BUTTON_SOURCE_ID
        self.gameKeyEvent: GameKeyEvent = GameKeyEvent.NONE
    

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)
        self._init_fields()
        inputFactory: InputFactory = InputFactory.getInstance()
        inputFactory.add(self.getId(), self)
    

    def update(self, inputToGameKeyMapping: InputToGameKeyMapping) -> None:
        try:
            gameKey: GameKey = inputToGameKeyMapping.getInstance(self.getId())
            self.gameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self, gameKey)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.UPDATE, e)
    

    def getSourceId(self) -> int:
        return self.TOUCH_BUTTON_SOURCE_ID
    

    def getGameKeyEvent(self) -> GameKeyEvent:
        return self.gameKeyEvent
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


