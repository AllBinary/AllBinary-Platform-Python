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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations



class WaypointCellPositionHistory:
    SINGLETON: WaypointCellPositionHistory = None

    def _init_fields(self) -> None:
        self.positionList: BasicArrayList = BasicArrayListD()
        self.layerList: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> WaypointCellPositionHistory:
        return WaypointCellPositionHistory.SINGLETON
    

    def add(self, cellPosition: CellPosition, layerInterface: AllBinaryLayer) -> None:
        self.positionList.add(cellPosition)
        self.layerList.add(layerInterface)
    

    def addList(self, list_: BasicArrayList, layerInterface: AllBinaryLayer) -> None:
        for index in range(list_.size() - 1, 0 - 1, -1):
            self.add(list_.get(index), layerInterface)
    

    def remove(self, cellPosition: CellPosition) -> None:
        index: int = self.positionList.indexOf(cellPosition)
        if index >= 0:
            self.positionList.removeAt(index)
            self.layerList.removeAt(index)
    

    def removeLayer(self, layerInterface: AllBinaryLayer) -> None:
        index: int = 0
        while index != -1:
            index = self.layerList.indexOf(layerInterface)
            if index >= 0:
                self.positionList.removeAt(index)
                self.layerList.removeAt(index)
    

    def clear(self) -> None:
        self.positionList.clear()
        self.layerList.clear()
    

    def isCellPositionWithDrop(self, cellPosition: CellPosition) -> bool:
        return self.positionList.contains(cellPosition)
    

    def anyCellPositionWithDrop(self, list_: BasicArrayList) -> bool:
        for index in range(list_.size() - 1, 0 - 1, -1):
            if self.isCellPositionWithDrop(list_.get(index)):
                return True
        return False
    

    def getLayerInterface(self, cellPosition: CellPosition) -> AllBinaryLayer:
        index: int = self.positionList.indexOf(cellPosition)
        if index >= 0:
            return self.layerList.get(index)
        else:
            return AllBinaryLayer.NULL_ALLBINARY_LAYER
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


WaypointCellPositionHistory.SINGLETON = WaypointCellPositionHistory()

