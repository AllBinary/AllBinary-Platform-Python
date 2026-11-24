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

from java.lang.JavaRuntimeStatic import lazy_static


class CustomMapGeneratorBaseFactory:
    instance: CustomMapGeneratorBaseFactory = None
    

    @staticmethod
    def getInstance() -> CustomMapGeneratorBaseFactory:
        return CustomMapGeneratorBaseFactory.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def create(self, raceTrackGeographicMap: RaceTrackGeographicMap) -> CustomMapGeneratorBase:
        from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGeneratorBase import CustomMapGeneratorBase
        return CustomMapGeneratorBase()


def _CustomMapGeneratorBaseFactory_instance() -> object:
    return CustomMapGeneratorBaseFactory()

lazy_static(CustomMapGeneratorBaseFactory, "instance", _CustomMapGeneratorBaseFactory_instance)

