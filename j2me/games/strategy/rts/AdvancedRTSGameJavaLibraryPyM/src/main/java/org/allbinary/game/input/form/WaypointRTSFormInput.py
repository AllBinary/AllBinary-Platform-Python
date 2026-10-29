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
# package org.allbinary.game.input.form

from __future__ import annotations

from org.allbinary.game.input.form.RTSFormInput import RTSFormInput


class WaypointRTSFormInput(RTSFormInput):

    def _init_fields(self) -> None:
        self.WAYPOINT_EVENT: RTSLayerEvent = RTSLayerEvent(NullRTSLayer.NULL_RTS_LAYER)
        self.dragToSpotGameNotificationEvent: GameNotificationEvent = None
        self.spotTakenGameNotificationEvent: GameNotificationEvent = None
        self.buildingCollisionGameNotificationEvent: GameNotificationEvent = None
        self.roadCollisionGameNotificationEvent: GameNotificationEvent = None
        self.newWaypointGameNotificationEvent: GameNotificationEvent = None
        self.noMoneyGameNotificationEvent: GameNotificationEvent = None
        self.isPrimaryWaypointCreator: bool = None
        self.stickyAssociatedRtsLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
    

    def __init__(self, groupInterface: list[Group], isPrimaryWaypointCreator: bool) -> None:
        super().__init__(groupInterface)
        self._init_fields()
        self.isPrimaryWaypointCreator = isPrimaryWaypointCreator
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.dragToSpotGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().DRAG_TO_SPOT, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.spotTakenGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().SPOT_TAKEN, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.buildingCollisionGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().BUILDING_COLLISION, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.roadCollisionGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().ROAD_COLLISION, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.newWaypointGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NEW_WAYPOINT, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.noMoneyGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NO_MONEY, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.dragToSpotGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.spotTakenGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.buildingCollisionGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.roadCollisionGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.newWaypointGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.noMoneyGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    # throws Exception
    def processAtPoint(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, point: GPoint) -> None:
        super().process(layerManager)
        if self.isStickyItemSelected() or associatedRtsLayer == CollidableDestroyableDamageableLayer.getNullInstance():
            if self.isStickyItemSelected() and associatedRtsLayer == CollidableDestroyableDamageableLayer.getNullInstance():
                geographicMapCompositeInterface: GeographicMapCompositeInterface = layerManager
                geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
                allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
                x: int = point.getX() + allBinaryTiledLayer.getXP()
                y: int = point.getY() + allBinaryTiledLayer.getYP()
                geographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXY(x, y)
                self.processCellPosition(rtsPlayerLayerInterface, layerManager, geographicMapCellPosition)
            else:
                if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                    GameNotificationEventHandler.getInstance().fireEvent(self.dragToSpotGameNotificationEvent)
        else:
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.spotTakenGameNotificationEvent)
    

    # throws Exception
    def processCellPosition(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        itemIndex: int = self.getSelectedStickyItemIndex()
        if self.newUnconstructedRTSLayerInterfaceArray[itemIndex] == CollidableDestroyableDamageableLayer.getNullInstance():
            self.newUnconstructedRTSLayerInterfaceArray[itemIndex] = self.getInstance(layerManager, self.getSelectedStickyItem(), geographicMapCellPosition)
        else:
            cellPoint: GPoint = geographicMapCellPosition.getPoint()
            rtsLayer: RTSLayer = self.newUnconstructedRTSLayerInterfaceArray[itemIndex]
            rtsLayer.setPosition(cellPoint.getX(), cellPoint.getY(), rtsLayer.getZP())
            geographicMapCompositeInterface: GeographicMapCompositeInterface = rtsLayer.allBinaryGameLayerManagerP
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            rtsLayer.geographicMapCellPositionAreaBase.update(geographicMapInterface)
        self.attemptBuild(rtsPlayerLayerInterface, layerManager, self.newUnconstructedRTSLayerInterfaceArray[itemIndex], itemIndex)
    

    # throws Exception
    def processStickyGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, index: int) -> None:
        self.logUtil.putF("Set Sticking Item: " + str(item), self, "processSticky")
        self.setSelectedStickyItem(item)
        self.setSelectedStickyItemIndex(index)
        self.setStickyItemSelected(True)
        self.stickyAssociatedRtsLayer = associatedRtsLayer
        self.getHashtable().put(Layer.ID, associatedRtsLayer)
    

    # throws Exception
    def attemptBuild(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, layerInterface: RTSLayer, itemIndex: int) -> bool:
        self.logUtil.putF("Layer: " + str(layerInterface), self, "attemptBuild")
        if layerInterface is None:
            self.logUtil.put("Layer was null", self, "attemptBuild", Exception())
            return False
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = layerInterface.geographicMapCellPositionAreaBase
        list_: BasicArrayList = geographicMapCellPositionArea.getOccupyingGeographicMapCellPositionList()
        if DropCellPositionHistory.getInstance().anyCellPositionWithDrop(list_) or WaypointCellPositionHistory.getInstance().anyCellPositionWithDrop(list_):
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.buildingCollisionGameNotificationEvent)
            return False
        geographicMapCompositeInterface: GeographicMapCompositeInterface = layerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        raceTrackGeographicMapCellTypeFactory: RaceTrackGeographicMapCellTypeFactory = geographicMapInterface.getGeographicMapCellTypeFactory()
        geographicMapCellType: GeographicMapCellType = None
        index = list_.size()
        while (index := index - 1) >= 0:
            geographicMapCellType = geographicMapInterface.getCellTypeAt(list_.get(index))
            if raceTrackGeographicMapCellTypeFactory.isPath(geographicMapCellType):
                rtsPlayerLayerInterface.add(ErrorSound.getInstance())
                if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                    GameNotificationEventHandler.getInstance().fireEvent(self.roadCollisionGameNotificationEvent)
                return False
        cost: int = layerInterface.getCost()
        capital: Capital = rtsPlayerLayerInterface.getCapital()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Trying to Build: ")
        stringBuffer.append(layerInterface.getName())
        stringBuffer.append(" for: $")
        stringBuffer.appendint(cost)
        stringBuffer.append(" with ")
        stringBuffer.appendint(int(capital.getTotalMoney()))
        self.logUtil.putF(str(stringBuffer), self, "attemptBuild")
        if cost <= capital.getTotalMoney():
            layerInterface.construct(rtsPlayerLayerInterface)
            self.newUnconstructedRTSLayerInterfaceArray[itemIndex] = CollidableDestroyableDamageableLayer.getNullInstance()
            capital.removeMoney(cost)
            WaypointCellPositionHistory.getInstance().addList(list_, layerInterface)
            geographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXY(layerInterface.getXP(), layerInterface.getYP())
            waypointLayer: WaypointLayer = layerInterface
            self.addWayPoint(waypointLayer)
            rtsPlayerGameInput: RTSPlayerGameInput = rtsPlayerLayerInterface.getPlayerGameInput()
            rtsPlayerGameInput.setSelectedRTSLayer(layerInterface, geographicMapCellPosition)
            advancedRTSPlayerLayerInterface: AdvancedRTSPlayerLayerInterface = rtsPlayerLayerInterface
            advancedRTSPlayerLayerInterface.getAdvancedPlayerOwnedRTSLayers().addWaypoint(layerInterface)
            layerManager.append(layerInterface)
            waypointAvancedRTSGameLayer: AdvancedRTSGameLayer = waypointLayer
            rtsPlayerLayerInterface.add(waypointAvancedRTSGameLayer.getWaypointBehavior().getWaypoint().getSound())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.newWaypointGameNotificationEvent)
            return True
        else:
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.noMoneyGameNotificationEvent)
            return False
    

    # throws Exception
    def addWayPoint(self, layerInterface: WaypointLayer) -> None:
        from org.allbinary.game.input.form.PrimaryWaypointHelper import PrimaryWaypointHelper
        stickyAssociatedAdvandedRtsLayer: AdvancedRTSGameLayer = self.stickyAssociatedRtsLayer
        list_: BasicArrayList = stickyAssociatedAdvandedRtsLayer.getWaypointBehavior().getOwnedWaypointList()
        RTSLayerUtil.getInstance().destroyAndClear(list_)
        list_.add(layerInterface)
        if self.isPrimaryWaypointCreator:
            PrimaryWaypointHelper.getInstance().setWaypointLayer(layerInterface)
        self.WAYPOINT_EVENT.setRtsLayer(layerInterface)
        WaypointEventHandlerFactory.getInstance(layerInterface.getGroupInterface()[0]).fireEvent(self.WAYPOINT_EVENT)
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.game.input.RTSPlayerGameInput import RTSPlayerGameInput
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.AdvancedRTSPlayerLayerInterface import AdvancedRTSPlayerLayerInterface
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.RTSLayerUtil import RTSLayerUtil
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.capital.Capital import Capital
from org.allbinary.game.layer.waypoint.WaypointCellPositionHistory import WaypointCellPositionHistory
from org.allbinary.game.layer.waypoint.WaypointLayer import WaypointLayer
from org.allbinary.game.layer.waypoint.event.WaypointEventHandlerFactory import WaypointEventHandlerFactory
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.layer.GeographicMapCellPositionAreaBase import GeographicMapCellPositionAreaBase
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.layer.NullRTSLayer import NullRTSLayer
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.Layer import Layer
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypeFactory import RaceTrackGeographicMapCellTypeFactory


