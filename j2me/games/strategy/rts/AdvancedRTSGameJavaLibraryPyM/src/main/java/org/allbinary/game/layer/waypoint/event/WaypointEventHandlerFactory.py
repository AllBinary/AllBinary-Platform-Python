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

from java.lang.JavaRuntimeStatic import lazy_static


class WaypointEventHandlerFactory:
    eventHandlerArray: list[WaypointEventHandler] = None
    

    @staticmethod
    def getInstance(groupInterface: Group) -> WaypointEventHandler:
        from org.allbinary.game.identification.Group import Group
        groupId: int = int(groupInterface.getGroupId())
        return WaypointEventHandlerFactory.eventHandlerArray[groupId]
    

    @staticmethod
    def removeAll() -> None:
        for index in range(len(WaypointEventHandlerFactory.eventHandlerArray) - 1, 0 - 1, -1):
            WaypointEventHandlerFactory.eventHandlerArray[index].removeAllListeners()
# from org.allbinary.game.identification.Group import Group


def _WaypointEventHandlerFactory_eventHandlerArray() -> object:
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    from org.allbinary.game.layer.waypoint.event.WaypointEventHandler import WaypointEventHandler
    return [WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler(), WaypointEventHandler()]

lazy_static(WaypointEventHandlerFactory, "eventHandlerArray", _WaypointEventHandlerFactory_eventHandlerArray)

