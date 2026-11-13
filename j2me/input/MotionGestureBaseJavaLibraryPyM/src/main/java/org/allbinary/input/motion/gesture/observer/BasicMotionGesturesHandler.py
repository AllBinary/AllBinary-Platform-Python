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
# package org.allbinary.input.motion.gesture.observer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class BasicMotionGesturesHandler(BasicEventHandler):
    SINGLETON: BasicMotionGesturesHandler = None
    

    @staticmethod
    def getInstance() -> BasicMotionGesturesHandler:
        return BasicMotionGesturesHandler.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        baseMotionGestureEventListener: BaseMotionGestureEventListener = eventListenerInterface
        baseMotionGestureEventListener.onMotionGestureEvent(eventObject)
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


def _BasicMotionGesturesHandler_SINGLETON() -> object:
    return BasicMotionGesturesHandler()

lazy_static(BasicMotionGesturesHandler, "SINGLETON", _BasicMotionGesturesHandler_SINGLETON)

