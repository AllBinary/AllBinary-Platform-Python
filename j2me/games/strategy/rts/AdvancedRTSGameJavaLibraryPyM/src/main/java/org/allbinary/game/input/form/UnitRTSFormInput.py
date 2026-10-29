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

from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput


class UnitRTSFormInput(RTSFormInput):
    DECAL_ID: int = SmallIntegerSingletonFactory.getInstance().getAt(23)

    def _init_fields(self) -> None:
        self.noMoneyGameNotificationEvent: GameNotificationEvent = None
        self.newUnitGameNotificationEvent: GameNotificationEvent = None
    

    def __init__(self, groupInterface: list[Group]) -> None:
        super().__init__(groupInterface)
        self._init_fields()
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.noMoneyGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NO_MONEY, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.newUnitGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NEW_UNIT, smallIntegerSingletonFactory.getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
        self.getHashtable().put(WorkWaypoint.ID, smallIntegerSingletonFactory.getAt(50))
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.noMoneyGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.newUnitGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    # throws Exception
    def processGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, itemIndex: int) -> None:
        super().process(layerManager)
        associatedRtsLayer2: RTSLayer = associatedRtsLayer
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = associatedRtsLayer2.geographicMapCellPositionAreaBase
        geographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionArea.getNextSurroundingGeographicMapCellPosition()
        self.getHashtable().put(Layer.ID, associatedRtsLayer)
        self.getHashtable().put(UnitRTSFormInput.DECAL_ID, (rtsPlayerLayerInterface).getDecalBasicColor())
        if self.newUnconstructedRTSLayerInterfaceArray[itemIndex] == CollidableDestroyableDamageableLayer.getNullInstance():
            self.newUnconstructedRTSLayerInterfaceArray[itemIndex] = self.getInstance(layerManager, item, geographicMapCellPosition)
        else:
            cellPoint: GPoint = geographicMapCellPosition.getPoint()
            rtsLayer: RTSLayer = self.newUnconstructedRTSLayerInterfaceArray[itemIndex]
            rtsLayer.setPosition(cellPoint.getX(), cellPoint.getY(), rtsLayer.getZP())
            geographicMapCompositeInterface: GeographicMapCompositeInterface = rtsLayer.allBinaryGameLayerManagerP
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            rtsLayer.geographicMapCellPositionAreaBase.update(geographicMapInterface)
        cellPoint: GPoint = geographicMapCellPosition.getMidPoint()
        rtsLayer: RTSLayer = self.newUnconstructedRTSLayerInterfaceArray[itemIndex]
        rtsLayer.setPosition(cellPoint.getX() - rtsLayer.getHalfWidth(), cellPoint.getY() - rtsLayer.getHalfHeight(), rtsLayer.getZP())
        self.attemptBuild(associatedRtsLayer2, rtsPlayerLayerInterface, layerManager, rtsLayer, itemIndex)
    

    # throws Exception
    def attemptBuild(self, associatedRtsLayer: RTSLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, layerInterface: RTSLayer, itemIndex: int) -> None:
        from org.allbinary.game.input.form.AssignWaypointsUtil import AssignWaypointsUtil
        from org.allbinary.game.input.form.PlayersSingletonFactory import PlayersSingletonFactory
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
            rtsPlayerLayerInterface.add(BuildingSound.getInstance())
            capital.removeMoney(cost)
            AssignWaypointsUtil.getInstance().set(layerInterface, associatedRtsLayer)
            layerManager.appendAt(layerInterface, PlayersSingletonFactory.total)
            advancedRTSPlayerLayerInterface: AdvancedRTSPlayerLayerInterface = rtsPlayerLayerInterface
            advancedPlayerOwnedRTSLayers: AdvancedPlayerOwnedRTSLayers = advancedRTSPlayerLayerInterface.getAdvancedPlayerOwnedRTSLayers()
            advancedPlayerOwnedRTSLayers.addUnit(layerInterface)
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.newUnitGameNotificationEvent)
        else:
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.noMoneyGameNotificationEvent)
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.game.layer.AdvancedPlayerOwnedRTSLayers import AdvancedPlayerOwnedRTSLayers
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.AdvancedRTSPlayerLayerInterface import AdvancedRTSPlayerLayerInterface
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.capital.Capital import Capital
from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
from org.allbinary.game.layer.waypoint.WorkWaypoint import WorkWaypoint
from org.allbinary.media.audio.BuildingSound import BuildingSound
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.GeographicMapCellPositionAreaBase import GeographicMapCellPositionAreaBase
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.Layer import Layer
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface


