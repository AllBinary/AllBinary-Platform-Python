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
# package org.allbinary.game.combat.destroy.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class DestroyedEventHandler(BasicEventHandler):
    instance: DestroyedEventHandler = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("list_", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> DestroyedEventHandler:
        with DestroyedEventHandler._lock:
            return DestroyedEventHandler._getInstance_unlocked()

    @staticmethod
    def _getInstance_unlocked() -> DestroyedEventHandler:
        return DestroyedEventHandler.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer) -> None:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        if not (self.list_.contains(collidableDestroyableDamageableLayer)):
            self.list_.add(collidableDestroyableDamageableLayer)
    

    def removeAllListeners(self) -> None:
        with self._lock:
            return __class__.__dict__["_removeAllListeners_unlocked"].__get__(self, __class__)()

    def _removeAllListeners_unlocked(self) -> None:
        self.list_.clear()
        java_super_call(super(), "removeAllListeners")
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        with self._lock:
            return __class__.__dict__["_removeListener_unlocked"].__get__(self, __class__)(eventListenerInterface)

    def _removeListener_unlocked(self, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        self.list_.remove(eventListenerInterface)
        java_super_call(super(), "removeListener", eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = self.list_.objectArray[index]
                collidableDestroyableDamageableLayer.onDestroyed(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        java_super_call(super(), "fireEvent", eventObject)
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
        destroyedEventListenerInterface: DestroyedEventListenerInterface = eventListenerInterface
        destroyedEventListenerInterface.onDestroyed(eventObject)
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _DestroyedEventHandler_instance() -> object:
    return DestroyedEventHandler()

lazy_static(DestroyedEventHandler, "instance", _DestroyedEventHandler_instance)

