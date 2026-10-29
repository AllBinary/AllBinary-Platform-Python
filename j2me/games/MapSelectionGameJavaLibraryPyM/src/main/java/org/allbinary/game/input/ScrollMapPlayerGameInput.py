#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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


class ScrollMapPlayerGameInput(PlayerGameInput):

    def _init_fields(self) -> None:
        self.inputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.border: int = 150
        self.inputList: BasicArrayList = None
        self.isSingleKeyProcessing: bool = Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_REPEAT_PRESS) or Features.getInstance().isFeature(InputFeatureFactory.getInstance().SINGLE_KEY_PRESS)
        self.geographicMapInterface: BasicGeographicMap = None
        self.maxBottom: int = 0
        self.maxRight: int = 0
        self.scrollMapEvent: ScrollMapEvent = ScrollMapEvent(self)
    

    def __init__(self, geographicMapInterface: BasicGeographicMap, list_: BasicArrayList, playerInputId: int) -> None:
        super().__init__(list_, BasicArrayListD(), playerInputId)
        self._init_fields()
        self.initInputProcessors()
        self.geographicMapInterface = geographicMapInterface
        self.inputList = list_
        self.init()
    

    # throws Exception
    def move(self, dx: int, dy: int) -> None:
        terrainTiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        terrainTiledLayer.moveDXY(-dx, -dy)
        self.scrollMapEvent.setDxDy(-dx, -dy)
        ScrollMapEventHandler.getInstance().fireEvent(self.scrollMapEvent)
    

    def init(self) -> None:
        self.maxBottom = self.getSpecialHeight()
        self.maxRight = self.getSpecialWidth()
    

    # throws Exception
    def scrollMiddleX(self) -> None:
        terrainTiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.move(-terrainTiledLayer.getXP(), 0)
        if terrainTiledLayer.getWidth() < displayInfo.getLastWidth():
            diffX: int = ((displayInfo.getLastWidth() - terrainTiledLayer.getWidth()) >> 1)
            self.move(-diffX, 0)
        else:
            diffX: int = ((terrainTiledLayer.getWidth() - displayInfo.getLastWidth()) >> 1)
            self.move(diffX, 0)
    

    # throws Exception
    def scrollY(self, anchor: int) -> None:
        terrainTiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if anchor == Graphics.TOP:
            self.logUtil.putF("Top", self, "scrollY")
        elif anchor == Graphics.BOTTOM:
            self.logUtil.putF("Bottom", self, "scrollY")
            diffY: int = (terrainTiledLayer.getHeight() - displayInfo.getLastHeight())
            self.move(0, diffY)
        elif anchor == Graphics.VCENTER:
            self.logUtil.putF("Center", self, "scrollY")
            diffY: int = (terrainTiledLayer.getHeight() - displayInfo.getLastHeight()) / 2
            self.move(0, diffY)
        else:
            raise Exception("No Such Anchor Supported")
    

    # throws Exception
    def up(self) -> None:
        y: int = self.geographicMapInterface.getAllBinaryTiledLayer().getYP() - 10
        if self.keepOnMapMinY(y):
            self.move(0, -10)
    

    # throws Exception
    def down(self) -> None:
        y: int = -self.geographicMapInterface.getAllBinaryTiledLayer().getYP() + 10
        if self.keepOnMapMaxY(y):
            self.move(0, 10)
    

    # throws Exception
    def right(self) -> None:
        x: int = self.geographicMapInterface.getAllBinaryTiledLayer().getYP() + 10
        if self.keepOnMapMinX(x):
            self.move(10, 0)
    

    # throws Exception
    def left(self) -> None:
        x: int = -self.geographicMapInterface.getAllBinaryTiledLayer().getYP() - 10
        if self.keepOnMapMaxX(x):
            self.move(-10, 0)
    

    def initInputProcessors(self) -> None:
        from org.allbinary.game.input.ScrollMapUpGameInputProcessor import ScrollMapUpGameInputProcessor
        from org.allbinary.game.input.ScrollMapDownGameInputProcessor import ScrollMapDownGameInputProcessor
        from org.allbinary.game.input.ScrollMapRightGameInputProcessor import ScrollMapRightGameInputProcessor
        from org.allbinary.game.input.ScrollMapLeftGameInputProcessor import ScrollMapLeftGameInputProcessor
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        self.inputProcessorArray[Canvas.UP] = ScrollMapUpGameInputProcessor(self)
        self.inputProcessorArray[Canvas.DOWN] = ScrollMapDownGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_NUM9] = ScrollMapRightGameInputProcessor(self)
        self.inputProcessorArray[Canvas.KEY_NUM7] = ScrollMapLeftGameInputProcessor(self)
        GameInputProcessorUtil.init(self.inputProcessorArray)
    

    # throws Exception
    def processInputKey(self, key: int) -> None:
        self.inputProcessorArray[key].processEvent(AllBinaryGameLayerManager.getNullInstance(), GameKeyEvent.NONE)
    

    # throws Exception
    def processInput(self, layerManager: AllBinaryLayerManager) -> None:
        try:
            size: int = self.inputList.size()
            key: int = 0
            for index in range(0, size):
                gameKeyEvent: GameKeyEvent = self.inputList.get(index)
                key = gameKeyEvent.getKey()
                self.processInputKey(key)
            if self.isSingleKeyProcessing:
                self.clear()
            else:
                self.update()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.PROCESS_INPUT, e)
    

    def getSpecialHeight(self) -> int:
        terrainTiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if terrainTiledLayer.getHeight() > displayInfo.getLastHeight():
            return terrainTiledLayer.getHeight() - displayInfo.getLastHeight()
        else:
            return displayInfo.getLastHeight() - terrainTiledLayer.getHeight() + terrainTiledLayer.getCellHeight()
    

    def getSpecialWidth(self) -> int:
        terrainTiledLayer: AllBinaryTiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if terrainTiledLayer.getWidth() > displayInfo.getLastWidth():
            return terrainTiledLayer.getWidth() - displayInfo.getLastWidth()
        else:
            return displayInfo.getLastWidth() - terrainTiledLayer.getWidth() + terrainTiledLayer.getCellWidth()
    

    def keepOnMapMaxY(self, newY: int) -> bool:
        y: int = self.geographicMapInterface.getAllBinaryTiledLayer().getYP()
        if y > self.maxBottom + self.border:
            return False
        else:
            return True
    

    def keepOnMapMinY(self, newY: int) -> bool:
        y: int = self.geographicMapInterface.getAllBinaryTiledLayer().getYP()
        if y < -self.border:
            return False
        else:
            return True
    

    def keepOnMapMaxX(self, newX: int) -> bool:
        x: int = self.geographicMapInterface.getAllBinaryTiledLayer().getXP()
        if x < -self.maxRight - self.border:
            return False
        else:
            return True
    

    def keepOnMapMinX(self, newX: int) -> bool:
        x: int = self.geographicMapInterface.getAllBinaryTiledLayer().getXP()
        if x > self.border:
            return False
        else:
            return True
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.event.ScrollMapEvent import ScrollMapEvent
from org.allbinary.layer.event.ScrollMapEventHandler import ScrollMapEventHandler
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.input.InputFactory import InputFactory


