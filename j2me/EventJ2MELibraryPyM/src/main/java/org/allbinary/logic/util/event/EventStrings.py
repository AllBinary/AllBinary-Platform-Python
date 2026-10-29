# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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



class EventStrings:
    instance: EventStrings = None

    def _init_fields(self) -> None:
        self.PERFORMANCE_MESSAGE: str = "Use Custom onEvent Methods for needed optimization"
        self.TOTAL_LISTENERS: str = "Total Listeners: "
        self.LISTENER_LABEL: str = " Listener: "
        self.FIRE_EVENT: str = "fireEvent"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> EventStrings:
        return EventStrings.instance


EventStrings.instance = EventStrings()

