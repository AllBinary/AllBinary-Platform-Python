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


class ScrolledMotionGesturesHandler(BasicEventHandler):
    SINGLETON: ScrolledMotionGesturesHandler = None
    

    @staticmethod
    def getInstance() -> ScrolledMotionGesturesHandler:
        return ScrolledMotionGesturesHandler.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        baseMotionGestureEventListener: BaseMotionGestureEventListener = eventListenerInterface
        baseMotionGestureEventListener.onScrolledMotionGestureEvent(eventObject)
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


def _ScrolledMotionGesturesHandler_SINGLETON() -> object:
    return ScrolledMotionGesturesHandler()

lazy_static(ScrolledMotionGesturesHandler, "SINGLETON", _ScrolledMotionGesturesHandler_SINGLETON)

