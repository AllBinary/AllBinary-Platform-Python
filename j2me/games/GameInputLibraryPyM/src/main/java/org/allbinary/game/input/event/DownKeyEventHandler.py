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
from org.allbinary.game.input.event.DownKeyEventHandlerBase import DownKeyEventHandlerBase
from org.allbinary.game.input.event.DownKeyEventHandlerBase import DownKeyEventHandlerBase


class DownKeyEventHandler(DownKeyEventHandlerBase):
    instance: DownKeyEventHandler = None
    instanceArray: list[DownKeyEventHandlerBase] = [DownKeyEventHandlerBase(), DownKeyEventHandlerBase(), DownKeyEventHandlerBase(), DownKeyEventHandlerBase(), DownKeyEventHandlerBase(), DownKeyEventHandlerBase()]
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.playerInputIdFactory: LocalPlayerInputIdFactory = LocalPlayerInputIdFactory.getInstance()
    

    @staticmethod
    def getInstance() -> DownKeyEventHandler:
        return DownKeyEventHandler.instance
    

    def getInstanceForDevice(self, deviceId: int) -> DownKeyEventHandlerBase:
        playerInputId: int = self.playerInputIdFactory.getPlayerForDevice(deviceId)
        return DownKeyEventHandler.instanceArray[playerInputId]
    

    def getInstanceForPlayer(self, playerInputId: int) -> DownKeyEventHandlerBase:
        return DownKeyEventHandler.instanceArray[playerInputId]
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def removeAllListeners(self) -> None:
        super().removeAllListeners()
        for index in range(len(DownKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownKeyEventHandler.instanceArray[index].removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        super().removeListenerSingleThreaded(eventListenerInterface)
        for index in range(len(DownKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownKeyEventHandler.instanceArray[index].removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return self._removeListener_unlocked(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        super().removeListener(eventListenerInterface)
        for index in range(len(DownKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            DownKeyEventHandler.instanceArray[index].removeListener(eventListenerInterface)
from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


DownKeyEventHandler.instance = DownKeyEventHandler()

