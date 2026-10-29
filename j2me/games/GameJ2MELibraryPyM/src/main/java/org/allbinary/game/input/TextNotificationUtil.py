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



class TextNotificationUtil:
    instance: TextNotificationUtil = None

    def _init_fields(self) -> None:
        self.TWO: int = SmallIntegerSingletonFactory.getInstance().getAt(2)
        self.FALSE: bool = BooleanFactory.getInstance().FALSE
        self.gameNotificationEventHandler: GameNotificationEventHandler = GameNotificationEventHandler.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TextNotificationUtil:
        return TextNotificationUtil.instance
    

    # throws Exception
    def fireError(self, message: str) -> None:
        PrimaryPlayerQueueFactory.getInstance().add(ErrorSound.getInstance())
        self.fire(message)
    

    # throws Exception
    def fireNew(self, message: str) -> None:
        PrimaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
        self.fire(message)
    

    # throws Exception
    def fireSuccess(self, message: str) -> None:
        PrimaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
        self.fire(message)
    

    # throws Exception
    def fire(self, message: str) -> None:
        gameNotificationEvent: GameNotificationEvent = GameNotificationEvent(self, message, self.TWO, BasicColorFactory.getInstance().RED, self.FALSE)
        self.gameNotificationEventHandler.fireEvent(gameNotificationEvent)
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.audio.PrimaryPlayerQueueFactory import PrimaryPlayerQueueFactory
from org.allbinary.media.audio.SelectSound import SelectSound


TextNotificationUtil.instance = TextNotificationUtil()

