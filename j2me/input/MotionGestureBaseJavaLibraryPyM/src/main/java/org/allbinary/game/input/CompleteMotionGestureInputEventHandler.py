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
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class CompleteMotionGestureInputEventHandler(BasicEventHandler):
    SINGLETON: CompleteMotionGestureInputEventHandler = None
    def _java_defaults(self):
        vars(self).setdefault("list_", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> CompleteMotionGestureInputEventHandler:
        return CompleteMotionGestureInputEventHandler.SINGLETON
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, completeMotionGestureInputEventListener: CompleteMotionGestureInputEventListener) -> None:
        if not (self.list_.contains(completeMotionGestureInputEventListener)):
            self.list_.add(completeMotionGestureInputEventListener)
    

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
                completeMotionGestureInputEventListener: CompleteMotionGestureInputEventListener = self.list_.objectArray[index]
                completeMotionGestureInputEventListener.onCompleteMotionGestureInputEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        java_super_call(super(), "fireEvent", eventObject)
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        completeMotionGestureInputEventListenerInterface: CompleteMotionGestureInputEventListenerInterface = eventListenerInterface
        completeMotionGestureInputEventListenerInterface.onCompleteMotionGestureInputEvent(eventObject)
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _CompleteMotionGestureInputEventHandler_SINGLETON() -> object:
    return CompleteMotionGestureInputEventHandler()

lazy_static(CompleteMotionGestureInputEventHandler, "SINGLETON", _CompleteMotionGestureInputEventHandler_SINGLETON)

