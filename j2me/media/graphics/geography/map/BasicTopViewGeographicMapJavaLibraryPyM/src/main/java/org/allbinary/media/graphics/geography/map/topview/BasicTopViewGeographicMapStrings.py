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
# package org.allbinary.media.graphics.geography.map.topview

from __future__ import annotations



class BasicTopViewGeographicMapStrings:
    instance: BasicTopViewGeographicMapStrings = None

    def _init_fields(self) -> None:
        self.DEFAULT: str = "Default"
        self.OTHER: str = "Other"
        self.WALL: str = "Wall"
        self.OFF_MAP: str = "OffMap"
        self.FLOOR: str = "Floor"
        self.DOOR: str = "Door"
        self.STAIRS_UP: str = "StairsUp"
        self.STAIRS_DOWN: str = "StairsDown"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicTopViewGeographicMapStrings:
        return BasicTopViewGeographicMapStrings.instance


BasicTopViewGeographicMapStrings.instance = BasicTopViewGeographicMapStrings()

