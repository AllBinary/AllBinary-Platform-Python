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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class GameNotificationEventHandler(BasicEventHandler):
    instance: GameNotificationEventHandler = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("enabled", False)

    def _init_fields(self) -> None:
        self.enabled: bool = True
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def removeAllListeners(self) -> None:
        with self._lock:
            return __class__.__dict__["_removeAllListeners_unlocked"].__get__(self, __class__)()

    def _removeAllListeners_unlocked(self) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        from org.allbinary.logic.util.event.NullEventListener import NullEventListener
        from org.allbinary.util.BasicArrayList import BasicArrayList
        eventListenerInterface: EventListenerInterface = NullEventListener.NULL_EVENT_LISTENER
        list_: BasicArrayList = self.eventListenerInterfaceList
        if list_.size() > 0:
            eventListenerInterface = list_.objectArray[0]
        java_super_call(super(), "removeAllListeners")
        if eventListenerInterface != NullEventListener.NULL_EVENT_LISTENER:
            self.addListenerInterface(eventListenerInterface)
    

    @staticmethod
    def getInstance() -> GameNotificationEventHandler:
        return GameNotificationEventHandler.instance
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        if not (self.enabled):
            return
        gameNotificationListenerInterface: GameNotificationListenerInterface = eventListenerInterface
        gameNotificationListenerInterface.onGameNotificationEvent(eventObject)
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.NullEventListener import NullEventListener
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _GameNotificationEventHandler_instance() -> object:
    return GameNotificationEventHandler()

lazy_static(GameNotificationEventHandler, "instance", _GameNotificationEventHandler_instance)

