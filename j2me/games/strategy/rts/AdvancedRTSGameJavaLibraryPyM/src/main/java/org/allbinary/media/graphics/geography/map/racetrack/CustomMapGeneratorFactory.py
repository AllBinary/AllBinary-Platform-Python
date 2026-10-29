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
# package org.allbinary.media.graphics.geography.map.racetrack

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGeneratorBaseFactory import CustomMapGeneratorBaseFactory


class CustomMapGeneratorFactory(CustomMapGeneratorBaseFactory):

    def __init__(self) -> None:
        super().__init__()
    

    # throws Exception
    def create(self, raceTrackGeographicMap: RaceTrackGeographicMap) -> CustomMapGeneratorBase:
        from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGenerator import CustomMapGenerator
        return CustomMapGenerator(raceTrackGeographicMap)


