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


class Waypoint2LogHelper:
    instance: Waypoint2LogHelper = None
    

    @staticmethod
    def getInstance() -> Waypoint2LogHelper:
        return Waypoint2LogHelper.instance
    

    def initRange(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, closeRange: int, sensorRange: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def processPossibleTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int, isShorterThanCurrentTargetDistance: bool, isCurrentTargetDestroyed: bool) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def processSetTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def processPossibleTargetCloser(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def setTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def setTargetPath(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def setTargetPathIgnoreNewPath(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def processWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, targetLayer: PathFindingLayerInterface, size: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def processWaypointTracked(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def processWaypointTrackedVisit(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        pass
    

    def processWaypointTrackedWithoutProgress(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, reason: str) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def wander(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def targetDestroyed(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def processTargeting(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, dx: int, dy: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def processTargetingNonWayPoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, dx: int, dy: int) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def removeWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, waypointLayer: PathFindingLayerInterface, reason: str) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        pass
    

    def removeWaypointList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, list_: BasicArrayList) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
    

    def removeWaypointClear(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def clearTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def addWaypointFromUser(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
    

    def targetMovedSoRetarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        pass
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _Waypoint2LogHelper_instance() -> object:
    return Waypoint2LogHelper()

lazy_static(Waypoint2LogHelper, "instance", _Waypoint2LogHelper_instance)

