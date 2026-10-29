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



# Java interface
class BasicEventHandlerInterface:
    

    def addListenerInterface(self, eventListenerInterface: EventListenerInterface) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        raise NotImplementedError()
    

    def removeAllListeners(self) -> None:
        raise NotImplementedError()
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        raise NotImplementedError()
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


