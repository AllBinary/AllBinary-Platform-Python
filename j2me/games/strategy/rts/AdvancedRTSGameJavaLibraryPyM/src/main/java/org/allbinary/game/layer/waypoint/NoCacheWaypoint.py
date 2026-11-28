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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.layer.building.event.BuildingEventListenerInterface import BuildingEventListenerInterface
from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase


@java_inherited_overloads
class NoCacheWaypoint(*java_bases(WaypointBase, BuildingEventListenerInterface)):
    def _java_defaults(self):
        vars(self).setdefault("ownerLayer", None)

    def _init_fields(self) -> None:
        if "ownerLayer" not in vars(self): self.ownerLayer: PathFindingLayerInterface = None
    

    def __init__(self, ownerLayer: PathFindingLayerInterface, sound: Sound) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.media.audio.Sound import Sound
        super().__init__(sound)
        __class__._init_fields(self)
        self.ownerLayer = ownerLayer
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        java_super_call(super(), "setAllBinaryGameLayerManager", allBinaryGameLayerManager)
    

    def releaseCachedPaths(self) -> None:
        pass
    

    # throws Exception
    def getPathsListFromCacheOnly(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        return BasicArrayListUtil.getInstance().getImmutableInstance()
    

    # throws Exception
    def getPathsListRunnable(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.createPaths(geographicMapCellPosition)
    

    # throws Exception
    def getEndGeographicMapCellPosition(self, startGeographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        endList: BasicArrayList = self.ownerLayer.getEndGeographicMapCellPositionList()
        endGeographicMapCellPosition: GeographicMapCellPosition = BasicArrayListUtil.getInstance().getRandom(endList)
        if startGeographicMapCellPosition == endGeographicMapCellPosition:
            for index in range(endList.size() - 1, 0 - 1, -1):
                endGeographicMapCellPosition = endList.get(index)
                if startGeographicMapCellPosition != endGeographicMapCellPosition:
                    break
        return endGeographicMapCellPosition
    

    # throws Exception
    def createPaths(self, startGeographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        from org.allbinary.game.media.graphics.geography.map.racetrack.PathFindingInfoFactory import PathFindingInfoFactory
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
        from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
        from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGenerator import CustomMapGenerator
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMap import RaceTrackGeographicMap
        from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
        from org.allbinary.media.graphics.geography.pathfinding.PathGenerator import PathGenerator
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        endGeographicMapCellPosition: GeographicMapCellPosition = self.getEndGeographicMapCellPosition(startGeographicMapCellPosition)
        if endGeographicMapCellPosition is None:
            return BasicArrayListUtil.getInstance().getImmutableInstance()
        if startGeographicMapCellPosition == endGeographicMapCellPosition:
            if self.ownerLayer.shouldHandleStartSameAsEnd():
                return BasicArrayListUtil.getInstance().getImmutableInstance()
            else:
                raise Exception("Start should not be End: " + str(endGeographicMapCellPosition))
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        raceTrackGeographicMap: RaceTrackGeographicMap = geographicMapInterface
        raceTrackGeographicMapCellTypeFactory: GeographicMapCellTypeFactory = raceTrackGeographicMap.getGeographicMapCellTypeFactory()
        customMapGenerator: CustomMapGenerator = raceTrackGeographicMap.getCustomMapGenerator()
        customMapGenerator.copyMapIntoCustomMap()
        customMapArray: list[list[int]] = customMapGenerator.getCustomMapArray()
        customMapArray[startGeographicMapCellPosition.getRow()][startGeographicMapCellPosition.getColumn()] = raceTrackGeographicMapCellTypeFactory.getStartType()
        customMapArray[endGeographicMapCellPosition.getRow()][endGeographicMapCellPosition.getColumn()] = raceTrackGeographicMapCellTypeFactory.getEndType()
        pathFindingInfo: PathFindingInfo = PathFindingInfoFactory.getInstance().getInstancePathFindingInfo(raceTrackGeographicMap, customMapArray)
        list_: BasicArrayList = PathGenerator.getInstance().getInstanceNoCache(geographicMapInterface, pathFindingInfo, 2)
        if list_.size() < 1:
            raise Exception("Path may have been cleared by clearing caching")
        return list_
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onBuildingEvent(self, event: RTSLayerEvent) -> None:
        from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
        pass
    

    def reset(self) -> None:
        self.getConnectedWaypointList().clear()
    

    # throws Exception
    def visit(self, unitLayer: PathFindingLayerInterface) -> None:
        from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
        if unitLayer.getGroupInterface()[0] != self.ownerLayer.getGroupInterface()[0]:
            return
        size: int = self.getConnectedWaypointList().size()
        if size > 0:
            unitWaypointBehavior: UnitWaypointBehavior = unitLayer.getWaypointBehavior()
            while self.getConnectedWaypointList().size() > 0:
                rtsLayer: CollidableDestroyableDamageableLayer = self.getConnectedWaypointList().get(0)
                if java_predicate(rtsLayer, "isDestroyed"):
                    self.getConnectedWaypointList().remove(rtsLayer)
                else:
                    unitLayer.handleCost(self.ownerLayer)
                    unitWaypointBehavior.insertWaypoint(0, rtsLayer)
                    break
# from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
# from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
# from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
# from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
# from org.allbinary.game.media.graphics.geography.map.racetrack.PathFindingInfoFactory import PathFindingInfoFactory
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.util.event.EventStrings import EventStrings
# from org.allbinary.media.audio.Sound import Sound
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
# from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
# from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGenerator import CustomMapGenerator
# from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMap import RaceTrackGeographicMap
# from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
# from org.allbinary.media.graphics.geography.pathfinding.PathGenerator import PathGenerator
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


