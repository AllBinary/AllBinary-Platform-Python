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
# package org.allbinary.bounds.event

from __future__ import annotations

from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class BoundsChangeEventHandler(BasicEventHandler):
    SINGLETON: BasicEventHandler = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> BasicEventHandler:
        return BoundsChangeEventHandler.SINGLETON
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        boundsChangeEventListener: BoundsChangeEventListener = eventListenerInterface
        boundsChangeEventListener.onBoundsChangeEvent(eventObject)
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


BoundsChangeEventHandler.SINGLETON = BoundsChangeEventHandler()

