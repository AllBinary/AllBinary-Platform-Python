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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.combat.destroy.event.DestroyedEventListenerInterface import DestroyedEventListenerInterface
from org.allbinary.game.layer.RTSLayer import RTSLayer


class AdvancedRTSGameLayer(RTSLayer, DestroyedEventListenerInterface):

    def _init_fields(self) -> None:
        self.shakeListener: ShakeAnimationListener = None
        self.vibration: AllBinaryVibrationME = None
        self.duration: int = None
        self.parentLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
        self.waypointBehaviorBase: TickableInterface = NullTickable.getInstance()
    

    # throws Exception
    @staticmethod
    def createSimulated() -> AdvancedRTSGameLayer:
        from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
        from org.allbinary.game.layer.AdvancedRTSProperties import AdvancedRTSProperties
        nullAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = NullAnimationFactory.getFactoryInstance()
        nullIndexedAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = NullIndexedAnimationFactory.getFactoryInstance()
        return AdvancedRTSGameLayer(RemoteInfo.REMOTE_INFO, NullPathFindingLayer.NULL_PATH_FINDING_LAYER, AdvancedRTSProperties.createPropertiesSimulated(), GroupFactory.getInstance().NULL_GROUP_ARRAY, StringUtil.getInstance().EMPTY_STRING, StringUtil.getInstance().EMPTY_STRING, Health.NULL_HEALTH, NullRTSFormInputFactory.getInstance(), nullAnimationInterfaceFactoryInterface, nullIndexedAnimationInterfaceFactoryInterface, nullAnimationInterfaceFactoryInterface, nullAnimationInterfaceFactoryInterface, nullIndexedAnimationInterfaceFactoryInterface, NullIndexedAnimationFactory.getFactoryInstance(), RectangleFactory.SINGLETON, 0, 0, TileLayerPositionIntoViewPosition())
    

    def __init__(self, remoteInfo: RemoteInfo, parentLayer: PathFindingLayerInterface, advancedRTSProperties: AdvancedRTSProperties, groupInterface: list[Group], rootName: str, name: str, healthInterface: Health, rtsFormInput: RTSFormInput, animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface: ProceduralAnimationInterfaceFactoryInterface, rectangle: Rectangle, x: int, y: int, viewPosition: ViewPositionBase) -> None:
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        super().__init__(remoteInfo, groupInterface, rootName, name, healthInterface, rtsFormInput, animationInterfaceFactoryInterface, emptyAnimationInterfaceFactoryInterface, baseAnimationInterfaceFactoryInterface, buildAnimationInterfaceFactoryInterface, verticleBuildAnimationInterfaceFactoryInterface, proceduralAnimationInterfaceFactoryInterface, rectangle, x, y, viewPosition)
        self._init_fields()
        self.setVisible(False)
        self.setWaypointBehavior(WaypointBehaviorBase())
        self.shakeListener = advancedRTSProperties.shakeListener
        self.vibration = advancedRTSProperties.vibration
        self.duration = advancedRTSProperties.duration
        self.setParentLayer(parentLayer)
    

    # throws Exception
    def updateWaypointBehavior(self, geographicMapInterface: BasicGeographicMap) -> None:
        super().updateWaypointBehavior(geographicMapInterface)
        self.getWaypointBehavior().getWaypoint().setAllBinaryGameLayerManager(self.allBinaryGameLayerManagerP)
    

    def initVisibility(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        advancedRTSPlayerLayerInterface: AdvancedRTSPlayerLayerInterface = rtsPlayerLayerInterface
        if advancedRTSPlayerLayerInterface.isLocalPlayer() or advancedRTSPlayerLayerInterface.getGameType() == GameTypeFactory.getInstance().BOT:
            self.setVisible(True)
        else:
            self.setVisible(False)
    

    # throws Exception
    def construct(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface) -> None:
        super().construct(rtsPlayerLayerInterface)
        self.initVisibility(rtsPlayerLayerInterface)
        BuildingEventHandler.getInstance().addListenerInterface(self.getWaypointBehavior().getWaypoint())
    

    # throws Exception
    def setDestroyed(self, destroyed: bool) -> None:
        from org.allbinary.game.layer.RTSLayerUtil import RTSLayerUtil
        super().setDestroyed(destroyed)
        if self.isDestroyed():
            BuildingEventHandler.getInstance().removeListener(self.getWaypointBehavior().getWaypoint())
            BuildingEventHandler.getInstance().removeListener(self)
            DestroyedEventHandler.getInstance().addListener(self)
            RTSLayerUtil.getInstance().destroyAndClear(self.getWaypointBehavior().getOwnedWaypointList())
    

    def getParentLayer(self) -> PathFindingLayerInterface:
        return self.parentLayer
    

    def setParentLayer(self, parentLayer: PathFindingLayerInterface) -> None:
        self.parentLayer = parentLayer
    

    def getWaypointBehavior(self) -> WaypointBehaviorBase:
        return self.waypointBehaviorBase
    

    def setWaypointBehavior(self, unitWaypointHelper: WaypointBehaviorBase) -> None:
        self.waypointBehaviorBase = unitWaypointHelper
    

    def getWaypointLogHelper(self) -> WaypointLogHelper:
        return self.waypointLogHelperP
    

    def getWaypoint2LogHelper(self) -> Waypoint2LogHelper:
        return self.waypoint2LogHelperP
    

    def getWaypointRunnableLogHelper(self) -> WaypointRunnableLogHelper:
        return self.waypointRunnableLogHelperP
    

    def shouldAddWaypointFromBuilding(self) -> bool:
        from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
        if self.parentLayer != NullPathFindingLayer.NULL_PATH_FINDING_LAYER:
            parentAdvancedRTSGameLayer: AdvancedRTSGameLayer = self.parentLayer
            if parentAdvancedRTSGameLayer.getType() != UnitLayer.getStaticType():
                return True
        return False
    

    def isWaypointListEmptyOrOnlyTargets(self) -> bool:
        if self.getType() != UnitLayer.getStaticType():
            return True
        return False
    

    # throws Exception
    def buildingChase(self, allbinaryLayer: AllBinaryLayer, cellPosition: GeographicMapCellPosition) -> bool:
        geographicMapCellPosition: GeographicMapCellPosition = self.getCurrentGeographicMapCellPosition()
        buildingDirection: Direction = GeographicMapDirectionUtil.getInstance().getDirectionFromCellPositionToAdjacentCellPosition(geographicMapCellPosition, cellPosition)
        angleInfo: AngleInfo = self.getRotationAnimationInterface().getAngleInfoP()
        angle: int = FrameUtil.getInstance().adjustAngleToFrameAngle(angleInfo.getAngle() + 90)
        gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        if buildingDirection == DirectionFactory.getInstance().UP:
            self.rtsLayer2LogHelper.buildingAbove(self)
            if angle > 180 and angle < 360:
                self.rtsLayer2LogHelper.buildingChaseLeft(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.LEFT))
                if angle <= 190:
                    return True
            else:
                self.rtsLayer2LogHelper.buildingChaseRight(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.RIGHT))
                if angle >= 170:
                    return True
        elif buildingDirection == DirectionFactory.getInstance().DOWN:
            self.rtsLayer2LogHelper.buildingDown(self)
            if angle > 180 and angle < 360:
                self.rtsLayer2LogHelper.buildingChaseLeft(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.RIGHT))
                if angle > 315:
                    return True
            else:
                self.rtsLayer2LogHelper.buildingChaseRight(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.LEFT))
                if angle < 45:
                    return True
        elif buildingDirection == DirectionFactory.getInstance().LEFT:
            self.rtsLayer2LogHelper.buildingLeft()
            if angle > 90 and angle < 270:
                self.rtsLayer2LogHelper.buildingChaseDown(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.LEFT))
                if angle < 135:
                    return True
            else:
                self.rtsLayer2LogHelper.buildingChaseUp(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.RIGHT))
                if angle > 45:
                    return True
        elif buildingDirection == DirectionFactory.getInstance().RIGHT:
            self.rtsLayer2LogHelper.buildingRight()
            if angle > 90 and angle < 270:
                self.rtsLayer2LogHelper.buildingChaseDown(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.RIGHT))
                if angle > 225:
                    return True
            else:
                self.rtsLayer2LogHelper.buildingChaseUp(self, angle)
                self.getGameKeyEventList().add(gameKeyEventFactory.getInstanceForKey(self, Canvas.LEFT))
                if angle < 315 and angle > 180:
                    return True
        else:
            return True
        return False
    

    # throws Exception
    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.geographicMapCellPositionAreaBase.update(geographicMapInterface)
        return self.geographicMapCellPositionAreaBase.getSurroundingGeographicMapCellPositionList()
    

    def setSelected(self, selected: bool) -> None:
        super().setSelected(selected)
        if self.debug:
            if selected:
                self.waypointLogHelperP = WaypointSelectedLogHelper.getInstance()
                self.waypoint2LogHelperP = Waypoint2SelectedLogHelper.getInstance()
                self.waypointRunnableLogHelperP = WaypointRunnableSelectedLogHelper.getInstance()
            else:
                self.waypointLogHelperP = WaypointLogHelper.getInstance()
                self.waypoint2LogHelperP = Waypoint2LogHelper.getInstance()
                self.waypointRunnableLogHelperP = WaypointRunnableLogHelper.getInstance()
    

    def onDestroyed(self, destroyedEvent: DestroyedEvent) -> None:
        try:
            layerInterface: AllBinaryLayer = destroyedEvent.getLayerInterface()
            if layerInterface == self:
                DestroyedEventHandler.getInstance().removeListener(self)
                waypoint: WaypointBase = self.getWaypointBehavior().getWaypoint()
                waypoint.reset()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onDestroyed", e)
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.animation.NullIndexedAnimationFactory import NullIndexedAnimationFactory
from org.allbinary.animation.ProceduralAnimationInterfaceFactoryInterface import ProceduralAnimationInterfaceFactoryInterface
from org.allbinary.animation.transition.shake.ShakeAnimationListener import ShakeAnimationListener
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.GameTypeFactory import GameTypeFactory
from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
from org.allbinary.game.combat.destroy.event.DestroyedEventHandler import DestroyedEventHandler
from org.allbinary.game.health.Health import Health
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.identification.GroupFactory import GroupFactory
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
from org.allbinary.game.layer.building.event.BuildingEventHandler import BuildingEventHandler
from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
from org.allbinary.game.layer.waypoint.Waypoint2LogHelper import Waypoint2LogHelper
from org.allbinary.game.layer.waypoint.Waypoint2SelectedLogHelper import Waypoint2SelectedLogHelper
from org.allbinary.game.layer.waypoint.WaypointBase import WaypointBase
from org.allbinary.game.layer.waypoint.WaypointLogHelper import WaypointLogHelper
from org.allbinary.game.layer.waypoint.WaypointRunnableLogHelper import WaypointRunnableLogHelper
from org.allbinary.game.layer.waypoint.WaypointRunnableSelectedLogHelper import WaypointRunnableSelectedLogHelper
from org.allbinary.game.layer.waypoint.WaypointSelectedLogHelper import WaypointSelectedLogHelper
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.game.tick.NullTickable import NullTickable
from org.allbinary.game.tick.TickableInterface import TickableInterface
from org.allbinary.game.view.TileLayerPositionIntoViewPosition import TileLayerPositionIntoViewPosition
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.math.FrameUtil import FrameUtil
from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.GeographicMapDirectionUtil import GeographicMapDirectionUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.view.ViewPositionBase import ViewPositionBase
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer


