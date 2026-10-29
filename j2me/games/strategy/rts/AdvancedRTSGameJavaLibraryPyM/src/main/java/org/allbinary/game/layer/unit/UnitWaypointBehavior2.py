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

from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.layer.unit.UnitWaypointBehavior import UnitWaypointBehavior


class UnitWaypointBehavior2(UnitWaypointBehavior):
    runningWaypointPathList: BasicArrayList = BasicArrayListD()
    TARGET_DISTANCE: str = "Target Distance"
    TARGET_LAYER: str = "Target Layer"
    class BuildingSteeringVisitor(SteeringVisitor):

        def _init_fields(self) -> None:
            self.positionList: BasicArrayList = BasicArrayListD()

        def __init__(self) -> None:
            super().__init__()
            self._init_fields()
        

        def visit(self, anyType: object) -> object:
            logUtil: LogUtil = LogUtil.getInstance()
            try:
                if self.getList().size() > 0:
                    allbinaryLayer: AllBinaryLayer = self.getList().get(0)
                    cellPosition: GeographicMapCellPosition = self.getPositionList().get(0)
                    clear: bool = self.buildingChase(allbinaryLayer, cellPosition)
                    if clear:
                        self.getList().clear()
                        self.positionList.clear()
                        return NullUtil.getInstance().NULL_OBJECT
                    return BooleanFactory.getInstance().FALSE
                return NullUtil.getInstance().NULL_OBJECT
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, self, "visit", e)
                return NullUtil.getInstance().NULL_OBJECT
        

        def getPositionList(self) -> BasicArrayList:
            return self.positionList

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.unitWaypointStrings: UnitWaypointStrings = UnitWaypointStrings.getInstance()
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.layerDistanceUtil: LayerDistanceUtil = LayerDistanceUtil.getInstance()
        self.pathFindingThreadPool: ThreadPool = PathFindingThreadPool.getInstance()
        self.progressTimeDelayHelper: TimeDelayHelper = None
        self.wanderPathsList: BasicArrayList = None
        self.waypointPathRunnable: WaypointPathRunnableBase = None
        self.sensorRange: int = 0
        self.closeRange: int = 0
        self.nextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.afterNextUnvisitedPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.waitingOnTargetPath: bool = False
        self.waitingOnWaypointPath: bool = False
        self.targetWithoutCachedPathLayerInterface: CollidableDestroyableDamageableLayer = CollidableDestroyableDamageableLayer.getNullInstance()
        self.buildingSteeringVisitor: BuildingSteeringVisitor = BuildingSteeringVisitor()
    

    def __init__(self, ownerAdvancedRTSGameLayer: UnitLayer, fakeWaypoint: AdvancedRTSGameLayer) -> None:
        super().__init__(ownerAdvancedRTSGameLayer, fakeWaypoint)
        self._init_fields()
        self.progressTimeDelayHelper = TimeDelayHelper(5000)
        self.wanderPathsList = BasicArrayListD()
        features: Features = Features.getInstance()
        self.waypointPathRunnable = (MultipassWaypointPathRunnable() if J2MEUtil.isHTML() else WaypointPathRunnable())
    

    def initRange(self, weaponRange: int) -> None:
        super().initRange(weaponRange)
        self.closeRange = weaponRange
        self.sensorRange = weaponRange * 4
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.initRange(self.associatedAdvancedRTSGameLayer, self.closeRange, self.sensorRange)
    

    def getNextUnvisitedPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.nextUnvisitedPathGeographicMapCellPosition
    

    def isRunning(self) -> bool:
        if self.waypointPathRunnable.isRunning():
            return True
        else:
            return False
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.waypointPathRunnable.isRunning():
            if self.waypointPathsListP != UnitWaypointBehavior2.runningWaypointPathList:
                self.waypointPathRunnable.setRunning(False)
                if self.waitingOnTargetPath:
                    self.setTargetPath()
                elif self.waitingOnWaypointPath:
                    self.setWaypointPath(self.waypointPathRunnable.getTargetLayer())
                else:
                    raise Exception("Should not happen")
            else:
                return
        self.processTargetList()
        if not self.waypointPathRunnable.isRunning():
            self.processWaypoint()
        else:
            return
        if not self.waypointPathRunnable.isRunning():
            self.processTargeting()
        else:
            return
        if not self.waypointPathRunnable.isRunning():
            self.teleportIfNoProgress()
        else:
            return
    

    # throws Exception
    def onEnemyMovement(self, layerInterface: AdvancedRTSGameLayer) -> None:
        anotherTargetDistance: int = self.layerDistanceUtil.getDistance(self.associatedAdvancedRTSGameLayer, layerInterface)
        if layerInterface == self.currentTargetLayerInterfaceP:
            self.setCurrentTargetDistance(anotherTargetDistance)
        else:
            self.processPossibleTarget(layerInterface, anotherTargetDistance)
    

    # throws Exception
    def processPossibleTarget(self, layerInterface: AdvancedRTSGameLayer, anotherTargetDistance: int) -> None:
        isShorterThanCurrentTargetDistance: bool = self.getCurrentTargetDistance() > anotherTargetDistance
        isCurrentTargetDestroyed: bool = self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance() and self.currentTargetLayerInterfaceP.isDestroyed()
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processPossibleTarget(self.associatedAdvancedRTSGameLayer, self, layerInterface, anotherTargetDistance, isShorterThanCurrentTargetDistance, isCurrentTargetDestroyed)
        if self.isWaypointListEmptyOrOnlyTargets() and self.isInSensorRange(layerInterface, anotherTargetDistance) and (isShorterThanCurrentTargetDistance or isCurrentTargetDestroyed):
            self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processSetTarget(self.associatedAdvancedRTSGameLayer, self, layerInterface, anotherTargetDistance)
            self.setTarget(layerInterface, anotherTargetDistance)
        elif self.isCloseRange(layerInterface, anotherTargetDistance) and (isShorterThanCurrentTargetDistance or isCurrentTargetDestroyed):
            self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processPossibleTargetCloser(self.associatedAdvancedRTSGameLayer, self, layerInterface, anotherTargetDistance)
            self.setTarget(layerInterface, anotherTargetDistance)
    

    # throws Exception
    def teleportIfNoProgress(self) -> None:
        if self.isTrackingWaypoint() or self.associatedAdvancedRTSGameLayer.getParentLayer().isDestroyed():
            if self.progressTimeDelayHelper.isTimeTNT() and self.nextUnvisitedPathGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
                self.associatedAdvancedRTSGameLayer.teleportTo(self.nextUnvisitedPathGeographicMapCellPosition)
            if self.getCompleteTimeDelayHelper().isTimeTNT():
                geographicMapCellPosition: GeographicMapCellPosition = self.currentGeographicMapCellHistoryP.getTracked().get(self.currentGeographicMapCellHistoryP.getSize() - 1)
                self.associatedAdvancedRTSGameLayer.teleportTo(geographicMapCellPosition)
    

    # throws Exception
    def setTarget(self, layerInterface: AdvancedRTSGameLayer, anotherTargetDistance: int) -> None:
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.setTarget(self.associatedAdvancedRTSGameLayer, self, layerInterface, anotherTargetDistance)
        self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.TARGET, BasicColorFactory.getInstance().GREEN)
        self.associatedAdvancedRTSGameLayer.setLoad(0)
        self.setCurrentTargetDistance(anotherTargetDistance)
        self.setCurrentTargetLayerInterface(layerInterface)
        self.setTrackingWaypoint(False)
        self.targetList.clear()
        if not self.isCloseRange(layerInterface, anotherTargetDistance) and self.canInsertWaypoint(0, self.currentTargetLayerInterfaceP):
            geographicMapCellPosition: GeographicMapCellPosition = self.associatedAdvancedRTSGameLayer.getCurrentGeographicMapCellPosition()
            pathFindingLayerInterface: PathFindingLayerInterface = (self.currentTargetLayerInterfaceP)
            waypoint: WaypointBase = pathFindingLayerInterface.getWaypointBehavior().getWaypoint()
            list_: BasicArrayList = waypoint.getPathsListFromCacheOnly(geographicMapCellPosition)
            self.setWaypointPathsList(list_)
            if self.waypointPathsListP is None:
                self.targetWithoutCachedPathLayerInterface = self.currentTargetLayerInterfaceP
            elif self.waypointPathsListP.size() != 0:
                self.setTargetPath()
    

    # throws Exception
    def setTargetPath(self) -> None:
        if self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance():
            if self.currentTargetLayerInterfaceP.isDestroyed():
                self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.setTargetPath(self.associatedAdvancedRTSGameLayer)
                self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.KILL, self.basicColorFactory.ORANGE)
                self.clearTarget()
                return
            if self.currentTargetLayerInterfaceP == self.waypointPathRunnable.getTargetLayer():
                self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.setTargetPathIgnoreNewPath(self.associatedAdvancedRTSGameLayer, self)
                self.insertWaypoint(0, self.currentTargetLayerInterfaceP)
                self.setRandomGeographicMapCellHistory(self.waypointPathsListP)
    

    # throws Exception
    def setGeographicMapCellHistoryPath(self, geographicMapCellPositionBasicArrayList: BasicArrayList) -> None:
        self.setCurrentPathGeographicMapCellPosition(SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION)
        self.nextUnvisitedPathGeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        super().setGeographicMapCellHistoryPath(geographicMapCellPositionBasicArrayList)
    

    # throws Exception
    def processWaypoint(self) -> None:
        size: int = self.targetList.size()
        if size > 0:
            targetLayer: AdvancedRTSGameLayer = self.targetList.get(0)
            self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processWaypoint(self.associatedAdvancedRTSGameLayer, self, targetLayer, size)
            if targetLayer.isDestroyed():
                self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.WAYPOINT_DESTROYED_SHORT, self.basicColorFactory.YELLOW)
                self.removeWaypoint(targetLayer, self.unitWaypointStrings.WAYPOINT_DESTROYED)
            else:
                geographicMapCellPosition: GeographicMapCellPosition = self.associatedAdvancedRTSGameLayer.getCurrentGeographicMapCellPosition()
                if self.isTrackingWaypoint():
                    self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processWaypointTracked(self.associatedAdvancedRTSGameLayer, self)
                    if self.visitIfAtMidPoint(geographicMapCellPosition):
                        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processWaypointTrackedVisit(self.associatedAdvancedRTSGameLayer, geographicMapCellPosition)
                    if self.currentGeographicMapCellHistoryP.isAllVisited2() and self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance():
                        oldWaypointLayer: AdvancedRTSGameLayer = self.currentTargetLayerInterfaceP
                        oldWaypointLayer.getWaypointBehavior().getWaypoint().visit(self.associatedAdvancedRTSGameLayer)
                        self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.ALL_VISITED_SHORT, self.basicColorFactory.GREEN)
                        self.removeWaypoint(self.currentTargetLayerInterfaceP, self.unitWaypointStrings.ALL_VISITED)
                elif self.currentTargetLayerInterfaceP is None or self.waypointOverridesAttacking:
                    list_: BasicArrayList = targetLayer.getWaypointBehavior().getWaypoint().getPathsListFromCacheOnly(geographicMapCellPosition)
                    self.setWaypointPathsList(list_)
                    if self.waypointPathsListP is None:
                        self.waitingOnWaypointPath = True
                        self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.THINKING, self.basicColorFactory.GREEN)
                        self.runWaypointPathTask(targetLayer)
                        return
                    self.setWaypointPath(targetLayer)
    

    # throws Exception
    def wander(self) -> None:
        if self.currentGeographicMapCellHistoryP.isAllVisited2():
            self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.wander(self.associatedAdvancedRTSGameLayer)
            self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.WANDERING, self.basicColorFactory.RED)
            self.wanderPathsList.clear()
            self.wanderPathsList.add(self.associatedAdvancedRTSGameLayer.getSurroundingGeographicMapCellPositionList())
            self.setRandomGeographicMapCellHistory(self.wanderPathsList)
        self.visitIfAtMidPoint(self.getCurrentPathGeographicMapCellPosition())
        self.updateCurrentPathGeographicMapCellPosition()
        self.associatedAdvancedRTSGameLayer.trackTo(self.unitWaypointStrings.NEXT_PATH_NODE)
    

    def visitIfAtMidPoint(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        unitLayer: UnitLayer = self.associatedAdvancedRTSGameLayer
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and self.nextUnvisitedPathGeographicMapCellPosition == geographicMapCellPosition:
            point: GPoint = geographicMapCellPosition.getMidPoint()
            afterNextPoint: GPoint = self.afterNextUnvisitedPathGeographicMapCellPosition.getMidPoint()
            beyondMidPoint: bool = True
            if geographicMapCellPosition.getColumn() == self.afterNextUnvisitedPathGeographicMapCellPosition.getColumn():
                pass
            elif point.getX() < afterNextPoint.getX():
                if unitLayer.getXP() + unitLayer.getHalfWidth() < point.getX():
                    beyondMidPoint = False
            else:
                if unitLayer.getXP() + unitLayer.getHalfWidth() > point.getX():
                    beyondMidPoint = False
            if geographicMapCellPosition.getRow() == self.afterNextUnvisitedPathGeographicMapCellPosition.getRow():
                pass
            elif point.getY() < afterNextPoint.getY():
                if unitLayer.getYP() + unitLayer.getHalfHeight() < point.getY():
                    beyondMidPoint = False
            else:
                if unitLayer.getYP() + unitLayer.getHalfHeight() > point.getY():
                    beyondMidPoint = False
            if beyondMidPoint:
                return self.currentGeographicMapCellHistoryP.visit(geographicMapCellPosition)
        return False
    

    # throws Exception
    def processTargetList(self) -> None:
        self.targetWithoutCachedPathLayerInterface = CollidableDestroyableDamageableLayer.getNullInstance()
        for index in range(self.getPossibleTargetList().size() - 1, 0 - 1, -1):
            layerInterface: AdvancedRTSGameLayer = self.getPossibleTargetList().get(index)
            if layerInterface.isDestroyed():
                self.getPossibleTargetList().remove(layerInterface)
            else:
                self.onEnemyMovement(layerInterface)
        if self.targetWithoutCachedPathLayerInterface != CollidableDestroyableDamageableLayer.getNullInstance():
            self.waitingOnTargetPath = True
            self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.THINKING_ABOUT_TARGET, self.basicColorFactory.GREEN)
            self.runWaypointPathTask(self.currentTargetLayerInterfaceP)
        self.getPossibleTargetList().clear()
    

    # throws Exception
    def processTargeting(self) -> None:
        if self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance() and (self.isInSensorRange(self.currentTargetLayerInterfaceP, self.getCurrentTargetDistance()) or self.isTrackingWaypoint()):
            if self.currentTargetLayerInterfaceP.isDestroyed():
                self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.targetDestroyed(self.associatedAdvancedRTSGameLayer)
                self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.KILL, self.basicColorFactory.ORANGE)
                self.clearTarget()
                return
            dx: int = 0
            dy: int = 0
            if self.isTrackingWaypoint():
                self.updateCurrentPathGeographicMapCellPosition()
                point: GPoint = self.nextUnvisitedPathGeographicMapCellPosition.getMidPoint()
                dx = self.associatedAdvancedRTSGameLayer.getXP() + self.associatedAdvancedRTSGameLayer.getHalfWidth() - point.getX()
                dy = self.associatedAdvancedRTSGameLayer.getYP() + self.associatedAdvancedRTSGameLayer.getHalfHeight() - point.getY()
                self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processTargeting(self.associatedAdvancedRTSGameLayer, dx, dy)
            else:
                self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.processTargetingNonWayPoint(self.associatedAdvancedRTSGameLayer, dx, dy)
                dx = (self.associatedAdvancedRTSGameLayer.getXP() + self.associatedAdvancedRTSGameLayer.getHalfWidth()) - (self.currentTargetLayerInterfaceP.getXP() + self.currentTargetLayerInterfaceP.getHalfWidth())
                dy = (self.associatedAdvancedRTSGameLayer.getYP() + self.associatedAdvancedRTSGameLayer.getHalfHeight()) - (self.currentTargetLayerInterfaceP.getYP() + self.currentTargetLayerInterfaceP.getHalfHeight())
            self.associatedAdvancedRTSGameLayer.trackToDXY(dx, dy)
        else:
            if self.associatedAdvancedRTSGameLayer.getParentLayer().isDestroyed():
                self.wander()
            else:
                if self.associatedAdvancedRTSGameLayer.showMoreCaptionStates:
                    self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.STOP, self.basicColorFactory.YELLOW)
                self.associatedAdvancedRTSGameLayer.allStop()
    

    def updateCurrentPathGeographicMapCellPosition(self) -> None:
        self.setLastPathGeographicMapCellPosition(self.getCurrentPathGeographicMapCellPosition())
        self.setCurrentPathGeographicMapCellPosition(self.nextUnvisitedPathGeographicMapCellPosition)
        self.nextUnvisitedPathGeographicMapCellPosition = self.currentGeographicMapCellHistoryP.getFirstUnvisited()
        self.afterNextUnvisitedPathGeographicMapCellPosition = self.currentGeographicMapCellHistoryP.getAfterIfNotLast(self.nextUnvisitedPathGeographicMapCellPosition)
        if self.getCurrentPathGeographicMapCellPosition() != self.nextUnvisitedPathGeographicMapCellPosition:
            self.progressTimeDelayHelper.setStartTimeTNT()
    

    # throws Exception
    def setWaypointPath(self, waypointLayer: AdvancedRTSGameLayer) -> None:
        if self.waypointPathsListP.size() != 0:
            self.setCurrentTargetLayerInterface(waypointLayer)
            MAX: int = 2147483647
            self.setCurrentTargetDistance(MAX)
            self.setRandomGeographicMapCellHistory(self.waypointPathsListP)
        else:
            waypointLayer.getWaypointBehavior().getWaypoint().visit(self.associatedAdvancedRTSGameLayer)
            self.associatedAdvancedRTSGameLayer.getCaptionAnimationHelper().update(self.unitWaypointStrings.ALREADY_THERE_SHORT, self.basicColorFactory.YELLOW)
            self.removeWaypoint(waypointLayer, self.unitWaypointStrings.ALREADY_THERE)
    

    # throws Exception
    def runWaypointPathTask(self, waypointLayer: AdvancedRTSGameLayer) -> None:
        self.setWaypointPathsList(UnitWaypointBehavior2.runningWaypointPathList)
        if self.waypointPathRunnable.isRunning():
            raise Exception("Should never be running here")
        self.waypointPathRunnable.setRunning(True)
        self.waypointPathRunnable.setUnitLayer(self.associatedAdvancedRTSGameLayer)
        self.waypointPathRunnable.setTargetLayer(waypointLayer)
        self.pathFindingThreadPool.runTask(self.waypointPathRunnable)
    

    # throws Exception
    def removeWaypoint(self, waypointLayer: RTSLayer, reason: str) -> None:
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.removeWaypoint(self.associatedAdvancedRTSGameLayer, self, waypointLayer, reason)
        self.targetList.remove(waypointLayer)
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.removeWaypointList(self.associatedAdvancedRTSGameLayer, self, self.targetList)
        if self.currentTargetLayerInterfaceP == waypointLayer:
            self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.removeWaypointClear(self.associatedAdvancedRTSGameLayer)
            self.clearTarget()
    

    # throws Exception
    def clearTarget(self) -> None:
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.clearTarget(self.associatedAdvancedRTSGameLayer)
        self.setCurrentTargetLayerInterface(CollidableDestroyableDamageableLayer.getNullInstance())
        self.setTrackingWaypoint(False)
        MAX: int = 2147483647
        self.setCurrentTargetDistance(MAX)
        TrackingEventHandler.getInstance().fireEvent(self.associatedAdvancedRTSGameLayer.getTrackingEvent())
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        list_: BasicArrayList = self.targetList
        if list_.size() == 0:
            return True
        for index in range(list_.size() - 1, 0 - 1, -1):
            layerInterface: AdvancedRTSGameLayer = list_.get(index)
            if layerInterface.isWaypointListEmptyOrOnlyTargets():
                return False
        return True
    

    def isCloseRange(self, layerInterface: AdvancedRTSGameLayer, targetDistance: int) -> bool:
        return targetDistance < self.closeRange + layerInterface.getHalfHeight()
    

    def isInSensorRange(self, layerInterface: CollidableDestroyableDamageableLayer, targetDistance: int) -> bool:
        return targetDistance < self.sensorRange + layerInterface.getHalfHeight()
    

    def getCurrentTargetingStateString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        if self.currentTargetLayerInterfaceP != CollidableDestroyableDamageableLayer.getNullInstance():
            stringBuffer.append(UnitWaypointBehavior2.TARGET_LAYER)
            stringBuffer.append(self.commonSeps.SPACE)
            stringBuffer.append(self.currentTargetLayerInterfaceP.getName())
            stringBuffer.append(" with ")
            stringBuffer.append(UnitWaypointBehavior2.TARGET_DISTANCE)
            stringBuffer.append(self.commonSeps.SPACE)
            stringBuffer.appendint(int(self.getCurrentTargetDistance()))
        return str(stringBuffer)
    

    # throws Exception
    def addWaypointFromUser(self, advancedRTSGameLayer: AdvancedRTSGameLayer) -> None:
        if advancedRTSGameLayer.isDestroyed():
            raise Exception("Trying to add a dead: " + str(advancedRTSGameLayer))
        self.associatedAdvancedRTSGameLayer.waypoint2LogHelperP.addWaypointFromUser(self.associatedAdvancedRTSGameLayer, advancedRTSGameLayer)
        self.targetList.clear()
        self.targetList.add(advancedRTSGameLayer)
        self.clearTarget()
    

    # throws Exception
    def addBuildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> None:
        if not self.buildingSteeringVisitor.getList().contains(allbinaryLayer):
            self.buildingSteeringVisitor.getList().add(allbinaryLayer)
            self.buildingSteeringVisitor.getPositionList().add(cellPosition)
        if not self.getSteeringVisitorList().contains(self.buildingSteeringVisitor):
            self.getSteeringVisitorList().add(self.buildingSteeringVisitor)
    

    # throws Exception
    def buildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> bool:
        return self.associatedAdvancedRTSGameLayer.buildingChase(allbinaryLayer, cellPosition)
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.layer.SteeringVisitor import SteeringVisitor
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.MultipassWaypointPathRunnable import MultipassWaypointPathRunnable
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.WaypointPathRunnable import WaypointPathRunnable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.WaypointPathRunnableBase import WaypointPathRunnableBase
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.math.LayerDistanceUtil import LayerDistanceUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.thread.PathFindingThreadPool import PathFindingThreadPool
from org.allbinary.thread.ThreadPool import ThreadPool
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.game.layer.unit.UnitWaypointStrings import UnitWaypointStrings
from org.allbinary.game.layer.unit.BuildingSteeringVisitor import BuildingSteeringVisitor


