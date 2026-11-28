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
# package org.allbinary.layer.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class LayerManagerEventHandler(BasicEventHandler):
    instance: LayerManagerEventHandler = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("list_", None)
        vars(self).setdefault("CREATE", None)
        vars(self).setdefault("DELETE", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.list_: BasicArrayList = BasicArrayListD()
        self.CREATE: str = "Create"
        self.DELETE: str = "Delete"
    

    @staticmethod
    def getInstance() -> LayerManagerEventHandler:
        return LayerManagerEventHandler.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, layerManagerEventListener: LayerManagerEventListener) -> None:
        if not (self.list_.contains(layerManagerEventListener)):
            self.list_.add(layerManagerEventListener)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        java_super_call(super(), "removeAllListeners")
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        self.list_.remove(eventListenerInterface)
        java_super_call(super(), "removeListener", eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                layerManagerEventListener: LayerManagerEventListener = self.list_.objectArray[index]
                layerManagerEventListener.onCreateLayerManagerEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        java_super_call(super(), "fireEvent", eventObject)
    

    # throws Exception
    def fireDeleteEvent(self, eventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return __class__.__dict__["_fireDeleteEvent_unlocked"].__get__(self, __class__)(eventObject)

    def _fireDeleteEvent_unlocked(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        from org.allbinary.util.BasicArrayList import BasicArrayList
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                layerManagerEventListener: LayerManagerEventListener = self.list_.objectArray[index]
                layerManagerEventListener.onDeleteLayerManagerEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        eventListenerInterfaceList: BasicArrayList = self.eventListenerInterfaceList
        eventListenerInterface: EventListenerInterface = None
        layerManagerEventListenerInterface: LayerManagerEventListenerInterface = None
        listenerIndex: int = 0
        while listenerIndex < eventListenerInterfaceList.size():
            try:
                eventListenerInterface = eventListenerInterfaceList.objectArray[listenerIndex]
                layerManagerEventListenerInterface = (eventListenerInterface)
                layerManagerEventListenerInterface.onDeleteLayerManagerEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
            listenerIndex += 1
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        layerManagerEventListenerInterface: LayerManagerEventListenerInterface = (eventListenerInterface)
        layerManagerEventListenerInterface.onCreateLayerManagerEvent(eventObject)
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _LayerManagerEventHandler_instance() -> object:
    return LayerManagerEventHandler()

lazy_static(LayerManagerEventHandler, "instance", _LayerManagerEventHandler_instance)

