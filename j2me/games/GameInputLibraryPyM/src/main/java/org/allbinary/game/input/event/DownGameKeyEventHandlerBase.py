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
# package org.allbinary.game.input.event

from __future__ import annotations

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class DownGameKeyEventHandlerBase(BasicEventHandler):
    TOTAL_LISTENERS: str = " Total PlayerGameInput Listeners: "
    LISTENER_LABEL: str = " PlayerGameInput Listener: "
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addListener(self, playerGameInput: PlayerGameInput) -> None:
        if not self.list_.contains(playerGameInput):
            self.list_.add(playerGameInput)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        super().removeAllListeners()
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        self.list_.remove(eventListenerInterface)
        super().removeListenerSingleThreaded(eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return self._removeListener_unlocked(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        self.list_.remove(eventListenerInterface)
        super().removeListener(eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                playerGameInput: PlayerGameInput = self.list_.objectArray[index]
                playerGameInput.onDownGameKeyEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        super().fireEvent(eventObject)
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        downGameKeyEventListenerInterface: DownGameKeyEventListenerInterface = eventListenerInterface
        downGameKeyEventListenerInterface.onDownGameKeyEvent(eventObject)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(str(super()))
        stringBuffer.append(DownGameKeyEventHandlerBase.TOTAL_LISTENERS)
        stringBuffer.appendint(self.list_.size())
        eventListenerInterface: EventListenerInterface = None
        size: int = self.list_.size()
        index: int = 0
        while index < size:
            try:
                eventListenerInterface = self.list_.get(index)
                stringBuffer.append(DownGameKeyEventHandlerBase.LISTENER_LABEL)
                stringBuffer.append(str(eventListenerInterface))
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.TOSTRING, e)
            index += 1
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


