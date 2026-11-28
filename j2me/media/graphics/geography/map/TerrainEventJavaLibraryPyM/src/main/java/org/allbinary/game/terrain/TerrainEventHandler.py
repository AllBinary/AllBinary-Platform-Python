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
# package org.allbinary.game.terrain

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class TerrainEventHandler(BasicEventHandler):
    hashtable: ABHashtable[object, object] = None
    def _java_defaults(self):
        vars(self).setdefault("list_", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def init() -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        TerrainEventHandler.hashtable = StdUtil.getInstance().createHashtable()
    

    @staticmethod
    def getInstance(anyType: object) -> TerrainEventHandler:
        eventHandlerCanBeNull: object = TerrainEventHandler.hashtable.get(anyType)
        if eventHandlerCanBeNull is None:
            eventHandlerCanBeNull = TerrainEventHandler()
            TerrainEventHandler.hashtable.put(anyType, eventHandlerCanBeNull)
        return eventHandlerCanBeNull
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, terrainEventListener: TerrainEventListener) -> None:
        if not (self.list_.contains(terrainEventListener)):
            self.list_.add(terrainEventListener)
    

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
                terrainEventListener: TerrainEventListener = self.list_.get(index)
                terrainEventListener.onTerrainEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        java_super_call(super(), "fireEvent", eventObject)
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        terrainEventListenerInterface: TerrainEventListenerInterface = eventListenerInterface
        terrainEventListenerInterface.onTerrainEvent(eventObject)
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _TerrainEventHandler_hashtable() -> object:
    from org.allbinary.logic.StdUtil import StdUtil
    from org.allbinary.util.ABHashtable import ABHashtable
    return StdUtil.getInstance().NULL_TABLE

lazy_static(TerrainEventHandler, "hashtable", _TerrainEventHandler_hashtable)

