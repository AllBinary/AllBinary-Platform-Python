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
# package org.allbinary.game.layer.unit

from __future__ import annotations

from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
from org.allbinary.game.layer.waypoint.event.WaypointEventListenerInterface import WaypointEventListenerInterface


class UnitWaypointBehavior(WaypointBehaviorBase, WaypointEventListenerInterface):
    PATHING: str = "Pathing"

    def _init_fields(self) -> None:
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.longWeaponRange: int = 0
        self.sensorAction: SensorAction = SensorActionFactory.getInstance().ATTACK
        self.completeTimeDelayHelper: TimeDelayHelper = None
        self.currentGeographicMapCellHistoryP: GeographicMapCellHistory = None
        self.lastPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.currentPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.FAKE_WAYPOINT_LAYER: CollidableDestroyableDamageableLayer = None
        self.targetList: BasicArrayList = None
        self.possibleTargetList: BasicArrayList = None
        self.associatedAdvancedRTSGameLayer: UnitLayer = None
        self.moving: bool = False
        self.movingFromStopped: bool = False
        self.waypointPathsListP: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.currentTargetDistance: int = 2147483647
        self.currentTargetLayerInterfaceP: CollidableDestroyableDamageableLayer = CollidableDestroyableDamageableLayer.getNullInstance()
        self.trackingWaypoint: bool = False
        self.repeatedToLong: TimeDelayHelper = TimeDelayHelper(22000)
    

    def __init__(self, associatedAdvancedRTSGameLayer: UnitLayer, fakeWaypoint: CollidableDestroyableDamageableLayer) -> None:
        super().__init__()
        self._init_fields()
        self.associatedAdvancedRTSGameLayer = associatedAdvancedRTSGameLayer
        self.completeTimeDelayHelper = TimeDelayHelper(30000)
        self.targetList = BasicArrayListD()
        self.possibleTargetList = BasicArrayListD()
        self.setWaypointPathsList(BasicArrayListUtil.getInstance().getImmutableInstance())
        self.currentGeographicMapCellHistoryP = GeographicMapCellHistory()
        self.FAKE_WAYPOINT_LAYER = fakeWaypoint
    

    def initRange(self, weaponRange: int) -> None:
        self.longWeaponRange = int(weaponRange / 2)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onWaypointEvent(self, event: RTSLayerEvent) -> None:
        advancedRTSGameLayer: AdvancedRTSGameLayer = event.getRtsLayer()
        self.associatedAdvancedRTSGameLayer.waypointLogHelperP.onWaypointEvent(self.associatedAdvancedRTSGameLayer, advancedRTSGameLayer)
        if self.associatedAdvancedRTSGameLayer.isSelected():
            self.addWaypointFromUser(advancedRTSGameLayer)
        elif advancedRTSGameLayer.shouldAddWaypointFromBuilding():
            self.addWaypointFromBuilding(advancedRTSGameLayer)
    

    # throws Exception
    def addWaypointFromUser(self, advancedRTSGameLayer: AdvancedRTSGameLayer) -> None:
        pass
    

    # throws Exception
    def addWaypointFromBuilding(self, advancedRTSGameLayer: AdvancedRTSGameLayer) -> None:
        if advancedRTSGameLayer == PrimaryWaypointHelper.getInstance().getWaypointLayer() or advancedRTSGameLayer.getParentLayer() == self.associatedAdvancedRTSGameLayer.getParentLayer():
            if not self.targetList.contains(advancedRTSGameLayer):
                self.associatedAdvancedRTSGameLayer.waypointLogHelperP.addWaypointFromBuilding(self.associatedAdvancedRTSGameLayer, advancedRTSGameLayer)
                if advancedRTSGameLayer.isDestroyed():
                    raise Exception("Trying to add a dead: " + str(advancedRTSGameLayer))
                self.targetList.add(advancedRTSGameLayer)
                self.associatedAdvancedRTSGameLayer.waypointLogHelperP.addWaypointFromBuildingList(self.associatedAdvancedRTSGameLayer, advancedRTSGameLayer, self.targetList)
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        return False
    

    # throws Exception
    def insertWaypoint(self, index: int, rtsLayer: CollidableDestroyableDamageableLayer) -> bool:
        if self.canInsertWaypoint(index, rtsLayer):
            self.associatedAdvancedRTSGameLayer.waypointLogHelperP.insertWaypoint(self.associatedAdvancedRTSGameLayer, index, rtsLayer, self.getName())
            if rtsLayer.isDestroyed():
                raise Exception("Trying to add a dead: " + str(rtsLayer))
            self.targetList.addAt(index, rtsLayer)
            self.associatedAdvancedRTSGameLayer.waypointLogHelperP.insertWaypointList(self.associatedAdvancedRTSGameLayer, index, rtsLayer, self.getName(), self.targetList)
            return True
        return False
    

    def move(self) -> None:
        if self.isMoving():
            self.setMovingFromStopped(False)
        else:
            self.setMovingFromStopped(True)
        self.setMoving(False)
    

    # throws Exception
    def setRandomGeographicMapCellHistory(self, pathsList: BasicArrayList) -> None:
        size: int = pathsList.size()
        self.associatedAdvancedRTSGameLayer.waypointLogHelperP.setRandomGeographicMapCellHistoryList(self.associatedAdvancedRTSGameLayer, pathsList)
        if size > 0:
            geographicMapCellPositionBasicArrayList: BasicArrayList = BasicArrayListUtil.getInstance().getRandom(pathsList)
            self.setGeographicMapCellHistoryPath(geographicMapCellPositionBasicArrayList)
    

    # throws Exception
    def setGeographicMapCellHistoryPath(self, geographicMapCellPositionBasicArrayList: BasicArrayList) -> None:
        self.lastPathGeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        if self.associatedAdvancedRTSGameLayer.showMoreCaptionStates:
            self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(UnitWaypointBehavior.PATHING, BasicColorFactory.getInstance().GREEN)
        self.currentGeographicMapCellHistoryP.init()
        self.associatedAdvancedRTSGameLayer.init(self.currentGeographicMapCellHistoryP, geographicMapCellPositionBasicArrayList)
        self.setTrackingWaypoint(True)
        self.getCompleteTimeDelayHelper().setStartTimeTNT()
    

    def canInsertWaypoint(self, index: int, rtsLayer: CollidableDestroyableDamageableLayer) -> bool:
        if self.targetList.size() > 4:
            pass
        elif self.targetList.contains(rtsLayer):
            pass
        else:
            return True
        return False
    

    # throws Exception
    def addBuildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> None:
        pass
    

    # throws Exception
    def moveAwayFromBuilding(self, buildingLayer: BuildingLayer) -> None:
        geographicMapCellPosition: GeographicMapCellPosition = self.associatedAdvancedRTSGameLayer.getCurrentGeographicMapCellPosition()
        list_: BasicArrayList = buildingLayer.geographicMapCellPositionAreaBase.getOccupyingGeographicMapCellPositionList()
        if list_.contains(geographicMapCellPosition):
            if self.insertWaypoint(0, self.FAKE_WAYPOINT_LAYER):
                self.associatedAdvancedRTSGameLayer.waypointLogHelperP.moveAwayFromBuilding(self.associatedAdvancedRTSGameLayer)
                self.setCurrentTargetLayerInterface(self.FAKE_WAYPOINT_LAYER)
                pathsList: BasicArrayList = buildingLayer.getMoveOutOfBuildAreaPath(geographicMapCellPosition)
                self.associatedAdvancedRTSGameLayer.setClosestGeographicMapCellHistory(pathsList)
    

    def needToMove(self) -> bool:
        self.associatedAdvancedRTSGameLayer.waypointLogHelperP.needToMove(self.associatedAdvancedRTSGameLayer, self)
        if self.isTrackingWaypoint() or self.sensorAction == SensorActionFactory.getInstance().EVADE or (self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance() and self.getCurrentTargetDistance() >= self.longWeaponRange + self.currentTargetLayerInterfaceP.getHalfHeight()):
            self.repeatedToLong.setStartTimeTNT()
            return True
        if self.repeatedToLong.isTimeTNT():
            message: str = "Repeating too long: " + str(self.getMovementLogicAsString())
            ForcedLogUtil.log(message, self.associatedAdvancedRTSGameLayer)
        return False
    

    def getMovementLogicAsString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("isTrackingWaypoint: ")
        stringBuffer.appendboolean(self.isTrackingWaypoint())
        stringBuffer.append(" sensorAction: ")
        stringBuffer.append(self.sensorAction.name)
        stringBuffer.append(" getCurrentTargetLayerInterface: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.currentTargetLayerInterfaceP))
        if self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance():
            stringBuffer.append(" Target Range: ")
            stringBuffer.appendint(self.getCurrentTargetDistance())
            stringBuffer.append(" >= ")
            stringBuffer.appendint(int(self.longWeaponRange + self.currentTargetLayerInterfaceP.getHalfHeight()))
        return str(stringBuffer)
    

    def isMovingFromStopped(self) -> bool:
        return self.movingFromStopped
    

    def setMovingFromStopped(self, movingFromStopped: bool) -> None:
        self.movingFromStopped = movingFromStopped
    

    def setWaypointPathsList(self, waypointPathsList: BasicArrayList) -> None:
        self.waypointPathsListP = waypointPathsList
    

    def getWaypointPathsList(self) -> BasicArrayList:
        return self.waypointPathsListP
    

    def isMoving(self) -> bool:
        return self.moving
    

    def setMoving(self, moving: bool) -> None:
        self.moving = moving
    

    def isTrackingWaypoint(self) -> bool:
        return self.trackingWaypoint
    

    def getPossibleTargetList(self) -> BasicArrayList:
        return self.possibleTargetList
    

    def setLastPathGeographicMapCellPosition(self, lastPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.lastPathGeographicMapCellPosition = lastPathGeographicMapCellPosition
    

    def getLastPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.lastPathGeographicMapCellPosition
    

    def setCurrentPathGeographicMapCellPosition(self, currentPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.currentPathGeographicMapCellPosition = currentPathGeographicMapCellPosition
    

    def getCurrentPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.currentPathGeographicMapCellPosition
    

    def setSensorAction(self, sensorAction: SensorAction) -> None:
        self.sensorAction = sensorAction
    

    def getSensorAction(self) -> SensorAction:
        return self.sensorAction
    

    def setCurrentTargetLayerInterface(self, currentTargetLayerInterface: CollidableDestroyableDamageableLayer) -> None:
        self.currentTargetLayerInterfaceP = currentTargetLayerInterface
    

    def getCurrentTargetLayerInterface(self) -> CollidableDestroyableDamageableLayer:
        return self.currentTargetLayerInterfaceP
    

    def setCurrentTargetDistance(self, currentTargetDistance: int) -> None:
        self.currentTargetDistance = currentTargetDistance
    

    def getCurrentTargetDistance(self) -> int:
        return self.currentTargetDistance
    

    def getCompleteTimeDelayHelper(self) -> TimeDelayHelper:
        return self.completeTimeDelayHelper
    

    def getCurrentGeographicMapCellHistory(self) -> GeographicMapCellHistory:
        return self.currentGeographicMapCellHistoryP
    

    def setTrackingWaypoint(self, trackingWaypoint: bool) -> None:
        self.trackingWaypoint = trackingWaypoint
from org.allbinary.game.input.form.PrimaryWaypointHelper import PrimaryWaypointHelper
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.SensorAction import SensorAction
from org.allbinary.game.layer.SensorActionFactory import SensorActionFactory
from org.allbinary.game.layer.building.BuildingLayer import BuildingLayer
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


