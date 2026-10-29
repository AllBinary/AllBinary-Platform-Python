# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.layer.capital.event

from __future__ import annotations

from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


# Java interface
class CapitalEventListenerInterface(EventListenerInterface):
    

    # throws Exception
    def onCapitalChangeEvent(self, event: CapitalEvent) -> None:
        raise NotImplementedError()


