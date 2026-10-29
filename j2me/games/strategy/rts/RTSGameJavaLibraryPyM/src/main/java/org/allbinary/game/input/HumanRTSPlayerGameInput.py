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

from org.allbinary.input.motion.gesture.observer.BaseMotionGestureEventListener import BaseMotionGestureEventListener
from org.allbinary.game.input.RTSPlayerGameInput import RTSPlayerGameInput


class HumanRTSPlayerGameInput(RTSPlayerGameInput, BaseMotionGestureEventListener):

    def _init_fields(self) -> None:
        self.isDragging: bool = False
        self.gameStateFactory: GameStateFactory = GameStateFactory.getInstance()
        self.rectangleCollisionUtil: RectangleCollisionUtil = RectangleCollisionUtil.getInstance()
        self.touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
        self.PRESSED: MotionGestureInput = self.touchMotionGestureFactory.PRESSED
        self.RELEASED: MotionGestureInput = self.touchMotionGestureFactory.RELEASED
        self.touchButtonsBuilderFactory: TouchButtonsBuilderFactory = None
        self.notYoursGameNotificationEvent: GameNotificationEvent = None
        self.selectedRtsLayer: CollidableDestroyableDamageableLayer = CollidableDestroyableDamageableLayer.getNullInstance()
        self.startPoint: GPoint = PointFactory.getInstance().ZERO_ZERO
        self.endPoint: GPoint = PointFactory.getInstance().ZERO_ZERO
        self.POSSIBLE: str = "Possible: "
        self.AT: str = "At: "
        self.METHOD: str = "makeSelection"
        self.ADDING: str = "Adding: "
        self.SPACE: str = CommonSeps.getInstance().SPACE
        self.multiSelectPaintable: MultiSelectPaintable = MultiSelectPaintable()
    

    def __init__(self, gameCanvas: AllBinaryGameCanvas, inputList: BasicArrayList, playerInputId: int, towerInfoPaintable: RTSLayerInfoPaintable, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerPositionFinderInterface: LayerPositionFinderInterface, selectRTSLayerVisitorFactoryInterface: SelectRTSLayerVisitorFactoryInterface, touchButtonsBuilderFactory: TouchButtonsBuilderFactory) -> None:
        super().__init__(gameCanvas, inputList, playerInputId, towerInfoPaintable, rtsPlayerLayerInterface, layerPositionFinderInterface, selectRTSLayerVisitorFactoryInterface)
        self._init_fields()
        self.touchButtonsBuilderFactory = touchButtonsBuilderFactory
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.notYoursGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NOT_YOURS, SmallIntegerSingletonFactory.getInstance().getAt(2), basicColorFactory.PINK, BooleanFactory.getInstance().FALSE)
        BasicMotionGesturesHandler.getInstance().addListenerInterface(self)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.notYoursGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    # throws Exception
    def processDraggingMotionInput(self, layerManager: AllBinaryLayerManager) -> bool:
        motionGestureEvent: MotionGestureEvent = self.getMotionGestureInputList().get(self.getMotionGestureInputList().size() - 1)
        motionGestureInput: MotionGestureInput = motionGestureEvent.getMotionGesture()
        rtsFormInput: RTSFormInput = self.getSelectedRtsFormInput()
        if motionGestureInput == self.PRESSED:
            point: GPoint = motionGestureEvent.getCurrentPoint()
            if self.getRtsPlayerLayerInterface().getCurrentScrollSelectionForm().isInForm(point):
                self.isDragging = rtsFormInput.processSticky(self.getSelectedRtsLayer(), self.getRtsPlayerLayerInterface(), layerManager, point)
        elif motionGestureInput == self.RELEASED:
            point: GPoint = motionGestureEvent.getCurrentPoint()
            if self.getRtsPlayerLayerInterface().getCurrentScrollSelectionForm().isInForm(point):
                rtsFormInput.processAtPoint(self.getSelectedRtsLayer(), self.getRtsPlayerLayerInterface(), layerManager, point)
            elif rtsFormInput.isStickyItemSelected():
                previousRtsFormInput: RTSFormInput = rtsFormInput
                self.select(motionGestureEvent)
                self.getSelectedBuildingPlayerGameInput().selectAllPreselected()
                previousRtsFormInput.processAtPoint(self.getSelectedRtsLayer(), self.getRtsPlayerLayerInterface(), layerManager, point)
                self.getSelectedBuildingPlayerGameInput().deselectAllPreselected()
            else:
                self.select(motionGestureEvent)
            rtsFormInput.setStickyItemSelected(False)
            rtsFormInput.setSelectedStickyItem(ABCustomItem.getNullInstance())
            rtsFormInput.setSelectedStickyItemIndex(-1)
            return True
        return False
    

    def makeSelection(self) -> None:
        rtsLayerList: BasicArrayList = self.getRtsPlayerLayerInterface().getPlayerOwnedRTSLayers().rtsLayerList
        rectX1: int = self.startPoint.getX()
        rectY1: int = self.startPoint.getY()
        rectX2: int = self.endPoint.getX()
        rectY2: int = self.endPoint.getY()
        if rectX1 > rectX2:
            rectX2 = rectX1
            rectX1 = self.endPoint.getX()
        if rectY1 > rectY2:
            rectY2 = rectY1
            rectY1 = self.endPoint.getY()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.AT)
        stringBuffer.appendint(rectX1)
        stringBuffer.append(self.SPACE)
        stringBuffer.appendint(rectY1)
        stringBuffer.append(self.SPACE)
        stringBuffer.appendint(rectX2)
        stringBuffer.append(self.SPACE)
        stringBuffer.appendint(rectY2)
        self.logUtil.putF(str(stringBuffer), self, self.METHOD)
        rtsLayer: RTSLayer = None
        for index in range(rtsLayerList.size() - 1, 0 - 1, -1):
            rtsLayer = rtsLayerList.get(index)
            stringBuffer.delete(0, stringBuffer.length())
            viewPosition: ViewPositionBase = rtsLayer.getViewPosition()
            stringBuffer.append(self.POSSIBLE)
            stringBuffer.append(rtsLayer.getName())
            stringBuffer.append(self.SPACE)
            stringBuffer.append(self.AT)
            stringBuffer.appendint(int((viewPosition.getX() + rtsLayer.getHalfWidth())))
            stringBuffer.append(self.SPACE)
            stringBuffer.appendint(int((viewPosition.getY() + rtsLayer.getHalfHeight())))
            self.logUtil.putF(str(stringBuffer), self, self.METHOD)
            if self.rectangleCollisionUtil.isInside(rectX1, rectY1, rectX2, rectY2, viewPosition.getX() + rtsLayer.getHalfWidth(), viewPosition.getY() + rtsLayer.getHalfHeight()):
                self.logUtil.putF(str(StringMaker().append(self.ADDING).append(rtsLayer.getName())), self, self.METHOD)
                rtsLayer.select()
                self.getSelectedBuildingPlayerGameInput().addSelectedRTSLayer(rtsLayer)
        gameLayer: CollidableDestroyableDamageableLayer = self.getSelectedBuildingPlayerGameInput().getLastSelectedRtsLayer()
        if gameLayer != CollidableDestroyableDamageableLayer.getNullInstance():
            lastRTSLayer: RTSLayer = gameLayer
            if lastRTSLayer.getScrollSelectionForm() != ScrollSelectionForm.getNullScrollSelectionForm():
                self.updateForm(lastRTSLayer.getScrollSelectionForm(), lastRTSLayer.getRTSFormInput())
                self.setSelectedRtsLayer(lastRTSLayer)
        self.updatePaintable()
    

    # throws Exception
    def processSelectionBoxMotionInput(self, layerManager: AllBinaryLayerManager) -> None:
        for index in range(self.getMotionGestureInputList().size() - 1, 0 - 1, -1):
            motionGestureEvent: MotionGestureEvent = self.getMotionGestureInputList().get(index)
            motionGestureInput: MotionGestureInput = motionGestureEvent.getMotionGesture()
            point: GPoint = motionGestureEvent.getCurrentPoint()
            if motionGestureInput == self.touchMotionGestureFactory.PRESSED:
                self.startPoint = point
                self.endPoint = point
            elif motionGestureInput == self.touchMotionGestureFactory.RELEASED:
                self.endPoint = point
                self.makeSelection()
                self.startPoint = PointFactory.getInstance().ZERO_ZERO
                self.endPoint = PointFactory.getInstance().ZERO_ZERO
            else:
                self.endPoint = point
    

    # throws Exception
    def processMotionInput(self, layerManager: AllBinaryLayerManager) -> None:
        if self.getMotionGestureInputList().size() > 0:
            endDrag: bool = self.processDraggingMotionInput(layerManager)
            if not self.isDragging:
                self.processSelectionBoxMotionInput(layerManager)
            if endDrag:
                self.isDragging = False
        self.getMotionGestureInputList().clear()
    

    def setSelectedRtsFormInput(self, selectedRtsFormInput: RTSFormInput) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START).append(StringUtil.getInstance().toString(selectedRtsFormInput))), self, "setSelectedRtsFormInput")
        super().setSelectedRtsFormInput(selectedRtsFormInput)
        self.setSelectedRtsLayer(CollidableDestroyableDamageableLayer.getNullInstance())
    

    def updateFormForLayer(self, rtsLayer: RTSLayer) -> None:
        scrollSelectionForm: ScrollSelectionForm = rtsLayer.getScrollSelectionForm()
        if scrollSelectionForm != ScrollSelectionForm.getNullScrollSelectionForm() and self.getRtsPlayerLayerInterface().getGroupInterface()[0] == rtsLayer.getGroupInterface()[0]:
            self.updateForm(scrollSelectionForm, rtsLayer.getRTSFormInput())
            self.getSelectedBuildingPlayerGameInput().setSelectedRTSLayer(CollidableDestroyableDamageableLayer.getNullInstance())
            self.setSelectedRtsLayer(rtsLayer)
        else:
            self.getRtsPlayerLayerInterface().setCurrentScrollSelectionForm(self.getRtsPlayerLayerInterface().getBuildingScrollSelectionForm())
            self.setSelectedRtsFormInput(self.getRtsPlayerLayerInterface().getRTSFormInput())
            self.getSelectedBuildingPlayerGameInput().setSelectedRTSLayer(CollidableDestroyableDamageableLayer.getNullInstance())
    

    def updateForm(self, scrollSelectionForm: ScrollSelectionForm, rtfFormInput: RTSFormInput) -> None:
        self.getRtsPlayerLayerInterface().setCurrentScrollSelectionForm(scrollSelectionForm)
        self.setSelectedRtsFormInput(rtfFormInput)
    

    # throws Exception
    def setSelectedRTSLayer(self, rtSLayer: CollidableDestroyableDamageableLayer, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        if rtSLayer != CollidableDestroyableDamageableLayer.getNullInstance() and self.getRtsPlayerLayerInterface().getGroupInterface()[0] != rtSLayer.getGroupInterface()[0]:
            self.getRtsPlayerLayerInterface().add(ErrorSound.getInstance())
            GameNotificationEventHandler.getInstance().fireEvent(self.notYoursGameNotificationEvent)
            return
        gameCanvas: AllBinaryGameCanvas = self.getGameCanvas()
        if rtSLayer != CollidableDestroyableDamageableLayer.getNullInstance():
            self.getRtsPlayerLayerInterface().add(SelectBuildingSound.getInstance())
            rtsLayer: RTSLayer = rtSLayer
            rtsLayer.select()
            self.updateFormForLayer(rtsLayer)
            if gameCanvas.getGameState() == self.gameStateFactory.PLAYING_GAME_STATE:
                if rtsLayer.isSelfUpgradeable():
                    gameCanvas.updateCurrentTouchInputFactory(RTSTouchButtonsBuilder())
                else:
                    gameCanvas.updateCurrentTouchInputFactory(NoBuildingSelectedTouchButtonsBuilder())
            else:
                endLevelTouchButtonsBuilder: EndLevelTouchButtonsBuilder = EndLevelTouchButtonsBuilder()
                if self.touchButtonsBuilderFactory is not None:
                    endLevelTouchButtonsBuilder.add(self.touchButtonsBuilderFactory.getInstance())
                gameCanvas.updateCurrentTouchInputFactory(endLevelTouchButtonsBuilder)
        else:
            self.logUtil.putF("Set Player Default Form", self, "setSelectedRTSLayer")
            self.getRtsPlayerLayerInterface().setCurrentScrollSelectionForm(self.getRtsPlayerLayerInterface().getBuildingScrollSelectionForm())
            self.setSelectedRtsFormInput(self.getRtsPlayerLayerInterface().getRTSFormInput())
            self.getSelectedBuildingPlayerGameInput().setSelectedRTSLayer(CollidableDestroyableDamageableLayer.getNullInstance())
            if gameCanvas.getGameState() == self.gameStateFactory.PLAYING_GAME_STATE:
                gameCanvas.updateCurrentTouchInputFactory(NoBuildingSelectedTouchButtonsBuilder())
            else:
                endLevelNoBuildingSelectedTouchButtonsBuilder: EndLevelNoBuildingSelectedTouchButtonsBuilder = EndLevelNoBuildingSelectedTouchButtonsBuilder()
                if self.touchButtonsBuilderFactory is not None:
                    endLevelNoBuildingSelectedTouchButtonsBuilder.add(self.touchButtonsBuilderFactory.getInstance())
                gameCanvas.updateCurrentTouchInputFactory(endLevelNoBuildingSelectedTouchButtonsBuilder)
        self.getSelectedRtsFormInput().setSelectedGeographicCellPosition(geographicMapCellPosition)
        self.getSelectedBuildingPlayerGameInput().setSelectedRTSLayer(rtSLayer)
        self.updatePaintable()
    

    def updatePaintable(self) -> None:
        list_: BasicArrayList = self.getSelectedBuildingPlayerGameInput().getSelectedBasicArrayList()
        if list_.size() > 1:
            geographicMapCompositeInterface: GeographicMapCompositeInterface = self.getGameCanvas()
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            self.multiSelectPaintable.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
            self.multiSelectPaintable.update(list_)
            self.getRTSLayerInfoPaintable().updateRTSLayerInfoSelection(self.multiSelectPaintable)
        elif list_.size() == 1:
            rtsLayer: RTSLayer = list_.get(0)
            self.getRTSLayerInfoPaintable().updateRTSLayerInfoSelection(rtsLayer.createHudPaintable())
        else:
            self.getRTSLayerInfoPaintable().updateRTSLayerInfoInit(NullInitUpdatePaintable.getInstance())
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        if self.startPoint != PointFactory.getInstance().ZERO_ZERO and self.endPoint != PointFactory.getInstance().ZERO_ZERO:
            graphics.setColor(int(BasicColorFactory.getInstance().RED))
            rectX1: int = self.startPoint.getX()
            rectY1: int = self.startPoint.getY()
            rectX2: int = self.endPoint.getX()
            rectY2: int = self.endPoint.getY()
            if rectX1 > rectX2:
                rectX2 = rectX1
                rectX1 = self.endPoint.getX()
            if rectY1 > rectY2:
                rectY2 = rectY1
                rectY1 = self.endPoint.getY()
            graphics.drawRect(rectX1, rectY1, rectX2 - rectX1, rectY2 - rectY1)
    

    def onMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        self.getMotionGestureInputList().add(motionGestureEvent)
    

    def onScrolledMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        pass
    

    def getSelectedRtsLayer(self) -> CollidableDestroyableDamageableLayer:
        return self.selectedRtsLayer
    

    def setSelectedRtsLayer(self, selectedRtsLayer: CollidableDestroyableDamageableLayer) -> None:
        self.selectedRtsLayer = selectedRtsLayer
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.form.RTSFormInput import RTSFormInput
from org.allbinary.game.layer.MultiSelectPaintable import MultiSelectPaintable
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSLayerInfoPaintable import RTSLayerInfoPaintable
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.state.GameStateFactory import GameStateFactory
from org.allbinary.input.motion.button.EndLevelNoBuildingSelectedTouchButtonsBuilder import EndLevelNoBuildingSelectedTouchButtonsBuilder
from org.allbinary.input.motion.button.EndLevelTouchButtonsBuilder import EndLevelTouchButtonsBuilder
from org.allbinary.input.motion.button.NoBuildingSelectedTouchButtonsBuilder import NoBuildingSelectedTouchButtonsBuilder
from org.allbinary.input.motion.button.RTSTouchButtonsBuilder import RTSTouchButtonsBuilder
from org.allbinary.media.audio.SelectBuildingSound import SelectBuildingSound
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.graphics.paint.NullInitUpdatePaintable import NullInitUpdatePaintable
from org.allbinary.input.motion.button.TouchButtonsBuilderFactory import TouchButtonsBuilderFactory
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.RectangleCollisionUtil import RectangleCollisionUtil
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.view.ViewPositionBase import ViewPositionBase


