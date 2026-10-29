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
# package org.allbinary.game.layer.building

from __future__ import annotations

from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.animation.RotationAnimationInterfaceCompositeInterface import RotationAnimationInterfaceCompositeInterface
from org.allbinary.game.tracking.TrackingEventListenerInterface import TrackingEventListenerInterface


class BuildingLayer(AdvancedRTSGameLayer, RotationAnimationInterfaceCompositeInterface, TrackingEventListenerInterface):

    def _init_fields(self) -> None:
        self.buildingLevelCost: int = 0
        self.productivity: int = 0
        self.efficiency: int = None
        self.efficiencyPerLevel: int = None
        self.trackingEvent: TrackingEvent = None
        self.damageFloaters: DamageFloaters = None
        self.damageFloatersPaintableInterface: Paintable = None
        self.healthBar: Paintable = None
        self.pathsHashtable: ABHashtable[object, object] = None
        self.local: bool = False
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(3000)
    

    # throws Exception
    @staticmethod
    def createSimulated() -> BuildingLayer:
        from org.allbinary.game.layer.building.SimulatedBuildingPropertiesFactory import SimulatedBuildingPropertiesFactory
        nullAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = NullAnimationFactory.getFactoryInstance()
        nullIndexedAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = NullIndexedAnimationFactory.getFactoryInstance()
        return BuildingLayer(RemoteInfo.REMOTE_INFO, SimulatedBuildingPropertiesFactory.getInstance(), AdvancedRTSProperties.createPropertiesSimulated(), GroupFactory.getInstance().NULL_GROUP_ARRAY, StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING, Health.NULL_HEALTH, NullRTSFormInputFactory.getInstance(), nullAnimationInterfaceFactoryInterface, nullIndexedAnimationInterfaceFactoryInterface, nullAnimationInterfaceFactoryInterface, nullAnimationInterfaceFactoryInterface, nullIndexedAnimationInterfaceFactoryInterface, NullIndexedAnimationFactory.getFactoryInstance(), RectangleFactory.SINGLETON, 0, 0)
    

    def __init__(self, remoteInfo: RemoteInfo, buildingPropertiesFactory: BuildingPropertiesFactory, advancedRTSProperties: AdvancedRTSProperties, groupInterface: list[Group], rootName: str, name: str, healthInterface: Health, rtsFormInput: RTSFormInput, animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface: ProceduralAnimationInterfaceFactoryInterface, rectangle: Rectangle, x: int, y: int) -> None:
        super().__init__(remoteInfo, NullPathFindingLayer.NULL_PATH_FINDING_LAYER, advancedRTSProperties, groupInterface, rootName, name, healthInterface, rtsFormInput, animationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface, rectangle, x, y, TileLayerPositionIntoViewPosition())
        self._init_fields()
        self.setCollidableInferface(CollidableRTSBehavior(True))
        self.getWaypointBehavior().setWaypoint(Waypoint(self, SelectSound.getInstance()))
        self.damageFloaters = buildingPropertiesFactory.getDamageFloaters(self)
        self.damageFloatersPaintableInterface = buildingPropertiesFactory.damageFloatersPaintableInterface
        self.healthBar = buildingPropertiesFactory.getHealthBar(self)
        self.pathsHashtable = buildingPropertiesFactory.getHashtable()
        self.setMaxLevel(30)
        self.setProductivity(1)
        self.setEfficiency(self.calculateEfficiency())
        self.efficiencyPerLevel = buildingPropertiesFactory.getEfficiencyPerLevel(self)
        self.efficiency = self.efficiencyPerLevel
        self.generateMoveOutOfBuildAreaPaths()
        self.trackingEvent = buildingPropertiesFactory.getTrackingEvent(self)
    

    def initVisibility(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        advancedRTSPlayerLayerInterface: AdvancedRTSPlayerLayerInterface = rtsPlayerLayerInterface
        if advancedRTSPlayerLayerInterface.isLocalPlayer():
            self.local = True
            self.addVisibility()
        else:
            self.local = False
        super().initVisibility(rtsPlayerLayerInterface)
    

    # throws Exception
    def construct(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        super().construct(rtsPlayerLayerInterface)
        TrackingEventHandler.getInstance().addListenerInterface(self)
    

    def onMovement(self, trackingEvent: TrackingEvent) -> None:
        try:
            layerInterface: AdvancedRTSGameLayer = trackingEvent.getLayerInterface()
            if layerInterface.getGroupInterface()[0] != self.getGroupInterface()[0]:
                layerInterface.onMovementFound(self.trackingEvent)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onMovement", e)
    

    # throws Exception
    def processBuiltTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        if self.getHealthInterface().isDamaged():
            self.setAnimationInterface(self.destroyAnimationInterface)
        if not self.getHealthInterface().isAlive():
            if self.isReadyForExplosion():
                currentFrame: int = self.destroyAnimationInterface.getFrame()
                size: int = self.destroyAnimationInterface.getSize() - 1
                if currentFrame == size and not self.timeDelayHelper.isTimeTNT():
                    if not self.getHealthInterface().isAlive():
                        self.setDestroyed(True)
                else:
                    self.destroyAnimationInterface.nextFrame()
            else:
                self.setAnimationInterface(self.destroyAnimationInterface)
                SecondaryPlayerQueueFactory.getInstance().add(ExplosionBasicSound.getInstance())
                self.shakeListener.onSmallShakeEvent()
                self.vibration.vibrate(self.duration, 0, 0)
                self.timeDelayHelper.setStartTimeTNT()
                self.setReadyForExplosion(True)
        else:
            super().processBuiltTick(allBinaryLayerManager)
        self.indexedButShouldBeRotationAnimationInterface.nextFrame()
    

    def calculateEfficiency(self) -> int:
        return self.efficiencyPerLevel
    

    def getCost(self) -> int:
        total: int = RTSLayerUtil.getInstance().getCostExponential(int((self.getLevel() * self.getBuildingLevelCost())))
        return total
    

    def getDowngradeCost(self) -> int:
        downgradeCost: int = RTSLayerUtil.getInstance().getCostExponential(int(((self.getLevel() - 1) * self.getBuildingLevelCost())))
        self.logUtil.putF("Cost: " + str(downgradeCost), self, "getDowngradeCost")
        return int(downgradeCost * 9 / 10)
    

    def getUpgradeCost(self) -> int:
        upgradeCost: int = RTSLayerUtil.getInstance().getCostExponential(int(((self.getLevel() + 1) * self.getBuildingLevelCost())))
        return upgradeCost
    

    def downgrade(self) -> None:
        super().downgrade()
        self.setProductivity(self.getProductivity() - 1)
        self.setEfficiency(self.getEfficiency() - self.calculateEfficiency())
        self.getHealthInterface().setMaxHealth(self.getHealthInterface().getMaxHealth() - ((self.getLevel() + 1) * 100))
    

    def upgrade(self) -> None:
        super().upgrade()
        self.setProductivity(self.getProductivity() + 1)
        self.setEfficiency(self.getEfficiency() + self.calculateEfficiency())
        self.getHealthInterface().setMaxHealth(self.getHealthInterface().getMaxHealth() + (self.getLevel() * 100))
    

    def getBuildingLevelCost(self) -> int:
        return self.buildingLevelCost
    

    def setBuildingLevelCost(self, buildingLevelCost: int) -> None:
        self.buildingLevelCost = buildingLevelCost
    

    def getProductivity(self) -> int:
        return self.productivity
    

    def setProductivity(self, productivity: int) -> None:
        self.productivity = productivity
    

    def getEfficiency(self) -> int:
        return self.efficiency
    

    def setEfficiency(self, efficiency: int) -> None:
        self.efficiency = efficiency
    

    # throws Exception
    def generateMoveOutOfBuildAreaPaths(self) -> None:
        occupyList: BasicArrayList = self.geographicMapCellPositionAreaBase.getOccupyingGeographicMapCellPositionList()
        surroundList: BasicArrayList = self.geographicMapCellPositionAreaBase.getSurroundingGeographicMapCellPositionList()
        NO_DIRECTION: Direction = DirectionFactory.getInstance().NO_DIRECTION
        geographicMapDirectionUtil: GeographicMapDirectionUtil = GeographicMapDirectionUtil.getInstance()
        pathsList: BasicArrayList = None
        occupyGeographicMapCellPosition: GeographicMapCellPosition = None
        surroundGeographicMapCellPosition: GeographicMapCellPosition = None
        list_: BasicArrayList = None
        for index2 in range(occupyList.size() - 1, 0 - 1, -1):
            pathsList = BasicArrayListD()
            occupyGeographicMapCellPosition = occupyList.get(index2)
            for index in range(surroundList.size() - 1, 0 - 1, -1):
                surroundGeographicMapCellPosition = surroundList.get(index)
                if geographicMapDirectionUtil.getEightDirectionFromCellPositionToAdjacentCellPosition(surroundGeographicMapCellPosition, occupyGeographicMapCellPosition) != NO_DIRECTION:
                    list_ = BasicArrayListS(1)
                    list_.add(surroundGeographicMapCellPosition)
                    pathsList.add(list_)
            self.pathsHashtable.put(occupyGeographicMapCellPosition, pathsList)
    

    def getMoveOutOfBuildAreaPath(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        pathsList: BasicArrayList = self.pathsHashtable.get(geographicMapCellPosition)
        return pathsList
    

    def getEndGeographicMapCellPositionList(self) -> BasicArrayList:
        return self.geographicMapCellPositionAreaBase.getSurroundingGeographicMapCellPositionList()
    

    def shouldHandleStartSameAsEnd(self) -> bool:
        return False
    

    def paint(self, graphics: Graphics) -> None:
        if self.isVisible():
            super().paint(graphics)
            self.damageFloatersPaintableInterface.paint(graphics)
            self.healthBar.paint(graphics)
    

    # throws Exception
    def damage(self, damage: int, damageType: int) -> None:
        super().damage(damage, damageType)
        self.damageFloaters.add(damage)
        if damage > 0:
            self.getHealthInterface().damage(damage)
    

    # throws Exception
    def getDamage(self, damageType: int) -> int:
        return 0
    

    def addVisibility(self) -> None:
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = self.geographicMapCellPositionAreaBase
        occupyList: BasicArrayList = geographicMapCellPositionArea.getOccupyingGeographicMapCellPositionList()
        VisibleCellPositionsSingleton.getInstance().addStationaryCellPositions(occupyList)
        surroundList: BasicArrayList = geographicMapCellPositionArea.getSurroundingGeographicMapCellPositionList()
        VisibleCellPositionsSingleton.getInstance().addStationaryCellPositions(surroundList)
    

    def removeVisibility(self) -> None:
        occupyList: BasicArrayList = self.geographicMapCellPositionAreaBase.getOccupyingGeographicMapCellPositionList()
        VisibleCellPositionsSingleton.getInstance().removeStationaryCellPositions(occupyList)
        surroundList: BasicArrayList = self.geographicMapCellPositionAreaBase.getSurroundingGeographicMapCellPositionList()
        VisibleCellPositionsSingleton.getInstance().removeStationaryCellPositions(surroundList)
    

    # throws Exception
    def setDestroyed(self, destroyed: bool) -> None:
        super().setDestroyed(destroyed)
        if self.isDestroyed():
            DropCellPositionHistory.getInstance().removeAll(self)
            TrackingEventHandler.getInstance().removeListener(self)
            if self.local:
                self.removeVisibility()
            if not self.getHealthInterface().isAlive():
                damage: int = self.getHealthInterface().getMaxHealth()
                if damage > 10:
                    SecondaryPlayerQueueFactory.getInstance().add(ExplosionBasicSound.getInstance())
                    if damage < 100:
                        self.shakeListener.onSmallShakeEvent()
                        self.vibration.vibrate(self.duration, 0, 0)
                    elif damage < 1000:
                        self.shakeListener.onMediumShakeEvent()
                        self.vibration.vibrate(self.duration * 2, 0, 0)
                    elif damage < 3000:
                        self.shakeListener.onLargeShakeEvent()
                        self.vibration.vibrate(self.duration * 4, 0, 0)
    

    def createHudPaintable(self) -> SelectionHudPaintable:
        from org.allbinary.game.layer.building.BuildingInfoHudPaintable import BuildingInfoHudPaintable
        buildingInfoHudPaintable: BuildingInfoHudPaintable = BuildingInfoHudPaintable.getInstance()
        buildingInfoHudPaintable.setBasicColorP(self.allBinaryGameLayerManagerP.getForegroundBasicColor())
        buildingInfoHudPaintable.setRtsLayer(self)
        return buildingInfoHudPaintable
    

    def getHudPaintable(self) -> SelectionHudPaintable:
        from org.allbinary.game.layer.building.BuildingInfoHudPaintable import BuildingInfoHudPaintable
        buildingInfoHudPaintable: BuildingInfoHudPaintable = BuildingInfoHudPaintable.getInstance()
        return buildingInfoHudPaintable
    

    def getType(self) -> int:
        return BuildingLayer.getStaticType()
    

    @staticmethod
    def getStaticType() -> int:
        return 2
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.ag.weapon.media.audio.ExplosionBasicSound import ExplosionBasicSound
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.NullIndexedAnimationFactory import NullIndexedAnimationFactory
from org.allbinary.game.identification.GroupFactory import GroupFactory
from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
from org.allbinary.game.input.form.VisibleCellPositionsSingleton import VisibleCellPositionsSingleton
from org.allbinary.game.layer.AdvancedRTSPlayerLayerInterface import AdvancedRTSPlayerLayerInterface
from org.allbinary.game.layer.AdvancedRTSProperties import AdvancedRTSProperties
from org.allbinary.game.layer.CollidableRTSBehavior import CollidableRTSBehavior
from org.allbinary.game.layer.RTSLayerUtil import RTSLayerUtil
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable
from org.allbinary.game.layer.waypoint.Waypoint import Waypoint
from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters
from org.allbinary.game.health.Health import Health
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.GeographicMapCellPositionAreaBase import GeographicMapCellPositionAreaBase
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.media.audio.SelectSound import SelectSound
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapDirectionUtil import GeographicMapDirectionUtil
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayListS import BasicArrayListS
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.util.ABHashtable import ABHashtable


