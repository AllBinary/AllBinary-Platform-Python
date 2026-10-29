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


class Waypoint(WaypointBase, BuildingEventListenerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.ownerLayer: PathFindingLayerInterface = None
        self.endList: BasicArrayList = self.basicArrayListUtil.getImmutableInstance()
        self.paths: list[list[BasicArrayList]] = self.basicArrayListUtil.NULL_ARRAY_OF_ARRAY
    

    def __init__(self, ownerLayer: PathFindingLayerInterface, sound: Sound) -> None:
        super().__init__(sound)
        self._init_fields()
        self.ownerLayer = ownerLayer
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        if self.paths != self.basicArrayListUtil.NULL_ARRAY_OF_ARRAY:
            raise RuntimeError()
        self.endList = self.ownerLayer.getEndGeographicMapCellPositionList()
        self.paths = [[None] * (tiledLayer.getRows()) for _ in range(tiledLayer.getColumns())]
        self.clearPaths()
    

    def releaseCachedPaths(self) -> None:
        columnIndex = len(self.paths)
        while (columnIndex := columnIndex - 1) >= 0:
            rowIndex = len(self.paths)
            while (rowIndex := rowIndex - 1) >= 0:
                pathsList: BasicArrayList = self.paths[columnIndex][rowIndex]
                if pathsList != self.basicArrayListUtil.getImmutableInstance():
                    BasicGeographicMapExtractedPathsCacheFactory.getInstance().release(pathsList)
    

    # throws Exception
    def getPathsListFromCacheOnly(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        return self.paths[geographicMapCellPosition.getColumn()][geographicMapCellPosition.getRow()]
    

    # throws Exception
    def getPathsListRunnable(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        pathsList: BasicArrayList = self.paths[geographicMapCellPosition.getColumn()][geographicMapCellPosition.getRow()]
        if pathsList == self.basicArrayListUtil.getImmutableInstance():
            pathsList = self.createPaths(geographicMapCellPosition)
            self.paths[geographicMapCellPosition.getColumn()][geographicMapCellPosition.getRow()] = pathsList
        return pathsList
    

    def getEndGeographicMapCellPosition(self, startGeographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        endGeographicMapCellPosition: GeographicMapCellPosition = self.basicArrayListUtil.getRandom(self.endList)
        if startGeographicMapCellPosition == endGeographicMapCellPosition:
            for index in range(self.endList.size() - 1, 0 - 1, -1):
                endGeographicMapCellPosition = self.endList.get(index)
                if startGeographicMapCellPosition != endGeographicMapCellPosition:
                    break
        return endGeographicMapCellPosition
    

    # throws Exception
    def createPaths(self, startGeographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        if self.endList.size() == 0:
            return self.basicArrayListUtil.getImmutableInstance()
        endGeographicMapCellPosition: GeographicMapCellPosition = self.getEndGeographicMapCellPosition(startGeographicMapCellPosition)
        if endGeographicMapCellPosition is None:
            return self.basicArrayListUtil.getImmutableInstance()
        if startGeographicMapCellPosition == endGeographicMapCellPosition:
            if self.ownerLayer.shouldHandleStartSameAsEnd():
                return self.basicArrayListUtil.getImmutableInstance()
            else:
                raise Exception("Start should not be End: " + str(self.endList.size()))
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
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onBuildingEvent(self, event: RTSLayerEvent) -> None:
        self.clearPaths()
    

    def clearPaths(self) -> None:
        columnIndex = len(self.paths)
        while (columnIndex := columnIndex - 1) >= 0:
            rowIndex = len(self.paths)
            while (rowIndex := rowIndex - 1) >= 0:
                self.paths[columnIndex][rowIndex] = self.basicArrayListUtil.getImmutableInstance()
    

    def reset(self) -> None:
        self.getConnectedWaypointList().clear()
        self.releaseCachedPaths()
    

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
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior
from org.allbinary.game.media.graphics.geography.map.racetrack.PathFindingInfoFactory import PathFindingInfoFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.racetrack.CustomMapGenerator import CustomMapGenerator
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMap import RaceTrackGeographicMap
from org.allbinary.media.graphics.geography.pathfinding.BasicGeographicMapExtractedPathsCacheFactory import BasicGeographicMapExtractedPathsCacheFactory
from org.allbinary.media.graphics.geography.pathfinding.PathFindingInfo import PathFindingInfo
from org.allbinary.media.graphics.geography.pathfinding.PathGenerator import PathGenerator
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


