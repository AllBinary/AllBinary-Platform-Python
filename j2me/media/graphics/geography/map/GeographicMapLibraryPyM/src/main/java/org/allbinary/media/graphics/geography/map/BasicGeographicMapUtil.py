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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations



class BasicGeographicMapUtil:
    instance: BasicGeographicMapUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicGeographicMapUtil:
        return BasicGeographicMapUtil.instance
    

    # throws Exception
    def getBorderingRow(self, direction: int, oldGeographicMapCellPosition: GeographicMapCellPosition) -> int:
        LOCATION_CHANGE: int = 1
        switch_value = direction
        if switch_value in (0,):
                return oldGeographicMapCellPosition.getRow()
        elif switch_value in (1,):
                return oldGeographicMapCellPosition.getRow()
        elif switch_value in (2,):
                return oldGeographicMapCellPosition.getRow() + LOCATION_CHANGE
        elif switch_value in (3,):
                return oldGeographicMapCellPosition.getRow() - LOCATION_CHANGE
        else:
                raise Exception("Only Four Directions")
    

    # throws Exception
    def getBorderingColumn(self, direction: int, oldGeographicMapCellPosition: GeographicMapCellPosition) -> int:
        LOCATION_CHANGE: int = 1
        switch_value = direction
        if switch_value in (0,):
                return oldGeographicMapCellPosition.getColumn() - LOCATION_CHANGE
        elif switch_value in (1,):
                return oldGeographicMapCellPosition.getColumn() + LOCATION_CHANGE
        elif switch_value in (2,):
                return oldGeographicMapCellPosition.getColumn()
        elif switch_value in (3,):
                return oldGeographicMapCellPosition.getColumn()
        else:
                raise Exception("Only Four Directions")
    

    # throws Exception
    def isSameCellPosition(self, fromGeographicMapCellPosition: GeographicMapCellPosition, toGeographicMapCellPosition: GeographicMapCellPosition) -> bool:
        fromColumn: int = fromGeographicMapCellPosition.getColumn()
        fromRow: int = fromGeographicMapCellPosition.getRow()
        goColumn: int = toGeographicMapCellPosition.getColumn()
        goRow: int = toGeographicMapCellPosition.getRow()
        if fromColumn == goColumn and fromRow == goRow:
            return True
        else:
            return False
    

    def createAllBinaryTiledLayerArray(self, geographicMapInterfaceArray: list[BasicGeographicMap]) -> list[Layer]:
        tiledLayerArray: list[Layer] = [None] * (len(geographicMapInterfaceArray))
        return self.getAllBinaryTiledLayerArray(geographicMapInterfaceArray, tiledLayerArray, 0)
    

    def getAllBinaryTiledLayerArray(self, geographicMapInterfaceArray: list[BasicGeographicMap], tiledLayerArray: list[Layer], startIndex: int) -> list[Layer]:
        geographicMapInterface: BasicGeographicMap = None
        size: int = len(geographicMapInterfaceArray)
        count: int = 0
        index = size + startIndex
        while (index := index - 1) >= startIndex:
            geographicMapInterface = geographicMapInterfaceArray[index]
            tiledLayerArray[((count := count + 1) - 1)] = geographicMapInterface.getAllBinaryTiledLayer()
        return tiledLayerArray
    

    def move(self, geographicMapInterfaceArray: list[BasicGeographicMap], dx: int, dy: int) -> None:
        geographicMapInterface: BasicGeographicMap = None
        size: int = len(geographicMapInterfaceArray)
        index = size
        while (index := index - 1) >= 0:
            geographicMapInterface = geographicMapInterfaceArray[index]
            geographicMapInterface.getAllBinaryTiledLayer().moveDXY(dx, dy)
    

    def setPosition(self, geographicMapInterfaceArray: list[BasicGeographicMap], x: int, y: int) -> None:
        geographicMapInterface: BasicGeographicMap = None
        size: int = len(geographicMapInterfaceArray)
        index = size
        while (index := index - 1) >= 0:
            geographicMapInterface = geographicMapInterfaceArray[index]
            geographicMapInterface.getAllBinaryTiledLayer().setPosition(x, y, geographicMapInterface.getAllBinaryTiledLayer().getZP())
from org.allbinary.layer.Layer import Layer
from org.allbinary.logic.communication.log.LogUtil import LogUtil


BasicGeographicMapUtil.instance = BasicGeographicMapUtil()

