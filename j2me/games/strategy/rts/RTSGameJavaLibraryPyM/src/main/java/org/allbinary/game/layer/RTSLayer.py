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

from org.allbinary.game.multiplayer.layer.MultiPlayerGameLayer import MultiPlayerGameLayer
from org.allbinary.game.input.GameInputInterface import GameInputInterface
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
from org.allbinary.game.tick.TickableInterface import TickableInterface
from org.allbinary.game.layer.RTSInterface import RTSInterface
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface


class RTSLayer(MultiPlayerGameLayer, TickableInterface, GameInputInterface, GameKeyEventSourceInterface, RTSInterface, PathFindingLayerInterface):
    id: int = 0
    MAIN_INDEX: int = 0
    SECONDARY_INDEX: int = 1

    def _init_fields(self) -> None:
        self.debug: bool = True
        self.showMoreCaptionStates: bool = self.debug
        self.inputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.rtsLayer2LogHelper: RTSLayer2LogHelper = RTSLayer2LogHelper.getInstance()
        self.waypointLogHelperP: WaypointLogHelper = WaypointLogHelper.getInstance()
        self.waypoint2LogHelperP: Waypoint2LogHelper = Waypoint2LogHelper.getInstance()
        self.waypointRunnableLogHelperP: WaypointRunnableLogHelper = WaypointRunnableLogHelper.getInstance()
        self.rtsFormInput: RTSFormInput = None
        self.verticleBuildAnimationInterface: IndexedAnimation = None
        self.rangeAnimation: Animation = None
        self.initRangeAnimation: Animation = None
        self.sensorRangeAnimation: Animation = None
        self.initSensorRangeAnimation: Animation = None
        self.baseAnimationInterface: Animation = None
        self.buildFrameTimeHelper: TimeDelayHelper = TimeDelayHelper(50)
        self.buildAnimationInterface: Animation = None
        self.animationInterface: Animation = None
        self.initAnimationInterface: IndexedAnimation = None
        self.indexedButShouldBeRotationAnimationInterface: IndexedAnimation = None
        self.emptyAnimationInterface: IndexedAnimation = None
        self.destroyAnimationInterface: IndexedAnimation = None
        self.fireTimeHelper: TimeDelayHelper = TimeDelayHelper(700)
        self.rootName: str = None
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.BUILD_VALUE: int = 63
        self.geographicMapCellPositionAreaBase: GeographicMapCellPositionAreaBase = None
        self.healthInterface: Health = Health.NULL_HEALTH
        self.level: int = 1
        self.maxLevel: int = 1
        self.hackVerticleBuild: int = self.BUILD_VALUE
        self.slightAngle: int = 0
        self.percentCompleteP: int = 0
        self.destroyed: bool = False
        self.selected: bool = False
        self.rtsLayerUtil: RTSLayerUtil = RTSLayerUtil.getInstance()
        self.layerDistanceUtil: LayerDistanceUtil = LayerDistanceUtil.getInstance()
    

    # throws Exception
    @staticmethod
    def createSimulatedInstance(remoteInfo: RemoteInfo) -> RTSLayer:
        nullAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = NullAnimationFactory.getFactoryInstance()
        nullIndexedAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = NullIndexedAnimationFactory.getFactoryInstance()
        return RTSLayer(RemoteInfo.REMOTE_INFO, GroupFactory.getInstance().NULL_GROUP_ARRAY, StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING, Health.NULL_HEALTH, NullRTSFormInputFactory.getInstance(), nullAnimationInterfaceFactoryInterface, nullIndexedAnimationInterfaceFactoryInterface, nullAnimationInterfaceFactoryInterface, nullAnimationInterfaceFactoryInterface, nullIndexedAnimationInterfaceFactoryInterface, NullIndexedAnimationFactory.getFactoryInstance(), RectangleFactory.SINGLETON, 0, 0, TileLayerPositionIntoViewPosition())
    

    def __init__(self, remoteInfo: RemoteInfo, groupInterface: list[Group], rootName: str, name: str, healthInterface: Health, rtsFormInput: RTSFormInput, animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface: ProceduralAnimationInterfaceFactoryInterface, rectangle: Rectangle, x: int, y: int, viewPosition: ViewPositionBase) -> None:
        from org.allbinary.game.layer.GeographicMapCellPositionArea import GeographicMapCellPositionArea
        super().__init__(remoteInfo, groupInterface, name, rectangle, viewPosition)
        self._init_fields()
        self.initInputProcessors()
        self.rootName = rootName
        self.healthInterface = healthInterface
        self.rtsFormInput = rtsFormInput
        self.setPosition(x, y, self.z)
        self.verticleBuildAnimationInterface = verticleBuildAnimationInterfaceFactoryInterface.getInstance(0)
        self.buildAnimationInterface = buildAnimationInterfaceFactoryInterface.getInstance(0)
        self.baseAnimationInterface = baseAnimationInterfaceFactoryInterface.getInstance(0)
        self.emptyAnimationInterface = emptyAnimationInterfaceFactoryInterface.getInstance(0)
        self.indexedButShouldBeRotationAnimationInterface = animationInterfaceFactoryInterface.getInstance(0)
        self.initAnimationInterface = self.indexedButShouldBeRotationAnimationInterface
        self.destroyAnimationInterface = proceduralAnimationInterfaceFactoryInterface.getInstanceAnimation(self.indexedButShouldBeRotationAnimationInterface)
        animation: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.rangeAnimation = animation
        self.initRangeAnimation = animation
        self.sensorRangeAnimation = animation
        self.initSensorRangeAnimation = animation
        self.animationInterface = self.initAnimationInterface
        self.geographicMapCellPositionAreaBase = GeographicMapCellPositionArea(self)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        viewPosition2: TileLayerPositionIntoViewPosition = self.getViewPosition()
        viewPosition2.setTiledLayer(tiledLayer)
        self.updateWaypointBehavior(geographicMapInterface)
    

    # throws Exception
    def updateWaypointBehavior(self, geographicMapInterface: BasicGeographicMap) -> None:
        self.geographicMapCellPositionAreaBase.update(geographicMapInterface)
    

    # throws Exception
    def construct(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        ViewPositionEventHandler.getInstance().addListener(self)
        self.animationInterface = self.buildAnimationInterface
        self.hackVerticleBuild = 0
    

    def select(self) -> None:
        self.rangeAnimation = self.initRangeAnimation
        self.sensorRangeAnimation = self.initSensorRangeAnimation
        self.setSelected(True)
    

    def deselect(self) -> None:
        animation: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.rangeAnimation = animation
        self.sensorRangeAnimation = animation
        self.setSelected(False)
    

    def setSelected(self, selected: bool) -> None:
        self.selected = selected
    

    def isSelected(self) -> bool:
        return self.selected
    

    def getPercentComplete(self) -> int:
        return self.percentCompleteP
    

    def getScrollSelectionForm(self) -> ScrollSelectionForm:
        return ScrollSelectionForm.getNullScrollSelectionForm()
    

    def initInputProcessors(self) -> None:
        GameInputProcessorUtil.init(self.inputProcessorArray)
    

    # throws Exception
    def processBuiltTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        self.animationInterface = self.indexedButShouldBeRotationAnimationInterface
    

    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        try:
            if self.isCompleted():
                self.processBuiltTick(allBinaryLayerManager)
            else:
                self.build()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "processTick", e)
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        pass
    

    def reload(self) -> None:
        pass
    

    def onMovement(self, trackingEvent: TrackingEvent) -> None:
        pass
    

    # throws Exception
    def onMovementFound(self, trackingEvent: TrackingEvent) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        super().paintFirst(graphics)
        viewPosition: ViewPositionBase = self.getViewPosition()
        viewX: int = viewPosition.getX()
        viewY: int = viewPosition.getY()
        self.getAnimationInterface().paintXY(graphics, viewX, viewY)
    

    # throws Exception
    def damage(self, damage: int, damageType: int) -> None:
        pass
    

    def getSourceId(self) -> int:
        return RTSLayer.id
    

    def downgrade(self) -> None:
        self.rtsLayerUtil.downgrade(self)
    

    def upgrade(self) -> None:
        self.rtsLayerUtil.upgrade(self)
    

    def isCompleted(self) -> bool:
        if self.hackVerticleBuild < self.BUILD_VALUE:
            return False
        else:
            return True
    

    # throws Exception
    def build(self) -> None:
        if self.buildFrameTimeHelper.isTimeTNT():
            self.animationInterface = self.buildAnimationInterface
            self.verticleBuildAnimationInterface.nextFrame()
            self.hackVerticleBuild += 1
        self.percentCompleteP = int(100 * self.hackVerticleBuild / self.BUILD_VALUE)
        self.getHudPaintable().updateInfo()
    

    def isSelfUpgradeable(self) -> bool:
        return True
    

    def getCost(self) -> int:
        return self.rtsLayerUtil.getCost(self)
    

    def getDowngradeCost(self) -> int:
        return self.rtsLayerUtil.getDowngradeCost(self)
    

    def getUpgradeCost(self) -> int:
        return self.rtsLayerUtil.getUpgradeCost(self)
    

    def isUpgradeable(self) -> bool:
        if self.getLevel() < self.getMaxLevel():
            return True
        else:
            return False
    

    def isDowngradeable(self) -> bool:
        if self.getLevel() > 1:
            return True
        else:
            return False
    

    def getLevel(self) -> int:
        return self.level
    

    def setLevel(self, level: int) -> None:
        self.level = level
    

    def getVerticleBuildAnimationInterface(self) -> Animation:
        return self.verticleBuildAnimationInterface
    

    def getAnimationInterface(self) -> Animation:
        return self.animationInterface
    

    def setAnimationInterface(self, animationInterface: Animation) -> None:
        self.animationInterface = animationInterface
    

    # throws Exception
    def setTarget(self, targetGameLayer: PathFindingLayerInterface) -> None:
        anotherTargetDistance: int = self.layerDistanceUtil.getDistance(self, targetGameLayer)
        waypointBehaviorBase: WaypointBehaviorBase = self.getWaypointBehavior()
        waypointBehaviorBase.setTargetWithDistance(targetGameLayer, anotherTargetDistance)
    

    def createHudPaintable(self) -> SelectionHudPaintable:
        raise RuntimeError()
    

    def getHudPaintable(self) -> SelectionHudPaintable:
        raise RuntimeError()
    

    def getMaxLevel(self) -> int:
        return self.maxLevel
    

    def setMaxLevel(self, maxLevel: int) -> None:
        self.maxLevel = maxLevel
    

    def getHealthInterface(self) -> Health:
        return self.healthInterface
    

    def setHealthInterface(self, healthInterface: Health) -> None:
        self.healthInterface = healthInterface
    

    def getRTSFormInput(self) -> RTSFormInput:
        return self.rtsFormInput
    

    # throws Exception
    def isDestroyed(self) -> bool:
        return self.destroyed
    

    # throws Exception
    def setDestroyed(self, destroyed: bool) -> None:
        self.destroyed = destroyed
        if self.isDestroyed():
            DestroyedLayerProcessor.getInstance().add(self)
            ViewPositionEventHandler.getInstance().removeListener(self)
    

    def getEndGeographicMapCellPositionList(self) -> BasicArrayList:
        return self.geographicMapCellPositionAreaBase.getOccupyingGeographicMapCellPositionList()
    

    def getGeographicMapCellPositionArea(self) -> GeographicMapCellPositionAreaBase:
        return self.geographicMapCellPositionAreaBase
    

    def shouldHandleStartSameAsEnd(self) -> bool:
        return True
    

    # throws Exception
    def handleCost(self, ownerLayer: PathFindingLayerInterface) -> None:
        pass
    

    def getWaypointBehavior(self) -> WaypointBehaviorBase:
        raise RuntimeError()
    

    def getParentLayer(self) -> PathFindingLayerInterface:
        raise RuntimeError()
    

    def getRTSLayer2LogHelper(self) -> RTSLayer2LogHelper:
        return self.rtsLayer2LogHelper
    

    def getWaypointLogHelper(self) -> WaypointLogHelper:
        return self.waypointLogHelperP
    

    def getWaypoint2LogHelper(self) -> Waypoint2LogHelper:
        return self.waypoint2LogHelperP
    

    def getWaypointRunnableLogHelper(self) -> WaypointRunnableLogHelper:
        return self.waypointRunnableLogHelperP
    

    def shouldAddWaypointFromBuilding(self) -> bool:
        return False
    

    def getCaptionAnimationHelper(self) -> CaptionAnimationHelperBase:
        raise RuntimeError()
    

    def isShowMoreCaptionStates(self) -> bool:
        return self.showMoreCaptionStates
    

    # throws Exception
    def init(self, geographicMapCellHistory: GeographicMapCellHistory, geographicMapCellPositionBasicArrayList: BasicArrayList) -> None:
        pass
    

    # throws Exception
    def getCurrentGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        raise RuntimeError()
    

    # throws Exception
    def getTopLeftGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        raise RuntimeError()
    

    def getMoveOutOfBuildAreaPath(self, geographicMapCellPosition: GeographicMapCellPosition) -> BasicArrayList:
        raise RuntimeError()
    

    # throws Exception
    def setClosestGeographicMapCellHistory(self, pathsList: BasicArrayList) -> None:
        pass
    

    def teleportTo(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        pass
    

    # throws Exception
    def setLoad(self, resource: int) -> None:
        pass
    

    # throws Exception
    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        raise RuntimeError()
    

    # throws Exception
    def trackTo(self, reason: str) -> None:
        pass
    

    # throws Exception
    def trackToDXY(self, dx: int, dy: int) -> None:
        pass
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        return False
    

    def getTrackingEvent(self) -> TrackingEvent:
        raise RuntimeError()
    

    # throws Exception
    def buildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> bool:
        return False
    

    def allStop(self) -> None:
        pass
    

    @staticmethod
    def getMinStaticType() -> int:
        return 1
    

    @staticmethod
    def getMaxStaticType() -> int:
        return 4
    

    @staticmethod
    def isRTSLayer(layerInterface: AllBinaryLayer) -> bool:
        if layerInterface.getType() >= RTSLayer.getMinStaticType() and layerInterface.getType() <= RTSLayer.getMaxStaticType():
            return True
        return False
    

    def implmentsTickableInterface(self) -> bool:
        return True
    

    def implmentsGameInputInterface(self) -> bool:
        return True
    

    def getRootName(self) -> str:
        return self.rootName
    

    def getRotationAnimationInterface(self) -> RotationAnimation:
        return self.indexedButShouldBeRotationAnimationInterface
    

    def setFrame(self, index: int) -> None:
        self.getRotationAnimationInterface().setFrame(index)
    

    def setRotationAnimationInterface(self, rotationAnimationInterface: RotationAnimation) -> None:
        self.indexedButShouldBeRotationAnimationInterface = rotationAnimationInterface
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.NullIndexedAnimationFactory import NullIndexedAnimationFactory
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.animation.RotationAnimation import RotationAnimation
from org.allbinary.animation.caption.CaptionAnimationHelperBase import CaptionAnimationHelperBase
from org.allbinary.game.combat.destroy.DestroyedLayerProcessor import DestroyedLayerProcessor
from org.allbinary.game.health.Health import Health
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.identification.GroupFactory import GroupFactory
from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
from org.allbinary.game.layer.waypoint.Waypoint2LogHelper import Waypoint2LogHelper
from org.allbinary.game.layer.waypoint.WaypointLogHelper import WaypointLogHelper
from org.allbinary.game.layer.waypoint.WaypointRunnableLogHelper import WaypointRunnableLogHelper
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.view.event.ViewPositionEventHandler import ViewPositionEventHandler
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.LayerDistanceUtil import LayerDistanceUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.view.ViewPositionBase import ViewPositionBase
from org.allbinary.game.layer.RTSLayer2LogHelper import RTSLayer2LogHelper
from org.allbinary.game.layer.RTSLayerUtil import RTSLayerUtil


