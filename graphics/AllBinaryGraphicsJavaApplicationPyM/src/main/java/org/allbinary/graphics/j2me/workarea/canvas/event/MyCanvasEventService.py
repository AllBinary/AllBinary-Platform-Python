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
# package org.allbinary.graphics.j2me.workarea.canvas.event

from __future__ import annotations

import threading
from org.allbinary.graphics.j2me.workarea.canvas.event.EventListenerList import EventListenerList


class MyCanvasEventService:
    listenerList: EventListenerList = EventListenerList()
    DELETE: str = "delete"
    DUPLICATE: str = "duplicate"
    SELECT: str = "select"
    ROTATE: str = "rotate"
    EXPLODE: str = "explode"
    AUTOEXPLODE: str = "autoExplode"
    CENTER: str = "center"
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def addListener(listener: MyCanvasEventListener) -> None:
        with MyCanvasEventService._lock:
            return MyCanvasEventService._addListener_unlocked(listener)

    @staticmethod
    def _addListener_unlocked(listener: MyCanvasEventListener) -> None:
        MyCanvasEventService.listenerList.add(type(listener), listener)
    

    @staticmethod
    def removeListener(listener: MyCanvasEventListener) -> None:
        with MyCanvasEventService._lock:
            return MyCanvasEventService._removeListener_unlocked(listener)

    @staticmethod
    def _removeListener_unlocked(listener: MyCanvasEventListener) -> None:
        MyCanvasEventService.listenerList.remove(type(listener), listener)
    

    # throws Exception
    @staticmethod
    def fire(evt: MyCanvasEvent) -> None:
        with MyCanvasEventService._lock:
            return MyCanvasEventService._fire_unlocked(evt)

    @staticmethod
    def _fire_unlocked(evt: MyCanvasEvent) -> None:
        listeners: list[object] = MyCanvasEventService.listenerList.getListenerList()
        for i in range(0, len(listeners), 2):
            if listeners[i] == type(listeners[i + 1]):
                if evt.getCommand().compareTo(MyCanvasEventService.DELETE) == 0:
                    (listeners[i + 1]).delete(evt)
                elif evt.getCommand().compareTo(MyCanvasEventService.DUPLICATE) == 0:
                    (listeners[i + 1]).duplicate(evt)
                elif evt.getCommand().compareTo(MyCanvasEventService.SELECT) == 0:
                    (listeners[i + 1]).select(evt)
                elif evt.getCommand().compareTo(MyCanvasEventService.ROTATE) == 0:
                    (listeners[i + 1]).rotate(evt)
                elif evt.getCommand().compareTo(MyCanvasEventService.EXPLODE) == 0:
                    (listeners[i + 1]).explode(evt)
                elif evt.getCommand().compareTo(MyCanvasEventService.AUTOEXPLODE) == 0:
                    (listeners[i + 1]).autoExplode(evt)
                elif evt.getCommand().compareTo(MyCanvasEventService.CENTER) == 0:
                    (listeners[i + 1]).center(evt)


