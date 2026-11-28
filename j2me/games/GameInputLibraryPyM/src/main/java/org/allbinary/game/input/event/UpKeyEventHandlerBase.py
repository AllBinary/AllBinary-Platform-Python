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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class UpKeyEventHandlerBase(BasicEventHandler):
    TOTAL_LISTENERS: str = " Total PlayerGameInput Listeners: "
    LISTENER_LABEL: str = " PlayerGameInput Listener: "
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("list_", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.list_: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, playerGameInput: PlayerGameInput) -> None:
        from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
        if not (self.list_.contains(playerGameInput)):
            self.list_.add(playerGameInput)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        java_super_call(super(), "removeAllListeners")
    

    def removeListenerSingleThreaded(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        self.list_.remove(eventListenerInterface)
        java_super_call(super(), "removeListenerSingleThreaded", eventListenerInterface)
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return __class__.__dict__["_removeListener_unlocked"].__get__(self, __class__)(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        self.list_.remove(eventListenerInterface)
        java_super_call(super(), "removeListener", eventListenerInterface)
    

    # throws Exception
    def fireEventForInteger(self, eventObject: int) -> None:
        from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                playerGameInput: PlayerGameInput = self.list_.objectArray[index]
                playerGameInput.onUpKeyEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        index: int = 0
        eventListenerInterface: EventListenerInterface = None
        while index < self.eventListenerInterfaceList.size():
            try:
                eventListenerInterface = self.eventListenerInterfaceList.get(index)
                self.processForInteger(eventObject, eventListenerInterface)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
            index += 1
    

    # throws Exception
    def processForInteger(self, eventObject: int, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        upKeyEventListenerInterface: UpKeyEventListenerInterface = eventListenerInterface
        upKeyEventListenerInterface.onUpKeyEvent(eventObject)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(java_super_call(super(), "toString"))
        stringBuffer.append(UpKeyEventHandlerBase.TOTAL_LISTENERS)
        stringBuffer.appendint(self.list_.size())
        for index in range(0, self.list_.size()):
            try:
                eventListenerInterface: EventListenerInterface = self.list_.get(index)
                stringBuffer.append(UpKeyEventHandlerBase.LISTENER_LABEL)
                stringBuffer.append(str(eventListenerInterface))
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.TOSTRING, e)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


