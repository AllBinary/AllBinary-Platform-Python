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
# package org.allbinary.input.event

from __future__ import annotations

import time
import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class VirtualKeyboardEventHandler(BasicEventHandler):
    gameKeyEventHandler: VirtualKeyboardEventHandler = None

    def _init_fields(self) -> None:
        self.SHOW_EVENT: VirtualKeyboardEvent = VirtualKeyboardEvent(BooleanFactory.getInstance().TRUE)
        self.HIDE_EVENT: VirtualKeyboardEvent = VirtualKeyboardEvent(BooleanFactory.getInstance().FALSE)
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> VirtualKeyboardEventHandler:
        return VirtualKeyboardEventHandler.gameKeyEventHandler
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        virtualKeyboardEventListenerInterface: VirtualKeyboardEventListenerInterface = eventListenerInterface
        virtualKeyboardEventListenerInterface.onVirtualKeyboardEvent(eventObject)
    

    def open(self) -> None:
        try:
            time.sleep((120) / 1000)
            self.fireEvent(self.SHOW_EVENT)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "open", e)
    

    # throws Exception
    def close(self) -> None:
        try:
            time.sleep((120) / 1000)
            self.fireEvent(self.HIDE_EVENT)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CLOSE, e)
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.input.event.VirtualKeyboardEvent import VirtualKeyboardEvent


VirtualKeyboardEventHandler.gameKeyEventHandler = VirtualKeyboardEventHandler()

