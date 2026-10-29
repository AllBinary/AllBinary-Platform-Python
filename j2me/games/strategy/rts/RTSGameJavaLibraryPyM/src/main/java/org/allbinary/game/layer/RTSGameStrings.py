# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



class RTSGameStrings:
    instance: RTSGameStrings = None

    def _init_fields(self) -> None:
        self.DRAG_TO_SPOT: str = "Please Drag"
        self.NOT_YOURS: str = "Not Yours"
        self.NEW_UNIT: str = "New Unit"
        self.NEW_WAYPOINT: str = "New Waypoint"
        self.BUILDING: str = "Building"
        self.UPGRADE: str = "Upgrading"
        self.DOWNGRADE: str = "Downgrading"
        self.NO_MONEY: str = "Not Enough Money"
        self.SPOT_TAKEN: str = "Spot Taken"
        self.BUILDING_COLLISION: str = "Building Collision"
        self.STRUCTURE_TO_CLOSE: str = "Building To Close"
        self.MAP_EDGE: str = "Map Edge"
        self.ROAD_COLLISION: str = "Road Collision"
        self.SELECT_BUILD_SPOT: str = "Select Build Spot"
        self.BUILD_ON_PATH: str = "Not On Path"
        self.DRAGGABLE: str = "Draggable"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RTSGameStrings:
        return RTSGameStrings.instance


RTSGameStrings.instance = RTSGameStrings()

