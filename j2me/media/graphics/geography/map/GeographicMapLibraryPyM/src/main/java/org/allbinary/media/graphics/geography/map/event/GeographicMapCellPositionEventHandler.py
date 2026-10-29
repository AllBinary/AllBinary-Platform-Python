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

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class GeographicMapCellPositionEventHandler(BasicEventHandler):
    instance: GeographicMapCellPositionEventHandler = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> GeographicMapCellPositionEventHandler:
        return GeographicMapCellPositionEventHandler.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addListener(self, miniMapLayer: MiniMapLayer) -> None:
        if not self.list_.contains(miniMapLayer):
            self.list_.add(miniMapLayer)
    

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
                miniMapLayer: MiniMapLayer = self.list_.get(index)
                miniMapLayer.onGeographicMapCellPositionEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        super().fireEvent(eventObject)
    

    # throws Exception
    def fireRemoveEvent(self, eventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return self._fireRemoveEvent_unlocked(eventObject)

    def _fireRemoveEvent_unlocked(self, eventObject: AllBinaryEventObject) -> None:
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
        geographicMapCellPositionEventListenerInterface: GeographicMapCellPositionEventListenerInterface = (eventListenerInterface)
        geographicMapCellPositionEventListenerInterface.onGeographicMapCellPositionEvent(eventObject)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.layer.geographic.map.MiniMapLayer import MiniMapLayer
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings


GeographicMapCellPositionEventHandler.instance = GeographicMapCellPositionEventHandler()

