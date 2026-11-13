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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase


class UpGameKeyEventHandler(UpGameKeyEventHandlerBase):
    instance: UpGameKeyEventHandler = None
    instanceArray: list[UpGameKeyEventHandlerBase] = None

    def _init_fields(self) -> None:
        from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
        self.playerInputIdFactory: LocalPlayerInputIdFactory = LocalPlayerInputIdFactory.getInstance()
    

    @staticmethod
    def getInstance() -> UpGameKeyEventHandler:
        return UpGameKeyEventHandler.instance
    

    def getInstanceForDevice(self, deviceId: int) -> UpGameKeyEventHandlerBase:
        playerInputId: int = self.playerInputIdFactory.getPlayerForDevice(deviceId)
        return UpGameKeyEventHandler.instanceArray[playerInputId]
    

    def getInstanceForPlayer(self, playerInputId: int) -> UpGameKeyEventHandlerBase:
        return UpGameKeyEventHandler.instanceArray[playerInputId]
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def removeAllListeners(self) -> None:
        super().removeAllListeners()
        for index in range(len(UpGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpGameKeyEventHandler.instanceArray[index].removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        super().removeListenerSingleThreaded(eventListenerInterface)
        for index in range(len(UpGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpGameKeyEventHandler.instanceArray[index].removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        super().removeListener(eventListenerInterface)
        for index in range(len(UpGameKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpGameKeyEventHandler.instanceArray[index].removeListener(eventListenerInterface)
# from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


def _UpGameKeyEventHandler_instance() -> object:
    return UpGameKeyEventHandler()

lazy_static(UpGameKeyEventHandler, "instance", _UpGameKeyEventHandler_instance)

def _UpGameKeyEventHandler_instanceArray() -> object:
    from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase
    from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase
    from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase
    from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase
    from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase
    from org.allbinary.game.input.event.UpGameKeyEventHandlerBase import UpGameKeyEventHandlerBase
    return [UpGameKeyEventHandlerBase(), UpGameKeyEventHandlerBase(), UpGameKeyEventHandlerBase(), UpGameKeyEventHandlerBase(), UpGameKeyEventHandlerBase(), UpGameKeyEventHandlerBase()]

lazy_static(UpGameKeyEventHandler, "instanceArray", _UpGameKeyEventHandler_instanceArray)

