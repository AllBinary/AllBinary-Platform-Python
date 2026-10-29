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
# package org.allbinary.android.input.motion.event

from __future__ import annotations

from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class AnalogControllerConfigurationEventHandler(BasicEventHandler):
    instance: AnalogControllerConfigurationEventHandler = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> AnalogControllerConfigurationEventHandler:
        return AnalogControllerConfigurationEventHandler.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def addListener(self, analogControllerConfigurationEventListenerInterface: AnalogControllerConfigurationEventListenerInterface) -> None:
        if not self.list_.contains(analogControllerConfigurationEventListenerInterface):
            self.list_.add(analogControllerConfigurationEventListenerInterface)
    

    def removeAllListeners(self) -> None:
        self.list_.clear()
        super().removeAllListeners()
    

    def removeListener(self, eventListenerInterface: EventListenerInterface) -> None:
        self.list_.remove(eventListenerInterface)
        super().removeListener(eventListenerInterface)
    

    # throws Exception
    def fireEvent(self, eventObject: AllBinaryEventObject) -> None:
        index = self.list_.size()
        while (index := index - 1) >= 0:
            try:
                playerGameInput: AnalogControllerConfigurationEventListenerInterface = self.list_.objectArray[index]
                playerGameInput.onAnalogControllerConfigurationEvent(eventObject)
            except Exception as e:
                self.logUtil.put(self.commonStrings.EXCEPTION, self, EventStrings.getInstance().FIRE_EVENT, e)
        super().fireEvent(eventObject)
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        analogControllerConfigurationEventListenerInterface: AnalogControllerConfigurationEventListenerInterface = (eventListenerInterface)
        analogControllerConfigurationEventListenerInterface.onAnalogControllerConfigurationEvent(eventObject)
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


AnalogControllerConfigurationEventHandler.instance = AnalogControllerConfigurationEventHandler()

