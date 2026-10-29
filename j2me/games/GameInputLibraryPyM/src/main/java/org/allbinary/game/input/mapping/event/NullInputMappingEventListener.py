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
# package org.allbinary.game.input.mapping.event

from __future__ import annotations

from org.allbinary.game.input.mapping.event.InputMappingEventListenerInterface import InputMappingEventListenerInterface


class NullInputMappingEventListener(InputMappingEventListenerInterface):
    NULL_INPUT_MAPPING_EVENT_LISTENER: NullInputMappingEventListener = None
    

    # throws Exception
    def onInputMappingEvent(self, inputMappingEvent: InputMappingEvent) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        pass
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


NullInputMappingEventListener.NULL_INPUT_MAPPING_EVENT_LISTENER = NullInputMappingEventListener()

