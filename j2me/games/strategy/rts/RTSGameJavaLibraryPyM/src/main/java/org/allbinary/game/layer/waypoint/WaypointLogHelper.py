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



class WaypointLogHelper:
    instance: WaypointLogHelper = None
    

    @staticmethod
    def getInstance() -> WaypointLogHelper:
        return WaypointLogHelper.instance
    

    def onWaypointEvent(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def addWaypointFromBuilding(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def addWaypointFromBuildingList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface, list_: BasicArrayList) -> None:
        pass
    

    def insertWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, index: int, rtsLayer: CollidableDestroyableDamageableLayer, waypointName: str) -> None:
        pass
    

    def insertWaypointList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, index: int, rtsLayer: CollidableDestroyableDamageableLayer, waypointName: str, list_: BasicArrayList) -> None:
        pass
    

    def setRandomGeographicMapCellHistoryList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, pathsList: BasicArrayList) -> None:
        pass
    

    def moveAwayFromBuilding(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def needToMove(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior: WaypointBehaviorBase) -> None:
        pass
    

    def setRandomGeographicMapCellHistory(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        pass
    

    def setCurrentPathGeographicMapCellPosition(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, existingCurrentPathGeographicMapCellPosition: GeographicMapCellPosition, currentPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        pass
    

    def setNextUnvisitedPathGeographicMapCellPosition(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, existingNextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition, nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        pass
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.util.BasicArrayList import BasicArrayList


WaypointLogHelper.instance = WaypointLogHelper()

