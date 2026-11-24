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
# package org.allbinary.game.layer.unit

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class UnitWaypointStrings:
    instance: UnitWaypointStrings = None

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonLabels import CommonLabels
        self.PATHING: str = "Pathing"
        self.WANDERING: str = "Order?"
        self.THINKING: str = "Thinking"
        self.THINKING_ABOUT_TARGET: str = "Hmmm"
        self.TARGET: str = "Target"
        self.KILL: str = "Kill!"
        self.STOP: str = "Stop"
        self.WAYPOINT_DESTROYED_SHORT: str = "Uh Oh"
        self.WAYPOINT_DESTROYED: str = "Waypoint Destroyed"
        self.ALL_VISITED_SHORT: str = "Arrived"
        self.ALL_VISITED: str = "All Visited"
        self.ALREADY_THERE_SHORT: str = "Again?"
        self.ALREADY_THERE: str = "Already There"
        self.NEXT_PATH_NODE: str = str(CommonLabels.getInstance().NEXT) + " Path Node"
        self._ALL_VISITED_SHORT: str = " Arrived"
        self._ALREADY_THERE_SHORT: str = " Again?"
        self.VISITED_MOST_OF_THE_PATH: str = " visited most of the path"
        self.RETURNING_AS_WAYPOINT_PATH_LIST: str = " returning as waypointPathsList was runningWaypointPathList"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> UnitWaypointStrings:
        return UnitWaypointStrings.instance
# from org.allbinary.string.CommonLabels import CommonLabels


def _UnitWaypointStrings_instance() -> object:
    return UnitWaypointStrings()

lazy_static(UnitWaypointStrings, "instance", _UnitWaypointStrings_instance)

