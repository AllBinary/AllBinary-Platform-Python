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
# package org.allbinary.game.layer.hud.event

from __future__ import annotations

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class GameNotificationEventHandler(BasicEventHandler):
    instance: GameNotificationEventHandler = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.enabled: bool = True
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def removeAllListeners(self) -> None:
        with self._lock:
            return self._removeAllListeners_unlocked()

    def _removeAllListeners_unlocked(self) -> None:
        eventListenerInterface: EventListenerInterface = NullEventListener.NULL_EVENT_LISTENER
        list_: BasicArrayList = self.eventListenerInterfaceList
        if list_.size() > 0:
            eventListenerInterface = list_.objectArray[0]
        super().removeAllListeners()
        if eventListenerInterface != NullEventListener.NULL_EVENT_LISTENER:
            self.addListenerInterface(eventListenerInterface)
    

    @staticmethod
    def getInstance() -> GameNotificationEventHandler:
        return GameNotificationEventHandler.instance
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        if not self.enabled:
            return
        gameNotificationListenerInterface: GameNotificationListenerInterface = eventListenerInterface
        gameNotificationListenerInterface.onGameNotificationEvent(eventObject)
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.NullEventListener import NullEventListener
from org.allbinary.util.BasicArrayList import BasicArrayList


GameNotificationEventHandler.instance = GameNotificationEventHandler()

