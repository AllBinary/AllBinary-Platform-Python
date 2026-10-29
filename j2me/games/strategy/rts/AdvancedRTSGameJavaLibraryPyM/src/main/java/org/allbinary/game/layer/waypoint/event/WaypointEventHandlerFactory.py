# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.waypoint.event

from __future__ import annotations

from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler


class WaypointEventHandlerFactory:
    eventHandlerArray: list[WaypointEventHandler] = [WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler()]
    

    @staticmethod
    def getInstance(groupInterface: Group) -> WaypointEventHandler:
        return WaypointEventHandlerFactory.eventHandlerArray[int(groupInterface.getGroupId())]
    

    @staticmethod
    def removeAll() -> None:
        for index in range(len(WaypointEventHandlerFactory.eventHandlerArray) - 1, 0 - 1, -1):
            WaypointEventHandlerFactory.eventHandlerArray[index].removeAllListeners()
from org.allbinary.game.identification.Group import Group


