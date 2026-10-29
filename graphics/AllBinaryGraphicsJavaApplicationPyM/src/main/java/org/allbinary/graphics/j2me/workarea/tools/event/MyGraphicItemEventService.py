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
# package org.allbinary.graphics.j2me.workarea.tools.event

from __future__ import annotations

import threading
from org.allbinary.graphics.j2me.workarea.tools.event.EventListenerList import EventListenerList


class MyGraphicItemEventService:
    listenerList: EventListenerList = EventListenerList()
    DELETE: str = "delete"
    DESELECT: str = "deselect"
    SELECT: str = "select"
    DUPLICATE: str = "duplicate"
    ROTATE: str = "rotate"
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def addListener(listener: MyGraphicItemEventListener) -> None:
        with MyGraphicItemEventService._lock:
            return MyGraphicItemEventService._addListener_unlocked(listener)

    @staticmethod
    def _addListener_unlocked(listener: MyGraphicItemEventListener) -> None:
        MyGraphicItemEventService.listenerList.add(type(listener), listener)
    

    @staticmethod
    def removeListener(listener: MyGraphicItemEventListener) -> None:
        with MyGraphicItemEventService._lock:
            return MyGraphicItemEventService._removeListener_unlocked(listener)

    @staticmethod
    def _removeListener_unlocked(listener: MyGraphicItemEventListener) -> None:
        MyGraphicItemEventService.listenerList.remove(type(listener), listener)
    

    # throws Exception
    @staticmethod
    def fire(evt: MyGraphicItemEvent) -> None:
        with MyGraphicItemEventService._lock:
            return MyGraphicItemEventService._fire_unlocked(evt)

    @staticmethod
    def _fire_unlocked(evt: MyGraphicItemEvent) -> None:
        listeners: list[object] = MyGraphicItemEventService.listenerList.getListenerList()
        for i in range(0, len(listeners), 2):
            if listeners[i] == type(listeners[i + 1]):
                if evt.getCommand().compareTo(MyGraphicItemEventService.SELECT) == 0:
                    (listeners[i + 1]).highlight(evt)
                elif evt.getCommand().compareTo(MyGraphicItemEventService.DESELECT) == 0:
                    (listeners[i + 1]).deselect(evt)
                elif evt.getCommand().compareTo(MyGraphicItemEventService.DELETE) == 0:
                    (listeners[i + 1]).delete(evt)
                elif evt.getCommand().compareTo(MyGraphicItemEventService.DUPLICATE) == 0:
                    (listeners[i + 1]).duplicate(evt)
                elif evt.getCommand().compareTo(MyGraphicItemEventService.ROTATE) == 0:
                    (listeners[i + 1]).rotate(evt)


