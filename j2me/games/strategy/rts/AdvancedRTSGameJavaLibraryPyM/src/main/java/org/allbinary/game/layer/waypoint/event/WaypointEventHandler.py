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
# package org.allbinary.game.layer.waypoint.event

from __future__ import annotations

from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class WaypointEventHandler(BasicEventHandler):
    

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def process(self, eventObject: AllBinaryEventObject, eventListenerInterface: EventListenerInterface) -> None:
        waypointEventListenerInterface: WaypointEventListenerInterface = (eventListenerInterface)
        waypointEventListenerInterface.onWaypointEvent(eventObject)
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventListenerInterface import EventListenerInterface


