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
# package org.allbinary.logic.util.event.handler

from __future__ import annotations

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandlerInterface import BasicEventHandlerInterface


class BasicEventHandler(BasicEventHandlerInterface):
    PERFORMANCE_MESSAGE: str = "Use Custom onEvent Methods for needed optimization"
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.eventListenerInterfaceList: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.eventListenerInterfaceList = BasicArrayListD()
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        LISTENER: str = " Listener: "
        stringBuffer.append("Total Listeners: ")
        stringBuffer.appendint(self.eventListenerInterfaceList.size())
        eventListenerInterface: EventListenerInterface = None
        index: int = 0
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.objectArray[index]
                stringBuffer.append(LISTENER)
                stringBuffer.append(StringUtil.getInstance().toString(eventListenerInterface))
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.TOSTRING, e)
            index += 1
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def removeAllListeners(self) -> None:
        with self._lock:
            return self._removeAllListeners_unlocked()

    def _removeAllListeners_unlocked(self) -> None:
        self.eventListenerInterfaceList = BasicArrayListD()
    

    def addListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        if not self.eventListenerInterfaceList.contains(eventListenerInterface):
            self.eventListenerInterfaceList.add(eventListenerInterface)
    

    def addListenerInterface(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return self._addListenerInterface_unlocked(eventListenerInterface)

    def _addListenerInterface_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        if not self.eventListenerInterfaceList.contains(eventListenerInterface):
            self.eventListenerInterfaceList.add(eventListenerInterface)
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        self.eventListenerInterfaceList.remove(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return self._removeListener_unlocked(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        self.eventListenerInterfaceList.remove(eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return self._fireEvent_unlocked(eventObject)

    def _fireEvent_unlocked(self, eventObject: AllBinaryEventObject) -> None:
        index: int = 0
        eventListenerInterface: EventListenerInterface = None
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.objectArray[index]
                self.process(eventObject, eventListenerInterface)
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
            index += 1
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        eventListenerInterface.onEvent(eventObject)
    

    def getEventListenerInterfaceListP(self) -> BasicArrayList:
        return self.eventListenerInterfaceList
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


