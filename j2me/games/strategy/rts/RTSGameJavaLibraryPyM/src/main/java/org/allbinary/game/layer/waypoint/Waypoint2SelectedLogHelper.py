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

from org.allbinary.game.layer.waypoint.Waypoint2LogHelper import Waypoint2LogHelper


class Waypoint2SelectedLogHelper(Waypoint2LogHelper):
    instanceC: Waypoint2SelectedLogHelper = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.positionStrings: PositionStrings = PositionStrings.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.ENEMY_POSSIBLE_TARGET: str = " Enemy Possible Target: "
        self.CLOSE_RANGE: str = "closeRange: "
        self.SENSOR_RANGE: str = " sensorRange: "
        self.ONLY_TARGETS: str = " Only Targets: "
        self.SHORTER_THAN_CURRENT_TARGET_DISTANCE: str = " isShorterThanCurrentTargetDistance: "
        self.CURRENT_TARGET_DESTROYED: str = " isCurrentTargetDestroyed: "
        self.CURRENT_TARGET_NOT_AVAILABLE: str = " isCurrentTargetNotAvailable: "
        self.PROCESS_POSSIBLE_TARGET: str = "selected: processPossibleTarget1"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> Waypoint2LogHelper:
        return Waypoint2SelectedLogHelper.instanceC
    

    def initRange(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, closeRange: int, sensorRange: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.CLOSE_RANGE)
        stringBuffer.appendint(closeRange)
        stringBuffer.append(self.SENSOR_RANGE)
        stringBuffer.appendint(sensorRange)
        self.logUtil.putF(str(stringBuffer), self, "selected: initRange")
    

    def processPossibleTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int, isShorterThanCurrentTargetDistance: bool, isCurrentTargetDestroyed: bool) -> None:
        if waypointBehaviorBase.isWaypointListEmptyOrOnlyTargets() and waypointBehaviorBase.isInSensorRange(layerInterface, anotherTargetDistance):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
            stringBuffer.append(self.ONLY_TARGETS)
            stringBuffer.appendboolean(waypointBehaviorBase.isWaypointListEmptyOrOnlyTargets())
            stringBuffer.append(self.SHORTER_THAN_CURRENT_TARGET_DISTANCE)
            stringBuffer.appendboolean(isShorterThanCurrentTargetDistance)
            stringBuffer.append(self.CURRENT_TARGET_DESTROYED)
            stringBuffer.appendboolean(isCurrentTargetDestroyed)
            stringBuffer.append(self.CURRENT_TARGET_NOT_AVAILABLE)
            stringBuffer.appendboolean((waypointBehaviorBase.getCurrentTargetLayerInterface() is None))
            self.logUtil.putF(str(stringBuffer), self, self.PROCESS_POSSIBLE_TARGET)
    

    def processSetTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(waypointBehaviorBase.getCurrentTargetingStateString())
        stringBuffer.append(self.ENEMY_POSSIBLE_TARGET)
        stringBuffer.append(layerInterface.getName())
        stringBuffer.append(" anotherTargetDistance: ")
        stringBuffer.appendint(anotherTargetDistance)
        self.logUtil.putF(str(stringBuffer), self, "selected: processPossibleTarget2")
    

    def processPossibleTargetCloser(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(waypointBehaviorBase.getCurrentTargetingStateString())
        stringBuffer.append(self.ENEMY_POSSIBLE_TARGET)
        stringBuffer.append(layerInterface.getName())
        stringBuffer.append(" anotherTargetDistance: ")
        stringBuffer.appendint(anotherTargetDistance)
        self.logUtil.putF(str(stringBuffer), self, "selected: processPossibleTarget3")
    

    def setTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase, layerInterface: PathFindingLayerInterface, anotherTargetDistance: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(waypointBehaviorBase.getName())
        stringBuffer.append(" targeting: ")
        stringBuffer.append(layerInterface.getName())
        stringBuffer.append(" at: ")
        stringBuffer.appendint(anotherTargetDistance)
        stringBuffer.append(" instead of: ")
        stringBuffer.append(waypointBehaviorBase.getCurrentTargetingStateString())
        self.logUtil.putF(str(stringBuffer), self, "selected: setTarget")
    

    def setTargetPath(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF("Target Destroyed", self, "selected: setTargetPath")
    

    def setTargetPathIgnoreNewPath(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Set Path To Target: ")
        stringBuffer.append(waypointBehaviorBase.getCurrentTargetLayerInterface().getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.stringUtil.toString(waypointBehaviorBase.getCurrentTargetLayerInterface()))
        self.logUtil.putF(str(stringBuffer), self, "selected: setTargetPath")
    

    def processWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase, targetLayer: PathFindingLayerInterface, size: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Size: ")
        stringBuffer.appendint(size)
        stringBuffer.append(" Waypoint: ")
        stringBuffer.append(targetLayer.getName())
        stringBuffer.append(" Target: ")
        stringBuffer.append(self.stringUtil.toString(waypointBehaviorBase.getCurrentTargetLayerInterface()))
        stringBuffer.append(" isTrackingWaypoint: ")
        stringBuffer.appendboolean(waypointBehaviorBase.isTrackingWaypoint())
        stringBuffer.append(" WaypointOverridesAttacking: ")
        stringBuffer.appendboolean(waypointBehaviorBase.isWaypointOverridesAttacking())
        self.logUtil.putF(str(stringBuffer), self, "selected: processWaypoint")
    

    def processWaypointTracked(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, waypointBehaviorBase: WaypointBehaviorBase) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" currentPathGeographicMapCellPosition: ")
        stringBuffer.append(self.stringUtil.toString(waypointBehaviorBase.getCurrentPathGeographicMapCellPosition()))
        stringBuffer.append(" nextUnvisitedPathGeographicMapCellPosition: ")
        stringBuffer.append(self.stringUtil.toString(waypointBehaviorBase.getNextUnvisitedPathGeographicMapCellPosition()))
        stringBuffer.append(" Tracked: ")
        stringBuffer.append(self.stringUtil.toString(waypointBehaviorBase.getCurrentGeographicMapCellHistory().getTracked()))
        self.logUtil.putF(str(stringBuffer), self, "selected: processWaypoint")
    

    def processWaypointTrackedVisit(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Visited: ")
        stringBuffer.append(self.stringUtil.toString(geographicMapCellPosition))
        self.logUtil.putF(str(stringBuffer), self, "selected: processWaypoint")
    

    def processWaypointTrackedWithoutProgress(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, reason: str) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(reason)), self, "turnTo")
    

    def wander(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(associatedAdvancedRTSGameLayer.getName(), self, "wander")
    

    def targetDestroyed(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" Target Destroyed")), self, "selected: processTargeting")
    

    def processTargeting(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, dx: int, dy: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.positionStrings.DX_LABEL)
        stringBuffer.appendint(dx)
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.positionStrings.DY_LABEL)
        stringBuffer.appendint(dy)
        self.logUtil.putF(str(stringBuffer), self, "selected: processTargeting")
    

    def processTargetingNonWayPoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, dx: int, dy: int) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Targeting Non Waypoint ")
        stringBuffer.append(self.positionStrings.DX_LABEL)
        stringBuffer.appendint(dx)
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(self.positionStrings.DY_LABEL)
        stringBuffer.appendint(dy)
        self.logUtil.putF(str(stringBuffer), self, "selected: processTargeting")
    

    def removeWaypoint(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, waypointLayer: PathFindingLayerInterface, reason: str) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(unitWaypointBehavior2.getName())
        stringBuffer.append(" remove: ")
        stringBuffer.append(waypointLayer.getName())
        stringBuffer.append(" because: ")
        stringBuffer.append(reason)
        self.logUtil.putF(str(stringBuffer), self, "selected: removeWaypoint")
    

    def removeWaypointList(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, unitWaypointBehavior2: WaypointBehaviorBase, list_: BasicArrayList) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(self.commonSeps.SPACE)
        stringBuffer.append(unitWaypointBehavior2.getName())
        stringBuffer.append(" Waypoints: ")
        stringBuffer.append(self.stringUtil.toString(list_))
        self.logUtil.putF(str(stringBuffer), self, "selected: removeWaypoint")
    

    def removeWaypointClear(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" Clearing removed waypoint")), self, "selected: removeWaypoint")
    

    def clearTarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" Cleared Target")), self, "selected: clearTarget")
    

    def addWaypointFromUser(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface, advancedRTSGameLayer: PathFindingLayerInterface) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(associatedAdvancedRTSGameLayer.getName())
        stringBuffer.append(" Adding Waypoint to Selected: ")
        stringBuffer.append(advancedRTSGameLayer.getName())
        if advancedRTSGameLayer.getParentLayer() is not None:
            stringBuffer.append(" With Parent: ")
            stringBuffer.append(advancedRTSGameLayer.getParentLayer().getName())
        self.logUtil.putF(str(stringBuffer), self, "selected: onWaypointEvent")
    

    def targetMovedSoRetarget(self, associatedAdvancedRTSGameLayer: PathFindingLayerInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(associatedAdvancedRTSGameLayer.getName()).append(" - target moved so retargeting")), self, "turnTo")
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.util.BasicArrayList import BasicArrayList


Waypoint2SelectedLogHelper.instanceC = Waypoint2SelectedLogHelper()

