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

from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase


class UpKeyEventHandler(UpKeyEventHandlerBase):
    instance: UpKeyEventHandler = None
    instanceArray: list[UpKeyEventHandlerBase] = [UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase()]

    def _init_fields(self) -> None:
        self.playerInputIdFactory: LocalPlayerInputIdFactory = LocalPlayerInputIdFactory.getInstance()
    

    @staticmethod
    def getInstance() -> UpKeyEventHandler:
        return UpKeyEventHandler.instance
    

    def getInstanceForDevice(self, deviceId: int) -> UpKeyEventHandlerBase:
        playerInputId: int = self.playerInputIdFactory.getPlayerForDevice(deviceId)
        return UpKeyEventHandler.instanceArray[playerInputId]
    

    def getInstanceForPlayer(self, playerInputId: int) -> UpKeyEventHandlerBase:
        return UpKeyEventHandler.instanceArray[playerInputId]
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def removeAllListeners(self) -> None:
        super().removeAllListeners()
        for index in range(len(UpKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpKeyEventHandler.instanceArray[index].removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        super().removeListenerSingleThreaded(eventListenerInterface)
        for index in range(len(UpKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpKeyEventHandler.instanceArray[index].removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        super().removeListener(eventListenerInterface)
        for index in range(len(UpKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpKeyEventHandler.instanceArray[index].removeListener(eventListenerInterface)
from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


UpKeyEventHandler.instance = UpKeyEventHandler()

