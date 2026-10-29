# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.input.form

from __future__ import annotations

from org.allbinary.game.input.form.BuildingRTSFormInput import BuildingRTSFormInput


class BuildingAdvancedRTSFormInput(BuildingRTSFormInput):

    def _init_fields(self) -> None:
        self.atLeastOneHouseGameNotificationEvent: GameNotificationEvent = None
        self.BUILD_BUILDING_RTS_LAYER_EVENT: RTSLayerEvent = RTSLayerEvent(NullPathFindingLayer.NULL_PATH_FINDING_LAYER)
    

    def __init__(self, groupInterface: list[Group], isUnitProducer: bool) -> None:
        super().__init__(groupInterface, isUnitProducer)
        self._init_fields()
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.atLeastOneHouseGameNotificationEvent = GameNotificationEvent(self, "Build At Least One House First", SmallIntegerSingletonFactory.getInstance().getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.atLeastOneHouseGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    def isPositionBlocked(self) -> bool:
        if DropCellPositionHistory.getInstance().isCellPositionWithDrop(self.getSelectedGeographicCellPosition()) or WaypointCellPositionHistory.getInstance().isCellPositionWithDrop(self.getSelectedGeographicCellPosition()):
            return True
        else:
            return False
    

    # throws Exception
    def isBuildAttemptValid(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerInterface: RTSLayer) -> bool:
        advancedRTSPlayerLayerInterface: AdvancedRTSPlayerLayerInterface = rtsPlayerLayerInterface
        advancedPlayerOwnedRTSLayers: AdvancedPlayerOwnedRTSLayers = advancedRTSPlayerLayerInterface.getAdvancedPlayerOwnedRTSLayers()
        totalHouses: int = advancedPlayerOwnedRTSLayers.getHouseList().size()
        if totalHouses < 1 and layerInterface.getName().indexOf(" House") < 0:
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.atLeastOneHouseGameNotificationEvent)
            return False
        return super().isBuildAttemptValid(rtsPlayerLayerInterface, layerInterface)
    

    # throws Exception
    def add(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, layerInterface: RTSLayer) -> None:
        self.BUILD_BUILDING_RTS_LAYER_EVENT.setRtsLayer(layerInterface)
        BuildingEventHandler.getInstance().fireEvent(self.BUILD_BUILDING_RTS_LAYER_EVENT)
        if (rtsPlayerLayerInterface).isLocalPlayer():
            LocalPlayerBuildingEventHandler.getInstance().fireEvent(self.BUILD_BUILDING_RTS_LAYER_EVENT)
        super().add(rtsPlayerLayerInterface, layerManager, layerInterface)
from org.allbinary.game.layer.AdvancedPlayerOwnedRTSLayers import AdvancedPlayerOwnedRTSLayers
from org.allbinary.game.layer.AdvancedRTSPlayerLayerInterface import AdvancedRTSPlayerLayerInterface
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.building.event.BuildingEventHandler import BuildingEventHandler
from org.allbinary.game.layer.building.event.LocalPlayerBuildingEventHandler import LocalPlayerBuildingEventHandler
from org.allbinary.game.layer.waypoint.WaypointCellPositionHistory import WaypointCellPositionHistory
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory


