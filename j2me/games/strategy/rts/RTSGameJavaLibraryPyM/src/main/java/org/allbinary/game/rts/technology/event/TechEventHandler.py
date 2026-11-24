# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.rts.technology.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class TechEventHandler(BasicEventHandler):
    eventHandler: TechEventHandler = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> TechEventHandler:
        return TechEventHandler.eventHandler
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        techEventListenerInterface: TechEventListenerInterface = (eventListenerInterface)
        techEventListenerInterface.onTechEvent(eventObject)
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


def _TechEventHandler_eventHandler() -> object:
    return TechEventHandler()

lazy_static(TechEventHandler, "eventHandler", _TechEventHandler_eventHandler)

