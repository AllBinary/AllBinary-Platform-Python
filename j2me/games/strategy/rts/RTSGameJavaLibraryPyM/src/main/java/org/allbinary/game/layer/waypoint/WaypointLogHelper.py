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

from java.lang.JavaRuntimeStatic import lazy_static


class WaypointLogHelper:
    instance: WaypointLogHelper = None
    

    @staticmethod
    def getInstance() -> WaypointLogHelper:
        return WaypointLogHelper.instance
    

    def onWaypointEvent(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def addWaypointFromBuilding(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def addWaypointFromBuildingList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface, list_: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
    

    def insertWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, index: int, rtsLayer: CollidableDestroyableDamageableLayer, waypointName: str) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        pass
    

    def insertWaypointList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, index: int, rtsLayer: CollidableDestroyableDamageableLayer, waypointName: str, list_: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
    

    def setRandomGeographicMapCellHistoryList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, pathsList: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
    

    def moveAwayFromBuilding(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def needToMove(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior: WaypointBehaviorBase) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def setRandomGeographicMapCellHistory(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def setCurrentPathGeographicMapCellPosition(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, existingCurrentPathGeographicMapCellPosition: GeographicMapCellPosition, currentPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        pass
    

    def setNextUnvisitedPathGeographicMapCellPosition(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, existingNextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition, nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        pass
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _WaypointLogHelper_instance() -> object:
    return WaypointLogHelper()

lazy_static(WaypointLogHelper, "instance", _WaypointLogHelper_instance)

