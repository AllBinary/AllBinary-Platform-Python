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

from org.allbinary.game.layer.building.event.BuildingEventListenerInterface import BuildingEventListenerInterface
from org.allbinary.layer.event.ScrollMapEventListenerInterface import ScrollMapEventListenerInterface


class VisibleCellPositionsSingleton(BuildingEventListenerInterface, ScrollMapEventListenerInterface):
    instance: VisibleCellPositionsSingleton = None

    def _init_fields(self) -> None:
        self.stationaryVisibleCellPositions: list[list[int]] = NullUtil.getInstance().NULL_SHORT_ARRAY_ARRAY
        self.visibleCellPositions: list[list[int]] = NullUtil.getInstance().NULL_SHORT_ARRAY_ARRAY
        self.currentlyVisibleCellPositions: list[list[int]] = NullUtil.getInstance().NULL_SHORT_ARRAY_ARRAY
        self.ALL_VISIBLE_TILEDLAYER: SimpleTiledLayer = SimpleTiledLayer(0, 0, 0, 0)
        self.simpleTiledLayer: SimpleTiledLayer = self.ALL_VISIBLE_TILEDLAYER
        self.paintSimpleTiledLayer: SimpleTiledLayer = self.ALL_VISIBLE_TILEDLAYER
        self.currentIndex: int = 0
    

    @staticmethod
    def getInstance() -> VisibleCellPositionsSingleton:
        return VisibleCellPositionsSingleton.instance
    

    def __init__(self) -> None:
        self._init_fields()
        LocalPlayerBuildingEventHandler.getInstance().addListenerInterface(self)
        ScrollMapEventHandler.getInstance().addListenerInterface(self)
    

    def init(self, simpleTiledLayer: SimpleTiledLayer) -> None:
        self.paintSimpleTiledLayer = self.ALL_VISIBLE_TILEDLAYER
        self.currentIndex = 0
        rows: int = simpleTiledLayer.getRows()
        columns: int = simpleTiledLayer.getColumns()
        self.stationaryVisibleCellPositions = [[0] * (columns) for _ in range(rows)]
        self.visibleCellPositions = [[0] * (columns) for _ in range(rows)]
        self.currentlyVisibleCellPositions = [[0] * (columns) for _ in range(rows)]
        self.setSimpleTiledLayer(simpleTiledLayer)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onBuildingEvent(self, event: RTSLayerEvent) -> None:
        self.paintSimpleTiledLayer = self.simpleTiledLayer
    

    # throws Exception
    def onMoveEvent(self, scrollMapEvent: ScrollMapEvent) -> None:
        self.move(scrollMapEvent.getDx(), scrollMapEvent.getDy())
    

    def addStationaryCellPositions(self, list_: BasicArrayList) -> None:
        for index in range(list_.size() - 1, 0 - 1, -1):
            cellPosition: CellPosition = list_.get(index)
            self.stationaryVisibleCellPositions[cellPosition.getRow()][cellPosition.getColumn()] += 1
    

    def removeStationaryCellPositions(self, list_: BasicArrayList) -> None:
        for index in range(list_.size() - 1, 0 - 1, -1):
            cellPosition: CellPosition = list_.get(index)
            self.stationaryVisibleCellPositions[cellPosition.getRow()][cellPosition.getColumn()] -= 1
    

    def update(self) -> None:
        if self.currentIndex == 0:
            temp: list[list[int]] = self.currentlyVisibleCellPositions
            self.currentlyVisibleCellPositions = self.visibleCellPositions
            self.visibleCellPositions = temp
            for index in range(len(self.visibleCellPositions) - 1, 0 - 1, -1):
                for index2 in range(len(self.visibleCellPositions[0]) - 1, 0 - 1, -1):
                    self.visibleCellPositions[index][index2] = self.stationaryVisibleCellPositions[index][index2]
        self.currentIndex += 1
        if self.currentIndex > 10:
            self.currentIndex = 0
    

    def shouldProcess(self) -> bool:
        if self.currentIndex == 0:
            return True
        else:
            return False
    

    def addCellPositions(self, list_: BasicArrayList) -> None:
        for index in range(list_.size() - 1, 0 - 1, -1):
            cellPosition: CellPosition = list_.get(index)
            self.visibleCellPositions[cellPosition.getRow()][cellPosition.getColumn()] += 1
    

    def isVisible(self, cellPosition: CellPosition) -> bool:
        if self.visibleCellPositions[cellPosition.getRow()][cellPosition.getColumn()] > 0:
            return True
        else:
            return False
    

    def move(self, dx: int, dy: int) -> None:
        self.getSimpleTiledLayer().moveDXY(dx, dy)
    

    def paint(self, graphics: Graphics) -> None:
        self.paintSimpleTiledLayer.paint(graphics, self.currentlyVisibleCellPositions)
    

    def setSimpleTiledLayer(self, simpleTiledLayer: SimpleTiledLayer) -> None:
        self.simpleTiledLayer = simpleTiledLayer
    

    def getSimpleTiledLayer(self) -> SimpleTiledLayer:
        return self.simpleTiledLayer
# from javax.microedition.lcdui.game.SimpleTiledLayer import SimpleTiledLayer
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.RTSLayerEvent import RTSLayerEvent
from org.allbinary.game.layer.building.event.LocalPlayerBuildingEventHandler import LocalPlayerBuildingEventHandler
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.layer.event.ScrollMapEvent import ScrollMapEvent
from org.allbinary.layer.event.ScrollMapEventHandler import ScrollMapEventHandler
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings


VisibleCellPositionsSingleton.instance = VisibleCellPositionsSingleton()

