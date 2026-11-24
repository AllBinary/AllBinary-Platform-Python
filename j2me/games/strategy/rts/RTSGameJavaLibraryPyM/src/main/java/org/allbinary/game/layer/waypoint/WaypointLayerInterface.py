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



# Java interface
class WaypointLayerInterface:
    

    # throws Exception
    def init(self, geographicMapCellHistory: GeographicMapCellHistory, geographicMapCellPositionBasicArrayList: BasicArrayList) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def getMoveOutOfBuildAreaPath(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    # throws Exception
    def setClosestGeographicMapCellHistory(self, pathsList: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def teleportTo(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
    

    # throws Exception
    def setLoad(self, resource: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def isSelected(self) -> bool:
        raise NotImplementedError()
    

    def shouldAddWaypointFromBuilding(self) -> bool:
        raise NotImplementedError()
    

    def isShowMoreCaptionStates(self) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def trackTo(self, reason: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def trackToDXY(self, dx: int, dy: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def buildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> bool:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
    

    def getTrackingEvent(self) -> TrackingEvent:
        from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
        raise NotImplementedError()
    

    def allStop(self) -> None:
        raise NotImplementedError()
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def getCurrentGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
    

    # throws Exception
    def getTopLeftGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
    

    def getCaptionAnimationHelper(self) -> CaptionAnimationHelperBase:
        from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase
        raise NotImplementedError()
    

    def getWaypointBehavior(self) -> WaypointBehaviorBase:
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        raise NotImplementedError()
    

    def getWaypointLogHelper(self) -> WaypointLogHelper:
        raise NotImplementedError()
    

    def getWaypoint2LogHelper(self) -> Waypoint2LogHelper:
        raise NotImplementedError()
    

    def getWaypointRunnableLogHelper(self) -> WaypointRunnableLogHelper:
        raise NotImplementedError()
# from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase
# from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
# from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayList import BasicArrayList


