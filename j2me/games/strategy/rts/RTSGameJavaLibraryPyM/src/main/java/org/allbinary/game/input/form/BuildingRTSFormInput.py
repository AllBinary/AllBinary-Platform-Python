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
# package org.allbinary.game.input.form

from __future__ import annotations

from org.allbinary.game.input.form.RTSFormInput import RTSFormInput


class BuildingRTSFormInput(RTSFormInput):

    def _init_fields(self) -> None:
        self.isUnitProducer: bool = None
        self.buildOnPathGameNotificationEvent: GameNotificationEvent = None
        self.spotTakenGameNotificationEvent: GameNotificationEvent = None
        self.selectBuildSpotGameNotificationEvent: GameNotificationEvent = None
        self.roadCollisionGameNotificationEvent: GameNotificationEvent = None
        self.noMoneyGameNotificationEvent: GameNotificationEvent = None
        self.buildingCollisionGameNotificationEvent: GameNotificationEvent = None
        self.structureToCloseCollisionGameNotificationEvent: GameNotificationEvent = None
        self.buildingGameNotificationEvent: GameNotificationEvent = None
        self.mapEdgeGameNotificationEvent: GameNotificationEvent = None
        self.dropCellPositionHistory: DropCellPositionHistory = DropCellPositionHistory.getInstance()
    

    def __init__(self, groupInterface: list[Group], isUnitProducer: bool) -> None:
        super().__init__(groupInterface)
        self._init_fields()
        self.isUnitProducer = isUnitProducer
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.buildOnPathGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().BUILD_ON_PATH, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.spotTakenGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().SPOT_TAKEN, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.selectBuildSpotGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().SELECT_BUILD_SPOT, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.roadCollisionGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().ROAD_COLLISION, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.noMoneyGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NO_MONEY, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.buildingCollisionGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().BUILDING_COLLISION, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.structureToCloseCollisionGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().STRUCTURE_TO_CLOSE, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.buildingGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().BUILDING, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.mapEdgeGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().MAP_EDGE, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.buildOnPathGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.spotTakenGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.selectBuildSpotGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.roadCollisionGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.noMoneyGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.buildingCollisionGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.structureToCloseCollisionGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.buildingGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.mapEdgeGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    # throws Exception
    def processGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, itemIndex: int) -> None:
        super().process(layerManager)
        self.buildFromMotionInput(rtsPlayerLayerInterface, layerManager, item, itemIndex)
    

    def isPositionBlocked(self) -> bool:
        return self.dropCellPositionHistory.isCellPositionWithDrop(self.getSelectedGeographicCellPosition())
    

    def isDemoLocked(self, item: ABCustomItem) -> bool:
        factoryItem: LayerInterfaceFactoryImageItem = item
        layerInterfaceFactoryInterface: DemoLockedWithCostLayerInterfaceFactoryInterface = factoryItem.getLayerInterfaceFactoryInterface()
        if LockedUtil.getInstance().isLocked() and layerInterfaceFactoryInterface.isDemoLocked():
            return True
        else:
            return False
    

    # throws Exception
    def buildFromMotionInput(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, itemIndex: int) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(commonStrings.START, self, "buildFromMotionInput")
        if layerManager is None:
            raise RuntimeError()
        geographicMapCompositeInterface: GeographicMapCompositeInterface = layerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        if self.isDemoLocked(item):
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            LockedFeatureNotificationUtil.getInstance().fireWithColor(geographicMapInterface.getForegroundBasicColor())
            return
        geographicMapCellPosition: GeographicMapCellPosition = self.getSelectedGeographicCellPosition()
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            if not self.isPositionBlocked():
                geographicMapCellType: GeographicMapCellType = geographicMapInterface.getCellTypeAt(geographicMapCellPosition)
                raceTrackGeographicMapCellTypeFactory: RaceTrackGeographicMapCellTypeFactory = geographicMapInterface.getGeographicMapCellTypeFactory()
                if not raceTrackGeographicMapCellTypeFactory.isPath(geographicMapCellType):
                    if self.newUnconstructedRTSLayerInterfaceArray[itemIndex] == CollidableDestroyableDamageableLayer.getNullInstance():
                        self.newUnconstructedRTSLayerInterfaceArray[itemIndex] = self.getInstance(layerManager, item, geographicMapCellPosition)
                    else:
                        rtsLayer: RTSLayer = self.newUnconstructedRTSLayerInterfaceArray[itemIndex]
                        cellPoint: GPoint = geographicMapCellPosition.getPoint()
                        rtsLayer.setPosition(cellPoint.getX(), cellPoint.getY(), cellPoint.getZ())
                        rtsLayer.geographicMapCellPositionAreaBase.update(geographicMapInterface)
                    rtsLayer: RTSLayer = self.newUnconstructedRTSLayerInterfaceArray[itemIndex]
                    self.attemptBuild(rtsPlayerLayerInterface, layerManager, rtsLayer, itemIndex)
                else:
                    rtsPlayerLayerInterface.add(ErrorSound.getInstance())
                    if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                        GameNotificationEventHandler.getInstance().fireEvent(self.buildOnPathGameNotificationEvent)
            else:
                rtsPlayerLayerInterface.add(ErrorSound.getInstance())
                if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                    GameNotificationEventHandler.getInstance().fireEvent(self.spotTakenGameNotificationEvent)
        else:
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.selectBuildSpotGameNotificationEvent)
    

    # throws Exception
    def attemptBuild(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, layerInterface: RTSLayer, itemIndex: int) -> bool:
        self.logUtil.putF(str(StringMaker().append("Layer: ").append(StringUtil.getInstance().toString(layerInterface))), self, "attemptBuild")
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = layerInterface.geographicMapCellPositionAreaBase
        occupyList: BasicArrayList = geographicMapCellPositionArea.getOccupyingGeographicMapCellPositionList()
        if not self.isBuildAttemptValid(rtsPlayerLayerInterface, layerInterface):
            return False
        geographicMapCellType: GeographicMapCellType = None
        for index in range(occupyList.size() - 1, 0 - 1, -1):
            geographicMapCompositeInterface: GeographicMapCompositeInterface = layerManager
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            geographicMapCellType = geographicMapInterface.getCellTypeAt(occupyList.get(index))
            raceTrackGeographicMapCellTypeFactory: RaceTrackGeographicMapCellTypeFactory = geographicMapInterface.getGeographicMapCellTypeFactory()
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
            self.add(rtsPlayerLayerInterface, layerManager, layerInterface)
            return True
        else:
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.noMoneyGameNotificationEvent)
            return False
    

    # throws Exception
    def isBuildAttemptValid(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerInterface: RTSLayer) -> bool:
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = layerInterface.geographicMapCellPositionAreaBase
        occupyList: BasicArrayList = geographicMapCellPositionArea.getOccupyingGeographicMapCellPositionList()
        if self.dropCellPositionHistory.anyCellPositionWithDrop(occupyList):
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.buildingCollisionGameNotificationEvent)
            return False
        if self.isUnitProducer and self.dropCellPositionHistory.anyCellPositionWithDrop(geographicMapCellPositionArea.getSurroundingGeographicMapCellPositionList()):
            rtsPlayerLayerInterface.add(ErrorSound.getInstance())
            if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                GameNotificationEventHandler.getInstance().fireEvent(self.structureToCloseCollisionGameNotificationEvent)
            return False
        else:
            if self.isSurroundingCellsOffMap(layerInterface):
                rtsPlayerLayerInterface.add(ErrorSound.getInstance())
                if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                    GameNotificationEventHandler.getInstance().fireEvent(self.mapEdgeGameNotificationEvent)
                return False
        return True
    

    # throws Exception
    def add(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, layerInterface: RTSLayer) -> None:
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = layerInterface.geographicMapCellPositionAreaBase
        occupyList: BasicArrayList = geographicMapCellPositionArea.getOccupyingGeographicMapCellPositionList()
        self.dropCellPositionHistory.addAll(occupyList, layerInterface)
        rtsPlayerGameInput: RTSPlayerGameInput = rtsPlayerLayerInterface.getPlayerGameInput()
        rtsPlayerGameInput.setSelectedRTSLayer(layerInterface, self.getSelectedGeographicCellPosition())
        layerManager.append(layerInterface)
        rtsPlayerLayerInterface.add(BuildingSound.getInstance())
        if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
            GameNotificationEventHandler.getInstance().fireEvent(self.buildingGameNotificationEvent)
    

    def isSurroundingCellsOffMap(self, layerInterface: RTSLayer) -> bool:
        geographicMapCellPositionArea: GeographicMapCellPositionAreaBase = layerInterface.geographicMapCellPositionAreaBase
        occupyList: BasicArrayList = geographicMapCellPositionArea.getOccupyingGeographicMapCellPositionList()
        surroundList: BasicArrayList = geographicMapCellPositionArea.getSurroundingGeographicMapCellPositionList()
        occupySize: int = occupyList.size()
        surroundSize: int = surroundList.size()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("occupySize: ")
        stringBuffer.appendint(occupySize)
        stringBuffer.append(" surroundSize: ")
        stringBuffer.appendint(surroundSize)
        stringBuffer.append(" surroundList: ")
        stringBuffer.append(StringUtil.getInstance().toString(surroundList))
        self.logUtil.putF(str(stringBuffer), self, "isSurroundingCellsOffMap")
        isSurroundOffMap: bool = False
        if occupySize == 1 and surroundSize != 8:
            isSurroundOffMap = True
        elif occupySize == 4 and surroundSize != 12:
            isSurroundOffMap = True
        if occupySize == 0 or isSurroundOffMap:
            return True
        else:
            return False
from org.allbinary.game.input.RTSPlayerGameInput import RTSPlayerGameInput
from org.allbinary.game.layer.DemoLockedWithCostLayerInterfaceFactoryInterface import DemoLockedWithCostLayerInterfaceFactoryInterface
from org.allbinary.game.layer.GeographicMapCellPositionAreaBase import GeographicMapCellPositionAreaBase
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.capital.Capital import Capital
from org.allbinary.game.layer.item.LayerInterfaceFactoryImageItem import LayerInterfaceFactoryImageItem
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.media.audio.BuildingSound import BuildingSound
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.system.security.licensing.LockedFeatureNotificationUtil import LockedFeatureNotificationUtil
from org.allbinary.logic.system.security.licensing.LockedUtil import LockedUtil
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypeFactory import RaceTrackGeographicMapCellTypeFactory


