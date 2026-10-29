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

from org.allbinary.logic.util.event.handler.BasicEventHandlerInterface import BasicEventHandlerInterface


class BasicEventHandler(BasicEventHandlerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.eventStrings: EventStrings = EventStrings.getInstance()
        self.eventListenerInterfaceList: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.eventListenerInterfaceList = BasicArrayListD()
    

    def removeAllListeners(self) -> None:
        self.eventListenerInterfaceList = BasicArrayListD()
    

    def addListeners(self, vector: BasicArrayList) -> None:
        eventListenerInterface: EventListenerInterface = None
        size: int = vector.size()
        for index in range(0, size):
            eventListenerInterface = vector.get(index)
            self.addListenerInterface(eventListenerInterface)
    

    def removeListeners(self, vector: BasicArrayList) -> None:
        eventListenerInterface: EventListenerInterface = None
        size: int = vector.size()
        for index in range(0, size):
            eventListenerInterface = vector.get(index)
            self.removeListener(eventListenerInterface)
    

    def addListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        if not self.eventListenerInterfaceList.contains(eventListenerInterface):
            self.eventListenerInterfaceList.add(eventListenerInterface)
    

    def addListenerInterface(self, eventListenerInterface: EventListenerInterface) -> None:
        if not self.eventListenerInterfaceList.contains(eventListenerInterface):
            self.eventListenerInterfaceList.add(eventListenerInterface)
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        self.eventListenerInterfaceList.remove(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        self.eventListenerInterfaceList.remove(eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        eventListenerInterface: EventListenerInterface = None
        index: int = 0
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.get(index)
                self.process(eventObject, eventListenerInterface)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.eventStrings.FIRE_EVENT, e)
            index += 1
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        eventListenerInterface.onEvent(eventObject)
    

    def getEventListenerInterfaceListP(self) -> BasicArrayList:
        return self.eventListenerInterfaceList
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.eventStrings.TOTAL_LISTENERS)
        stringBuffer.appendint(self.eventListenerInterfaceList.size())
        eventListenerInterface: EventListenerInterface = None
        index: int = 0
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.get(index)
                stringBuffer.append(self.eventStrings.LISTENER_LABEL)
                stringBuffer.append(str(eventListenerInterface))
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.TOSTRING, e)
            index += 1
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from jsinterop.annotations.JsType import JsType
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor
from jsinterop.annotations.JsProperty import JsProperty


