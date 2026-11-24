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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class RTSLayer2LogHelper:
    instance: RTSLayer2LogHelper = None
    

    @staticmethod
    def getInstance() -> RTSLayer2LogHelper:
        return RTSLayer2LogHelper.instance
    

    def steeringUp(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        pass
    

    def steeringFireOrStop(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        pass
    

    def buildingAbove(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        pass
    

    def buildingChaseLeft(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        pass
    

    def buildingChaseRight(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        pass
    

    def buildingDown(self, pathFindingLayerInterface: PathFindingLayerInterface) -> None:
        pass
    

    def buildingChaseDown(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        pass
    

    def buildingChaseUp(self, pathFindingLayerInterface: PathFindingLayerInterface, angle: int) -> None:
        pass
    

    def buildingLeft(self) -> None:
        pass
    

    def buildingRight(self) -> None:
        pass


def _RTSLayer2LogHelper_instance() -> object:
    return RTSLayer2LogHelper()

lazy_static(RTSLayer2LogHelper, "instance", _RTSLayer2LogHelper_instance)

