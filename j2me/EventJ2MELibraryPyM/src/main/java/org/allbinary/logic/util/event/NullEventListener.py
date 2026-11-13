# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.logic.util.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


class NullEventListener(EventListenerInterface):
    NULL_EVENT_LISTENER: NullEventListener = None
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        pass


def _NullEventListener_NULL_EVENT_LISTENER() -> object:
    return NullEventListener()

lazy_static(NullEventListener, "NULL_EVENT_LISTENER", _NullEventListener_NULL_EVENT_LISTENER)

