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


class RTSPlayerGameInput(PlayerGameInput):

    def _init_fields(self) -> None:
        self.inputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.removeInputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.inputList: BasicArrayList = None
        self.isSingleKeyProcessing: bool = Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_REPEAT_PRESS) or Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_PRESS)
        self.gameCanvas: AllBinaryGameCanvas = None
        self.motionGestureInputList: BasicArrayList = BasicArrayListD()
        self.scrollPlayerGameInput: ScrollMapPlayerGameInput = None
        self.selectedRTSLayerPlayerGameInput: SelectedRTSLayersPlayerGameInput = None
        self.towerInfoPaintable: RTSLayerInfoPaintable = None
        self.rtsPlayerLayerInterface: RTSPlayerLayerInterface = None
        self.layerPositionFinderInterface: LayerPositionFinderInterface = None
        self.selectedRtsFormInput: RTSFormInput = NullRTSFormInputFactory.getInstance()
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas, inputList: BasicArrayList, playerInputId: int, towerInfoPaintable: RTSLayerInfoPaintable, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerPositionFinderInterface: LayerPositionFinderInterface, selectRTSLayerVisitorFactoryInterface: SelectRTSLayerVisitorFactoryInterface) -> None:
        from org.allbinary.game.input.SelectedRTSLayersPlayerGameInput import SelectedRTSLayersPlayerGameInput
        from org.allbinary.game.input.ScrollMapPlayerGameInput import ScrollMapPlayerGameInput
        super().__init__(inputList, BasicArrayListD(), playerInputId)
        self._init_fields()
        self.initInputProcessors()
        self.gameCanvas = gameCanvas
        self.inputList = inputList
        self.towerInfoPaintable = towerInfoPaintable
        self.rtsPlayerLayerInterface = rtsPlayerLayerInterface
        self.selectedRTSLayerPlayerGameInput = SelectedRTSLayersPlayerGameInput(self.getRTSLayerInfoPaintable(), self.getRtsPlayerLayerInterface(), self.inputList, playerInputId, selectRTSLayerVisitorFactoryInterface)
        if self.rtsPlayerLayerInterface != NullRTSLayer.NULL_RTS_LAYER:
            self.setSelectedRtsFormInput(self.rtsPlayerLayerInterface.getRTSFormInput())
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.gameCanvas.getLayerManager()
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.scrollPlayerGameInput = ScrollMapPlayerGameInput(geographicMapInterface, self.inputList, playerInputId)
        self.layerPositionFinderInterface = layerPositionFinderInterface
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        self.selectedRTSLayerPlayerGameInput.setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        if self.selectedRtsFormInput != NullRTSFormInputFactory.getInstance():
            self.selectedRtsFormInput.setAllBinaryGameLayerManager(allBinaryGameLayerManager)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "onDisplayChangeEvent")
            self.getRTSLayerInfoPaintable().update()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "onDisplayChangeEvent", e)
    

    # throws Exception
    def left(self) -> None:
        self.rtsPlayerLayerInterface.getCurrentScrollSelectionForm().processInputKey(Canvas.LEFT)
    

    # throws Exception
    def right(self) -> None:
        self.rtsPlayerLayerInterface.getCurrentScrollSelectionForm().processInputKey(Canvas.RIGHT)
    

    def initInputProcessors(self) -> None:
        from org.allbinary.game.input.RTSPlayerLeftGameInputProcessor import RTSPlayerLeftGameInputProcessor
        from org.allbinary.game.input.RTSPlayerRightGameInputProcessor import RTSPlayerRightGameInputProcessor
        from org.allbinary.game.input.RTSPlayerFireGameInputProcessor import RTSPlayerFireGameInputProcessor
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        self.inputProcessorArray[Canvas.LEFT] = RTSPlayerLeftGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_NUM0] = self.inputProcessorArray[Canvas.LEFT]
        self.inputProcessorArray[Canvas.RIGHT] = RTSPlayerRightGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_POUND] = self.inputProcessorArray[Canvas.RIGHT]
        self.removeInputProcessorArray[Canvas.KEY_NUM1] = RTSPlayerFireGameInputProcessor(self)
        self.removeInputProcessorArray[Canvas.KEY_NUM3] = self.removeInputProcessorArray[Canvas.KEY_NUM1]
        self.removeInputProcessorArray[Canvas.KEY_NUM3] = self.removeInputProcessorArray[Canvas.KEY_NUM1]
        self.removeInputProcessorArray[Canvas.LEFT] = self.removeInputProcessorArray[Canvas.KEY_NUM1]
        self.removeInputProcessorArray[Canvas.RIGHT] = self.removeInputProcessorArray[Canvas.KEY_NUM1]
        self.removeInputProcessorArray[Canvas.KEY_NUM0] = self.removeInputProcessorArray[Canvas.KEY_NUM1]
        self.removeInputProcessorArray[Canvas.KEY_POUND] = self.removeInputProcessorArray[Canvas.KEY_NUM1]
        GameInputProcessorUtil.init(self.inputProcessorArray)
        GameInputProcessorUtil.init(self.removeInputProcessorArray)
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        try:
            self.processMotionInput(layerManager)
            size: int = self.inputList.size()
            key: int = 0
            for index in range(0, size):
                gameKeyEvent: GameKeyEvent = self.inputList.get(index)
                key = gameKeyEvent.getKey()
                self.getScrollPlayerGameInput().processInputKey(key)
                self.getSelectedBuildingPlayerGameInput().processInputKey(key)
                self.inputProcessorArray[key].processEvent(layerManager, gameKeyEvent)
                self.removeInputProcessorArray[key].processEvent(layerManager, gameKeyEvent)
            if self.isIsSingleKeyProcessing():
                self.clear()
            else:
                self.update()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.PROCESS_INPUT, e)
    

    # throws Exception
    def processMotionInput(self, layerManager: AllBinaryLayerManager) -> None:
        pass
    

    # throws Exception
    def select(self, motionGestureEvent: MotionGestureEvent) -> None:
        point: GPoint = motionGestureEvent.getCurrentPoint()
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.gameCanvas.getLayerManager()
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        x: int = point.getX() + allBinaryTiledLayer.getXP()
        y: int = point.getY() + allBinaryTiledLayer.getYP()
        geographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(x, y)
        if geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            SecondaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
            layer: AllBinaryLayer = self.layerPositionFinderInterface.getLayerInterface(geographicMapCellPosition)
            if layer == AllBinaryLayer.NULL_ALLBINARY_LAYER:
                layer = CollidableDestroyableDamageableLayer.getNullInstance()
            else:
                geographicMapCellPosition = geographicMapInterface.getCellPositionAtXY(layer.getXP(), layer.getYP())
            foundRTSLayer: CollidableDestroyableDamageableLayer = layer
            self.setSelectedRTSLayer(foundRTSLayer, geographicMapCellPosition)
        else:
            commonLabels: CommonLabels = CommonLabels.getInstance()
            self.logUtil.putF(str(StringMaker().append("Off Of Map -").append(commonLabels.WIDTH_LABEL).appendint(int(allBinaryTiledLayer.getWidth())).append(commonLabels.HEIGHT_LABEL).appendint(int(allBinaryTiledLayer.getHeight()))), self, "select")
    

    # throws Exception
    def setSelectedRTSLayer(self, rtsLayer: CollidableDestroyableDamageableLayer, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.getSelectedBuildingPlayerGameInput().setSelectedRTSLayer(rtsLayer)
    

    def paint(self, graphics: Graphics) -> None:
        geographicMapCellPosition: GeographicMapCellPosition = self.getSelectedRtsFormInput().getSelectedGeographicCellPosition()
        geographicMapCompositeInterface: GeographicMapCompositeInterface = self.gameCanvas.getLayerManager()
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        graphics.setColor(int(BasicColorFactory.getInstance().GREEN))
        list_: BasicArrayList = self.getSelectedBuildingPlayerGameInput().getPaintSelectedRTSLayersList()
        width: int = 0
        height: int = 0
        if list_.size() > 0:
            for index in range(list_.size() - 1, 0 - 1, -1):
                rtsLayer: RTSLayer = list_.get(index)
                width = rtsLayer.getWidth()
                height = rtsLayer.getHeight()
                graphics.drawRect(rtsLayer.getXP() - allBinaryTiledLayer.getXP(), rtsLayer.getYP() - allBinaryTiledLayer.getYP(), width, height)
        elif geographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            point: GPoint = geographicMapCellPosition.getPoint()
            width = allBinaryTiledLayer.getCellWidth()
            height = allBinaryTiledLayer.getCellHeight()
            graphics.drawRect(point.getX() - allBinaryTiledLayer.getXP(), point.getY() - allBinaryTiledLayer.getYP(), width, height)
    

    def updatePaintable(self) -> None:
        pass
    

    def getSelectedBuildingPlayerGameInput(self) -> SelectedRTSLayersPlayerGameInput:
        return self.selectedRTSLayerPlayerGameInput
    

    def getSelectedRtsFormInput(self) -> RTSFormInput:
        return self.selectedRtsFormInput
    

    def setSelectedRtsFormInput(self, selectedRtsFormInput: RTSFormInput) -> None:
        self.logUtil.putF(str(StringMaker().append("RTSFormInput: ").append(StringUtil.getInstance().toString(selectedRtsFormInput))), self, "setSelectedRtsFormInput")
        self.selectedRtsFormInput = selectedRtsFormInput
    

    def getRtsPlayerLayerInterface(self) -> RTSPlayerLayerInterface:
        return self.rtsPlayerLayerInterface
    

    def getRTSLayerInfoPaintable(self) -> RTSLayerInfoPaintable:
        return self.towerInfoPaintable
    

    def getMotionGestureInputList(self) -> BasicArrayList:
        return self.motionGestureInputList
    

    def getGameCanvas(self) -> AllBinaryGameCanvas:
        return self.gameCanvas
    

    def isIsSingleKeyProcessing(self) -> bool:
        return self.isSingleKeyProcessing
    

    def getScrollPlayerGameInput(self) -> ScrollMapPlayerGameInput:
        return self.scrollPlayerGameInput
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSLayerInfoPaintable import RTSLayerInfoPaintable
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.form.NullRTSFormInputFactory import NullRTSFormInputFactory
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.layer.NullRTSLayer import NullRTSLayer
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
from org.allbinary.media.audio.SelectSound import SelectSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.game.input.InputFactory import InputFactory


