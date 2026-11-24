# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface


class NullPathFindingLayer(PathFindingLayerInterface):
    NULL_PATH_FINDING_LAYER: NullPathFindingLayer = None
    

    def getName(self) -> str:
        raise RuntimeError()
    

    # throws Exception
    def getEndGeographicMapCellPositionList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    def shouldHandleStartSameAsEnd(self) -> bool:
        raise RuntimeError()
    

    def getGeographicMapCellPositionArea(self) -> GeographicMapCellPositionAreaBase:
        raise RuntimeError()
    

    def getHudPaintable(self) -> SelectionHudPaintable:
        raise RuntimeError()
    

    # throws Exception
    def handleCost(self, ownerLayer: PathFindingLayerInterface) -> None:
        raise RuntimeError()
    

    def getParentLayer(self) -> PathFindingLayerInterface:
        raise RuntimeError()
    

    def getRTSLayer2LogHelper(self) -> RTSLayer2LogHelper:
        raise RuntimeError()
    

    # throws Exception
    def setTarget(self, targetGameLayer: PathFindingLayerInterface) -> None:
        raise RuntimeError()
    

    # throws Exception
    def init(self, geographicMapCellHistory: GeographicMapCellHistory, geographicMapCellPositionBasicArrayList: BasicArrayList) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    def getMoveOutOfBuildAreaPath(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    # throws Exception
    def setClosestGeographicMapCellHistory(self, pathsList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    def teleportTo(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    # throws Exception
    def setLoad(self, resource: int) -> None:
        raise RuntimeError()
    

    # throws Exception
    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    def isSelected(self) -> bool:
        raise RuntimeError()
    

    def shouldAddWaypointFromBuilding(self) -> bool:
        raise RuntimeError()
    

    def isShowMoreCaptionStates(self) -> bool:
        raise RuntimeError()
    

    # throws Exception
    def trackTo(self, reason: str) -> None:
        raise RuntimeError()
    

    # throws Exception
    def trackToDXY(self, dx: int, dy: int) -> None:
        raise RuntimeError()
    

    # throws Exception
    def buildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> bool:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    def getTrackingEvent(self) -> TrackingEvent:
        from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
        raise RuntimeError()
    

    def allStop(self) -> None:
        raise RuntimeError()
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        raise RuntimeError()
    

    # throws Exception
    def getCurrentGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    # throws Exception
    def getTopLeftGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    def getCaptionAnimationHelper(self) -> CaptionAnimationHelperBase:
        from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase
        raise RuntimeError()
    

    def getWaypointBehavior(self) -> WaypointBehaviorBase:
        raise RuntimeError()
    

    def getWaypointLogHelper(self) -> WaypointLogHelper:
        from org.allbinary.game.layer.waypoint.WaypointLogHelper import WaypointLogHelper
        raise RuntimeError()
    

    def getWaypoint2LogHelper(self) -> Waypoint2LogHelper:
        from org.allbinary.game.layer.waypoint.Waypoint2LogHelper import Waypoint2LogHelper
        raise RuntimeError()
    

    def getWaypointRunnableLogHelper(self) -> WaypointRunnableLogHelper:
        from org.allbinary.game.layer.waypoint.WaypointRunnableLogHelper import WaypointRunnableLogHelper
        raise RuntimeError()
    

    def getGroupInterface(self) -> list[Group]:
        from org.allbinary.game.identification.Group import Group
        raise RuntimeError()
    

    # throws Exception
    def isDestroyed(self) -> bool:
        raise RuntimeError()
    

    def getSourceId(self) -> int:
        raise RuntimeError()
# from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase
# from org.allbinary.game.identification.Group import Group
# from org.allbinary.game.layer.waypoint.Waypoint2LogHelper import Waypoint2LogHelper
# from org.allbinary.game.layer.waypoint.WaypointLogHelper import WaypointLogHelper
# from org.allbinary.game.layer.waypoint.WaypointRunnableLogHelper import WaypointRunnableLogHelper
# from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _NullPathFindingLayer_NULL_PATH_FINDING_LAYER() -> object:
    return NullPathFindingLayer()

lazy_static(NullPathFindingLayer, "NULL_PATH_FINDING_LAYER", _NullPathFindingLayer_NULL_PATH_FINDING_LAYER)

