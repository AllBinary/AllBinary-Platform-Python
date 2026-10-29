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
# package org.allbinary.game.input.mapping.event

from __future__ import annotations

from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class InputMappingEventHandler(BasicEventHandler):
    gameKeyEventHandler: InputMappingEventHandler = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> InputMappingEventHandler:
        return InputMappingEventHandler.gameKeyEventHandler
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        inputMappingEventListenerInterface: InputMappingEventListenerInterface = eventListenerInterface
        inputMappingEventListenerInterface.onInputMappingEvent(eventObject)
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


InputMappingEventHandler.gameKeyEventHandler = InputMappingEventHandler()

