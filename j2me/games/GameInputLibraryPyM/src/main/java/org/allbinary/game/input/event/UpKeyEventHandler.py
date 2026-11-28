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
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase


@java_inherited_overloads
class UpKeyEventHandler(UpKeyEventHandlerBase):
    instance: UpKeyEventHandler = None
    instanceArray: list[UpKeyEventHandlerBase] = None
    def _java_defaults(self):
        vars(self).setdefault("playerInputIdFactory", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
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
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def removeAllListeners(self) -> None:
        java_super_call(super(), "removeAllListeners")
        for index in range(len(UpKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpKeyEventHandler.instanceArray[index].removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        java_super_call(super(), "removeListenerSingleThreaded", eventListenerInterface)
        for index in range(len(UpKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpKeyEventHandler.instanceArray[index].removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        java_super_call(super(), "removeListener", eventListenerInterface)
        for index in range(len(UpKeyEventHandler.instanceArray) - 1, 0 - 1, -1):
            UpKeyEventHandler.instanceArray[index].removeListener(eventListenerInterface)
# from org.allbinary.game.input.LocalPlayerInputIdFactory import LocalPlayerInputIdFactory
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


def _UpKeyEventHandler_instance() -> object:
    return UpKeyEventHandler()

lazy_static(UpKeyEventHandler, "instance", _UpKeyEventHandler_instance)

def _UpKeyEventHandler_instanceArray() -> object:
    from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
    from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
    from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
    from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
    from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
    from org.allbinary.game.input.event.UpKeyEventHandlerBase import UpKeyEventHandlerBase
    return [UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase(), UpKeyEventHandlerBase()]

lazy_static(UpKeyEventHandler, "instanceArray", _UpKeyEventHandler_instanceArray)

