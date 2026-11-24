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

from org.allbinary.game.tick.TickableInterface import TickableInterface


class WaypointBehaviorBase(TickableInterface):

    def _init_fields(self) -> None:
        from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.ownedWaypointList: BasicArrayList = None
        self.waypointOverridesAttacking: bool = True
        self.waypoint: WaypointBase = WaypointBase.NULL_WAYPOINT_BASE
        self.steeringVisitorList: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        from org.allbinary.util.BasicArrayListS import BasicArrayListS
        self._init_fields()
        self.ownedWaypointList = BasicArrayListS(1)
    

    def getName(self) -> str:
        return type(self).__module__ + "." + type(self).__qualname__
    

    def isRunning(self) -> bool:
        return False
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    def getOwnedWaypointList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.ownedWaypointList
    

    def getWaypoint(self) -> WaypointBase:
        from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
        return self.waypoint
    

    def setWaypoint(self, waypoint: WaypointBase) -> None:
        from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
        self.waypoint = waypoint
    

    def getSteeringVisitorList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.steeringVisitorList
    

    def getMovementLogicAsString(self) -> str:
        raise RuntimeError()
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        raise RuntimeError()
    

    def isInSensorRange(self, layerInterface: CollidableDestroyableDamageableLayer, targetDistance: int) -> bool:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        raise RuntimeError()
    

    def getCurrentTargetLayerInterface(self) -> CollidableDestroyableDamageableLayer:
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        raise RuntimeError()
    

    def getCurrentTargetingStateString(self) -> str:
        raise RuntimeError()
    

    def isTrackingWaypoint(self) -> bool:
        raise RuntimeError()
    

    def getCurrentPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    def getCurrentGeographicMapCellHistory(self) -> GeographicMapCellHistory:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        raise RuntimeError()
    

    def isWaypointOverridesAttacking(self) -> bool:
        return self.waypointOverridesAttacking
    

    def getNextUnvisitedPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    def needToMove(self) -> bool:
        raise RuntimeError()
    

    def setWaypointPathsList(self, waypointPathsList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    def getWaypointPathsList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    # throws Exception
    def setTarget(self, layerInterface: PathFindingLayerInterface) -> None:
        raise RuntimeError()
    

    # throws Exception
    def setTargetWithDistance(self, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        raise RuntimeError()
    

    # throws Exception
    def clearTarget(self) -> None:
        raise RuntimeError()
    

    # throws Exception
    def updatePathOnTargetMove(self, reason: str) -> None:
        pass
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
# from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayListS import BasicArrayListS


