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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations



class WaypointRunnableLogHelper:
    instance: WaypointRunnableLogHelper = None
    

    @staticmethod
    def getInstance() -> WaypointRunnableLogHelper:
        return WaypointRunnableLogHelper.instance
    

    def start(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        pass
    

    def end(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        pass
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface


WaypointRunnableLogHelper.instance = WaypointRunnableLogHelper()

