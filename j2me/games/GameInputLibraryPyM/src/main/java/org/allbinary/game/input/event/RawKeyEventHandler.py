# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.input.event

from __future__ import annotations



class RawKeyEventHandler:
    instance: RawKeyEventHandler = None
    TOTAL_LISTENERS: str = "Total Listeners: "
    LISTENER_LABEL: str = " Listener: "

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.eventListenerInterfaceList: BasicArrayList = None
    

    @staticmethod
    def getInstance() -> RawKeyEventHandler:
        return RawKeyEventHandler.instance
    

    def __init__(self) -> None:
        self._init_fields()
        self.eventListenerInterfaceList = BasicArrayListD()
    

    def removeAllListeners(self) -> None:
        self.eventListenerInterfaceList = BasicArrayListD()
    

    def addListeners(self, vector: BasicArrayList) -> None:
        eventListenerInterface: RawKeyEventListener = None
        size: int = vector.size()
        for index in range(0, size):
            eventListenerInterface = vector.get(index)
            self.addListener(eventListenerInterface)
    

    def addListenerSingleThreaded(self, eventListenerInterface: RawKeyEventListener) -> None:
        if not self.eventListenerInterfaceList.contains(eventListenerInterface):
            self.eventListenerInterfaceList.add(eventListenerInterface)
    

    def addListener(self, eventListenerInterface: RawKeyEventListener) -> None:
        if not self.eventListenerInterfaceList.contains(eventListenerInterface):
            self.eventListenerInterfaceList.add(eventListenerInterface)
    

    def removeListenerSingleThreaded(self, eventListenerInterface: RawKeyEventListener) -> None:
        self.eventListenerInterfaceList.remove(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: RawKeyEventListener) -> None:
        self.eventListenerInterfaceList.remove(eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, keyCode: int, deviceId: int, repeated: bool) -> None:
        eventListenerInterface: RawKeyEventListener = None
        index: int = 0
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.get(index)
                self.process(keyCode, deviceId, repeated, eventListenerInterface)
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
            index += 1
    

    # throws Exception
    def process(self, keyCode: int, deviceId: int, repeated: bool, eventListenerInterface: RawKeyEventListener) -> None:
        eventListenerInterface.onEventRaw(keyCode, deviceId, repeated)
    

    def getEventListenerInterfaceListP(self) -> BasicArrayList:
        return self.eventListenerInterfaceList
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(RawKeyEventHandler.TOTAL_LISTENERS)
        stringBuffer.appendint(self.eventListenerInterfaceList.size())
        eventListenerInterface: RawKeyEventListener = None
        index: int = 0
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.get(index)
                stringBuffer.append(RawKeyEventHandler.LISTENER_LABEL)
                stringBuffer.append(str(eventListenerInterface))
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.TOSTRING, e)
            index += 1
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


RawKeyEventHandler.instance = RawKeyEventHandler()

