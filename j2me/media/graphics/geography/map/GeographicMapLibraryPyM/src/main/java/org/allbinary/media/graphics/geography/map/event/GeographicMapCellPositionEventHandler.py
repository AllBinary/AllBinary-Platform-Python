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
# package org.allbinary.media.graphics.geography.map.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class GeographicMapCellPositionEventHandler(BasicEventHandler):
    instance: GeographicMapCellPositionEventHandler = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("list_", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> GeographicMapCellPositionEventHandler:
        return GeographicMapCellPositionEventHandler.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, miniMapLayer: MiniMapLayer) -> None:
        from org.allbinary.game.layer.geographic.map.MiniMapLayer import MiniMapLayer
        if not (self.list_.contains(miniMapLayer)):
            self.list_.add(miniMapLayer)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        java_super_call(super(), "removeAllListeners")
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        self.list_.remove(eventListenerInterface)
        java_super_call(super(), "removeListener", eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.game.layer.geographic.map.MiniMapLayer import MiniMapLayer
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                miniMapLayer: MiniMapLayer = self.list_.get(index)
                miniMapLayer.onGeographicMapCellPositionEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        java_super_call(super(), "fireEvent", eventObject)
    

    # throws Exception
    def fireRemoveEvent(self, eventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return __class__.__dict__["_fireRemoveEvent_unlocked"].__get__(self, __class__)(eventObject)

    def _fireRemoveEvent_unlocked(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.game.layer.geographic.map.MiniMapLayer import MiniMapLayer
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        list_: BasicArrayList = self.eventListenerInterfaceList
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                miniMapLayer: MiniMapLayer = self.list_.get(index)
                miniMapLayer.onRemoveGeographicMapCellPositionEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        eventListenerInterface: EventListenerInterface = None
        geographicMapCellPositionEventListenerInterface: GeographicMapCellPositionEventListenerInterface = None
        size: int = list_.size()
        for index in range(0, size):
            try:
                eventListenerInterface = list_.get(index)
                geographicMapCellPositionEventListenerInterface = (eventListenerInterface)
                geographicMapCellPositionEventListenerInterface.onRemoveGeographicMapCellPositionEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        geographicMapCellPositionEventListenerInterface: GeographicMapCellPositionEventListenerInterface = (eventListenerInterface)
        geographicMapCellPositionEventListenerInterface.onGeographicMapCellPositionEvent(eventObject)
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.game.layer.geographic.map.MiniMapLayer import MiniMapLayer
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.EventStrings import EventStrings


def _GeographicMapCellPositionEventHandler_instance() -> object:
    return GeographicMapCellPositionEventHandler()

lazy_static(GeographicMapCellPositionEventHandler, "instance", _GeographicMapCellPositionEventHandler_instance)

