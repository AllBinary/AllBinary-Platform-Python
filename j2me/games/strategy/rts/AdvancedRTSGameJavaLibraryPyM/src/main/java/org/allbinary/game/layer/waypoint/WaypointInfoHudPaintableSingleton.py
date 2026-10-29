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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from org.allbinary.game.layer.waypoint.WaypointInfoHudPaintable import WaypointInfoHudPaintable


class WaypointInfoHudPaintableSingleton:
    instance: WaypointInfoHudPaintable = WaypointInfoHudPaintable()
    

    @staticmethod
    def getInstance() -> WaypointInfoHudPaintable:
        return WaypointInfoHudPaintableSingleton.instance


