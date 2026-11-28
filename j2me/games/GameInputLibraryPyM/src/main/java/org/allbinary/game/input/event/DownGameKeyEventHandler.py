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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase


@java_inherited_overloads
class DownGameKeyEventHandler(DownGameKeyEventHandlerBase):
    instance: DownGameKeyEventHandler = None
    instanceArray: list[DownGameKeyEventHandlerBase] = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("playerInputIdFactory", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
        self.playerInputIdFactory: LocalPlayerInputIdFactory = LocalPlayerInputIdFactory.getInstance()
    

    @staticmethod
    def getInstance() -> DownGameKeyEventHandler:
        return DownGameKeyEventHandler.instance
    

    def getInstanceForDevice(self, deviceId: int) -> DownGameKeyEventHandlerBase:
        playerInputId: int = self.playerInputIdFactory.getPlayerForDevice(deviceId)
        return DownGameKeyEventHandler.instanceArray[playerInputId]
    

    def getInstanceForPlayer(self, playerInputId: int) -> DownGameKeyEventHandlerBase:
        return DownGameKeyEventHandler.instanceArray[playerInputId]
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def removeAllListeners(self) -> None:
        java_super_call(super(), "removeAllListeners")
        for index in range(len(DownGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownGameKeyEventHandler.instanceArray[index].removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        java_super_call(super(), "removeListenerSingleThreaded", eventListenerInterface)
        for index in range(len(DownGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownGameKeyEventHandler.instanceArray[index].removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return __class__.__dict__["_removeListener_unlocked"].__get__(self, __class__)(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        java_super_call(super(), "removeListener", eventListenerInterface)
        for index in range(len(DownGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownGameKeyEventHandler.instanceArray[index].removeListener(eventListenerInterface)
# from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


def _DownGameKeyEventHandler_instance() -> object:
    return DownGameKeyEventHandler()

lazy_static(DownGameKeyEventHandler, "instance", _DownGameKeyEventHandler_instance)

def _DownGameKeyEventHandler_instanceArray() -> object:
    from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
    from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
    from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
    from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
    from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
    from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
    return [DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase()]

lazy_static(DownGameKeyEventHandler, "instanceArray", _DownGameKeyEventHandler_instanceArray)

