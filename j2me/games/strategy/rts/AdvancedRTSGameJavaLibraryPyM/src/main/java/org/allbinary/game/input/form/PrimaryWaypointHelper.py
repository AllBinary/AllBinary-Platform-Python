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
# package org.allbinary.game.input.form

from __future__ import annotations



class PrimaryWaypointHelper:
    instance: PrimaryWaypointHelper = None

    def _init_fields(self) -> None:
        self.waypointLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
    

    @staticmethod
    def getInstance() -> PrimaryWaypointHelper:
        return PrimaryWaypointHelper.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getWaypointLayer(self) -> PathFindingLayerInterface:
        return self.waypointLayer
    

    def setWaypointLayer(self, waypointLayer: WaypointLayer) -> None:
        self.waypointLayer = waypointLayer
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.waypoint.WaypointLayer import WaypointLayer


PrimaryWaypointHelper.instance = PrimaryWaypointHelper()

