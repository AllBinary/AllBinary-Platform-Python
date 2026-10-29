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

import threading
from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase
from org.allbinary.game.input.event.DownGameKeyEventHandlerBase import DownGameKeyEventHandlerBase


class DownGameKeyEventHandler(DownGameKeyEventHandlerBase):
    instance: DownGameKeyEventHandler = None
    instanceArray: list[DownGameKeyEventHandlerBase] = [DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase(), DownGameKeyEventHandlerBase()]
    _lock = threading.RLock()

    def _init_fields(self) -> None:
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
        super().__init__()
        self._init_fields()
    

    def removeAllListeners(self) -> None:
        super().removeAllListeners()
        for index in range(len(DownGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownGameKeyEventHandler.instanceArray[index].removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        super().removeListenerSingleThreaded(eventListenerInterface)
        for index in range(len(DownGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownGameKeyEventHandler.instanceArray[index].removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return self._removeListener_unlocked(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        super().removeListener(eventListenerInterface)
        for index in range(len(DownGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownGameKeyEventHandler.instanceArray[index].removeListener(eventListenerInterface)
from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


DownGameKeyEventHandler.instance = DownGameKeyEventHandler()

