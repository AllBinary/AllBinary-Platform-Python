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
# package org.allbinary.game.layer.geographic.map

from __future__ import annotations

import threading
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.event.GeographicMapCellPositionEventListenerInterface import GeographicMapCellPositionEventListenerInterface


class MiniMapLayer(AllBinaryLayer, GeographicMapCellPositionEventListenerInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.allBinaryTiledLayer: AllBinaryTiledLayer = None
        self.geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = None
        self.list_: BasicArrayList = None
        self.basicColorList: BasicArrayList = None
        self.positionList: BasicArrayList = None
        self.animationInterface: CircleFilledAnimation = None
    

    def __init__(self, geographicMapInterface: BasicGeographicMap, viewPosition: ViewPositionBase) -> None:
        super().__init__(StringUtil.getInstance().EMPTY_STRING, Rectangle(PointFactory.getInstance().createXY(0, viewPosition.getY()), geographicMapInterface.getAllBinaryTiledLayer().getWidth(), geographicMapInterface.getAllBinaryTiledLayer().getHeight()), viewPosition)
        self._init_fields()
        self.allBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        self.geographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        self.animationInterface = CircleFilledAnimation(self.allBinaryTiledLayer.getCellWidth(), self.allBinaryTiledLayer.getCellHeight(), BasicColorFactory.getInstance().WHITE)
        self.list_ = BasicArrayListD()
        self.basicColorList = BasicArrayListD()
        self.positionList = BasicArrayListD()
        GeographicMapCellPositionEventHandler.getInstance().addListener(self)
        self.init()
    

    # throws Exception
    def init(self) -> None:
        self.allBinaryTiledLayer.setPosition(self.x, self.y, self.z)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onRemoveGeographicMapCellPositionEvent(self, geographicMapCellPositionEvent: GeographicMapCellPositionEvent) -> None:
        with self._lock:
            return self._onRemoveGeographicMapCellPositionEvent_unlocked(geographicMapCellPositionEvent)

    def _onRemoveGeographicMapCellPositionEvent_unlocked(self, geographicMapCellPositionEvent: GeographicMapCellPositionEvent) -> None:
        colorCompositeInterface: ColorCompositeInterface = geographicMapCellPositionEvent.getSource()
        index: int = self.list_.indexOf(colorCompositeInterface)
        if index >= 0:
            self.list_.removeAt(index)
            self.basicColorList.removeAt(index)
            self.positionList.removeAt(index)
    

    # throws Exception
    def onGeographicMapCellPositionEvent(self, geographicMapCellPositionEvent: GeographicMapCellPositionEvent) -> None:
        with self._lock:
            return self._onGeographicMapCellPositionEvent_unlocked(geographicMapCellPositionEvent)

    def _onGeographicMapCellPositionEvent_unlocked(self, geographicMapCellPositionEvent: GeographicMapCellPositionEvent) -> None:
        colorCompositeInterface: ColorCompositeInterface = geographicMapCellPositionEvent.getSource()
        layerIndex: int = -1
        size: int = self.list_.size()
        nextColorCompositeInterface: ColorCompositeInterface = None
        for index in range(0, size):
            nextColorCompositeInterface = self.list_.get(index)
            if nextColorCompositeInterface == colorCompositeInterface:
                layerIndex = index
                break
        geographicMapCellPosition: GeographicMapCellPosition = self.geographicMapCellPositionFactory.getInstance(geographicMapCellPositionEvent.getGeographicMapCellPosition())
        point: GPoint = geographicMapCellPosition.getPoint()
        if layerIndex == -1:
            self.list_.add(colorCompositeInterface)
            basicColor: BasicColor = colorCompositeInterface.getBasicColorP()
            self.basicColorList.add(basicColor)
            self.positionList.add(point)
            layerIndex = self.basicColorList.size() - 1
        else:
            self.positionList.set(layerIndex, point)
    

    def paintDots(self, graphics: Graphics) -> None:
        localPositionList: BasicArrayList = self.positionList
        localBasicColorList: BasicArrayList = self.basicColorList
        length: int = localPositionList.size()
        point: GPoint = None
        basicColor: BasicColor = None
        index = length
        while (index := index - 1) >= 0:
            point = localPositionList.get(index)
            basicColor = localBasicColorList.get(index)
            graphics.setColor(int(basicColor))
            self.animationInterface.setBasicColorP(basicColor)
            self.animationInterface.paintXY(graphics, point.getX() + self.x, point.getY() + self.y)
    

    def paint(self, graphics: Graphics) -> None:
        self.allBinaryTiledLayer.paint(graphics)
        self.paintDots(graphics)
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.animation.vector.CircleFilledAnimation import CircleFilledAnimation
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.ColorCompositeInterface import ColorCompositeInterface
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.event.GeographicMapCellPositionEvent import GeographicMapCellPositionEvent
from org.allbinary.media.graphics.geography.map.event.GeographicMapCellPositionEventHandler import GeographicMapCellPositionEventHandler
from org.allbinary.view.ViewPositionBase import ViewPositionBase


