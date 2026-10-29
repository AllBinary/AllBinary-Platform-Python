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

from org.allbinary.game.layer.building.event.BuildingEventListenerInterface import BuildingEventListenerInterface
from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase


class MultipassNoCacheWaypoint(WaypointBase, BuildingEventListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.ownerLayer: PathFindingLayerInterface = None
    

    def __init__(self, ownerLayer: PathFindingLayerInterface, sound: Sound) -> None:
        super().__init__(sound)
        self._init_fields()
        self.ownerLayer = ownerLayer
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
    

    def releaseCachedPaths(self) -> None:
        pass
    

    # throws Exception
    def getPathFindingInfo(self, geographicMapCellPosition: GeographicMapCellPosition) -> PathFindingInfo:
        startGeographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPosition
        endGeographicMapCellPosition: GeographicMapCellPosition = self.getEndGeographicMapCellPosition(startGeographicMapCellPosition)
        if endGeographicMapCellPosition is None:
            return PathFindingInfo.NULL_PATH_FINDING_INFO
        if startGeographicMapCellPosition == endGeographicMapCellPosition:
            if self.ownerLayer.shouldHandleStartSameAsEnd():
                return PathFindingInfo.NULL_PATH_FINDING_INFO
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
        return pathFindingInfo
    

    # throws Exception
    def getPathsList(self, geographicMapCellPosition: GeographicMapCellPosition, pathFindingInfo: PathFindingInfo, multipassState: MultipassState) -> BasicArrayList:
        try:
            if pathFindingInfo is None:
                self.logUtil.putF("pathFindingInfo: " + str(pathFindingInfo), self, "getPathsList")
                return BasicArrayListUtil.getInstance().getImmutableInstance()
            geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            list_: BasicArrayList = PathGenerator.getInstance().createN(geographicMapInterface, pathFindingInfo, 2, multipassState)
            if list_ is not None and list_ != BasicArrayListUtil.getInstance().getImmutableInstance():
                if list_.size() < 1:
                    raise Exception("Path may have been cleared by clearing caching")
                return list_
            return BasicArrayListUtil.getInstance().getImmutableInstance()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "getPathsList", e)
            return BasicArrayListUtil.getInstance().getImmutableInstance()
    

    # throws Exception
    def getEndGeographicMapCellPosition(self, startGeographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        endList: BasicArrayList = self.ownerLayer.getEndGeographicMapCellPositionList()
        endGeographicMapCellPosition: GeographicMapCellPosition = BasicArrayListUtil.getInstance().getRandom(endList)
        if startGeographicMapCellPosition == endGeographicMapCellPosition:
            for index in range(endList.size() - 1, 0 - 1, -1):
                endGeographicMapCellPosition = endList.get(index)
                if startGeographicMapCellPosition != endGeographicMapCellPosition:
                    break
        return endGeographicMapCellPosition
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onBuildingEvent(self, event: RTSLayerEvent) -> None:
        pass
    

    def reset(self) -> None:
        self.getConnectedWaypointList().clear()
    

    # throws Exception
    def visit(self, unitLayer: PathFindingLayerInterface) -> None:
        if unitLayer.getGroupInterface()[0] != self.ownerLayer.getGroupInterface()[0]:
            return
        size: int = self.getConnectedWaypointList().size()
        if size > 0:
            unitWaypointBehavior: UnitWaypointBehavior = unitLayer.getWaypointBehavior()
            while self.getConnectedWaypointList().size() > 0:
                rtsLayer: CollidableDestroyableDamageableLayer = self.getConnectedWaypointList().get(0)
                if rtsLayer.isDestroyed():
                    self.getConnectedWaypointList().remove(rtsLayer)
                else:
                    unitLayer.handleCost(self.ownerLayer)
                    unitWaypointBehavior.insertWaypoint(0, rtsLayer)
                    break
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
from org.allbinary.game.media.graphics.geography.map.racetrack.PathFindingInfoFactory import PathFindingInfoFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGenerator import CustomMapGenerator
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMap import RaceTrackGeographicMap
from org.allbinary.media.graphics.geography.pathfinding.MultipassState import MultipassState
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathGenerator import PathGenerator
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


