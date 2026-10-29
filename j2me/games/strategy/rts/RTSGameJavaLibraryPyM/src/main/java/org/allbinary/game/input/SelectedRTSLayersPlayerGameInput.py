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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.PlayerGameInput import PlayerGameInput


class SelectedRTSLayersPlayerGameInput(PlayerGameInput):

    def _init_fields(self) -> None:
        self.inputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.list_: BasicArrayList = None
        self.isSingleKeyProcessing: bool = Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_REPEAT_PRESS) or Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_PRESS)
        self.selectedRTSLayersList: BasicArrayList = BasicArrayListD()
        self.preSelectedRTSLayersList: BasicArrayList = BasicArrayListD()
        self.paintSelectedRTSLayersList: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.rtsPlayerLayerInterface: RTSPlayerLayerInterface = None
        self.selectRTSLayerVisitorInterface: Visitor = None
        self.upgradeGameNotificationEvent: GameNotificationEvent = None
        self.noMoneyGameNotificationEvent: GameNotificationEvent = None
        self.downgradeGameNotificationEvent: GameNotificationEvent = None
    

    def __init__(self, towerInfoPaintable: RTSLayerInfoPaintable, rtsPlayerLayerInterface: RTSPlayerLayerInterface, list_: BasicArrayList, playerInputId: int, selectRTSLayerVisitorFactoryInterface: SelectRTSLayerVisitorFactoryInterface) -> None:
        super().__init__(list_, BasicArrayListD(), playerInputId)
        self._init_fields()
        self.initInputProcessors()
        self.rtsPlayerLayerInterface = rtsPlayerLayerInterface
        self.list_ = list_
        self.selectRTSLayerVisitorInterface = selectRTSLayerVisitorFactoryInterface.create(self)
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.upgradeGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().UPGRADE, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.noMoneyGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NO_MONEY, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        self.downgradeGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().DOWNGRADE, smallIntegerSingletonFactory.getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.upgradeGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.noMoneyGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
        self.downgradeGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    def isSelected(self, rtsLayer: RTSLayer) -> bool:
        if self.selectedRTSLayersList.contains(rtsLayer):
            return True
        else:
            return False
    

    # throws Exception
    def upgrade(self) -> None:
        anyChanged: bool = False
        for index in range(self.selectedRTSLayersList.size() - 1, 0 - 1, -1):
            rtsLayer: RTSLayer = self.selectedRTSLayersList.get(index)
            if rtsLayer.isUpgradeable():
                capital: Capital = self.rtsPlayerLayerInterface.getCapital()
                upgradeCost: int = rtsLayer.getUpgradeCost()
                if upgradeCost <= capital.getTotalMoney():
                    anyChanged = True
                    self.rtsPlayerLayerInterface.add(UpgradeSound.getInstance())
                    rtsLayer.upgrade()
                    capital.removeMoney(upgradeCost)
                    if not self.rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                        GameNotificationEventHandler.getInstance().fireEvent(self.upgradeGameNotificationEvent)
                else:
                    self.rtsPlayerLayerInterface.add(ErrorSound.getInstance())
                    if not self.rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                        GameNotificationEventHandler.getInstance().fireEvent(self.noMoneyGameNotificationEvent)
        if anyChanged:
            rtsPlayerGameInput: RTSPlayerGameInput = (self.rtsPlayerLayerInterface.getPlayerGameInput())
            rtsPlayerGameInput.updatePaintable()
    

    # throws Exception
    def downgrade(self) -> None:
        anyChanged: bool = False
        index = self.selectedRTSLayersList.size()
        while (index := index - 1) >= 0:
            rtsLayer: RTSLayer = self.selectedRTSLayersList.get(index)
            if rtsLayer.isDowngradeable():
                anyChanged = True
                self.rtsPlayerLayerInterface.add(DowngradeSound.getInstance())
                downgradeCost: int = rtsLayer.getDowngradeCost()
                rtsLayer.downgrade()
                capital: Capital = self.rtsPlayerLayerInterface.getCapital()
                capital.addMoney(downgradeCost)
                if not self.rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                    GameNotificationEventHandler.getInstance().fireEvent(self.downgradeGameNotificationEvent)
        if anyChanged:
            rtsPlayerGameInput: RTSPlayerGameInput = (self.rtsPlayerLayerInterface.getPlayerGameInput())
            rtsPlayerGameInput.updatePaintable()
    

    def initInputProcessors(self) -> None:
        from org.allbinary.game.input.SelectedRTSLayersPlayerUpgradeGameInputProcessor import SelectedRTSLayersPlayerUpgradeGameInputProcessor
        from org.allbinary.game.input.SelectedRTSLayersPlayerDowngradeGameInputProcessor import SelectedRTSLayersPlayerDowngradeGameInputProcessor
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        self.inputProcessorArray[Canvas.KEY_NUM1] = SelectedRTSLayersPlayerUpgradeGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_NUM3] = SelectedRTSLayersPlayerDowngradeGameInputProcessor(self)
        GameInputProcessorUtil.init(self.inputProcessorArray)
    

    # throws Exception
    def processInputKey(self, key: int) -> None:
        if self.selectedRTSLayersList is not None:
            self.inputProcessorArray[key].processEvent(AllBinaryGameLayerManager.getNullInstance(), GameKeyEvent.NONE)
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        try:
            size: int = self.list_.size()
            key: int = 0
            for index in range(0, size):
                gameKeyEvent: GameKeyEvent = self.list_.get(index)
                key = gameKeyEvent.getKey()
                self.processInputKey(key)
            if self.isSingleKeyProcessing:
                self.clear()
            else:
                self.update()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.PROCESS_INPUT, e)
    

    def getSelectedBasicArrayList(self) -> BasicArrayList:
        return self.selectedRTSLayersList
    

    def addSelectedRTSLayer(self, selectedLayer: RTSLayer) -> None:
        self.paintSelectedRTSLayersList = BasicArrayListUtil.getInstance().getImmutableInstance()
        if selectedLayer == CollidableDestroyableDamageableLayer.getNullInstance():
            self.deselectAll()
            self.selectedRTSLayersList.clear()
        else:
            if not self.selectedRTSLayersList.contains(selectedLayer):
                self.selectedRTSLayersList.add(selectedLayer)
        self.paintSelectedRTSLayersList = self.selectedRTSLayersList
    

    def setSelectedRTSLayer(self, selectedLayer: CollidableDestroyableDamageableLayer) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Selected Layer: ")
        if selectedLayer is not None:
            stringBuffer.append(selectedLayer.getName())
        self.logUtil.putF(str(stringBuffer), self, "setSelectedRTSLayer")
        self.paintSelectedRTSLayersList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.selectRTSLayerVisitorInterface.visit(selectedLayer)
        self.deselectAll()
        if self.selectedRTSLayersList.size() > 0:
            self.getPreSelectedRTSLayersList().clear()
            tempList: BasicArrayList = self.getPreSelectedRTSLayersList()
            self.preSelectedRTSLayersList = self.selectedRTSLayersList
            self.selectedRTSLayersList = tempList
            self.logUtil.putF(str(StringMaker().append("Preselected: ").append(str(self.preSelectedRTSLayersList))), self, "setSelectedRTSLayer")
        if selectedLayer != CollidableDestroyableDamageableLayer.getNullInstance():
            self.selectedRTSLayersList.add(selectedLayer)
        self.paintSelectedRTSLayersList = self.selectedRTSLayersList
    

    def getLastSelectedRtsLayer(self) -> CollidableDestroyableDamageableLayer:
        if self.isAnyRTSLayerSelected():
            return self.selectedRTSLayersList.get(self.selectedRTSLayersList.size() - 1)
        else:
            return CollidableDestroyableDamageableLayer.getNullInstance()
    

    def selectAllPreselected(self) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Select all Preselected: ")
        stringBuffer.append(str(self.preSelectedRTSLayersList))
        self.logUtil.putF(str(stringBuffer), self, "selectAllPreselected")
        for index in range(self.preSelectedRTSLayersList.size() - 1, 0 - 1, -1):
            rtsLayer: RTSLayer = self.preSelectedRTSLayersList.get(index)
            rtsLayer.select()
    

    def deselectAllPreselected(self) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Deselect all Preselected: ")
        stringBuffer.append(str(self.preSelectedRTSLayersList))
        self.logUtil.putF(str(stringBuffer), self, "deselectAllPreselected")
        for index in range(self.preSelectedRTSLayersList.size() - 1, 0 - 1, -1):
            rtsLayer: RTSLayer = self.preSelectedRTSLayersList.get(index)
            rtsLayer.deselect()
        self.preSelectedRTSLayersList.clear()
    

    def deselectAll(self) -> None:
        for index in range(self.selectedRTSLayersList.size() - 1, 0 - 1, -1):
            rtsLayer: RTSLayer = self.selectedRTSLayersList.get(index)
            rtsLayer.deselect()
    

    def isAnyRTSLayerSelected(self) -> bool:
        if self.selectedRTSLayersList.size() == 0:
            return False
        return True
    

    def getPaintSelectedRTSLayersList(self) -> BasicArrayList:
        return self.paintSelectedRTSLayersList
    

    def getPreSelectedRTSLayersList(self) -> BasicArrayList:
        return self.preSelectedRTSLayersList
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSLayerInfoPaintable import RTSLayerInfoPaintable
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.capital.Capital import Capital
from org.allbinary.media.audio.DowngradeSound import DowngradeSound
from org.allbinary.media.audio.UpgradeSound import UpgradeSound
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.util.visitor.Visitor import Visitor
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.game.input.InputFactory import InputFactory


