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

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class LayerManagerEventHandler(BasicEventHandler):
    instance: LayerManagerEventHandler = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
        self.CREATE: str = "Create"
        self.DELETE: str = "Delete"
    

    @staticmethod
    def getInstance() -> LayerManagerEventHandler:
        return LayerManagerEventHandler.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addListener(self, layerManagerEventListener: LayerManagerEventListener) -> None:
        if not self.list_.contains(layerManagerEventListener):
            self.list_.add(layerManagerEventListener)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        super().removeAllListeners()
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        self.list_.remove(eventListenerInterface)
        super().removeListener(eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                layerManagerEventListener: LayerManagerEventListener = self.list_.objectArray[index]
                layerManagerEventListener.onCreateLayerManagerEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        super().fireEvent(eventObject)
    

    # throws Exception
    def fireDeleteEvent(self, eventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return self._fireDeleteEvent_unlocked(eventObject)

    def _fireDeleteEvent_unlocked(self, eventObject: AllBinaryEventObject) -> None:
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
        index: int = 0
        while index < eventListenerInterfaceList.size():
            try:
                eventListenerInterface = eventListenerInterfaceList.objectArray[index]
                layerManagerEventListenerInterface = (eventListenerInterface)
                layerManagerEventListenerInterface.onDeleteLayerManagerEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
            index += 1
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        layerManagerEventListenerInterface: LayerManagerEventListenerInterface = (eventListenerInterface)
        layerManagerEventListenerInterface.onCreateLayerManagerEvent(eventObject)
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


LayerManagerEventHandler.instance = LayerManagerEventHandler()

