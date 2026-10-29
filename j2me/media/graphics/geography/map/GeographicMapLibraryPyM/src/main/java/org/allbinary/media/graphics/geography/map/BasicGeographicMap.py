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

from org.allbinary.media.graphics.geography.map.SimpleGeographicMap import SimpleGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapInterface import GeographicMapInterface


class BasicGeographicMap(SimpleGeographicMap, GeographicMapInterface):
    NULL_BASIC_GEOGRAPHIC_MAP_ARRAY: list[BasicGeographicMap] = None

    def _init_fields(self) -> None:
        self.mathUtil: MathUtil = MathUtil.getInstance()
        self.geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = None
        self.geographicMapCellPositionFactoryInterface: GeographicMapCellPositionFactoryInterface = None
        self.geographicMapCellTypeFactory: GeographicMapCellTypeFactory = None
    

    def __init__(self, id: int, name: str, cellTypeIdToGeographicMapCellType: list[int], tiledLayer: AllBinaryTiledLayer, foregroundBasicColor: BasicColor, backgroundBasicColor: BasicColor, geographicMapCellPositionFactoryInterface: GeographicMapCellPositionFactoryInterface, geographicMapCellPositionBaseFactory: GeographicMapCellPositionBaseFactory, geographicMapCellTypeFactory: GeographicMapCellTypeFactory) -> None:
        super().__init__(id, name, cellTypeIdToGeographicMapCellType, tiledLayer, foregroundBasicColor, backgroundBasicColor)
        self._init_fields()
        self.geographicMapCellPositionFactoryInterface = geographicMapCellPositionFactoryInterface
        self.geographicMapCellPositionFactory = geographicMapCellPositionBaseFactory.getInstance(self)
        self.geographicMapCellTypeFactory = geographicMapCellTypeFactory
    

    # throws Exception
    def getCellPosition(self, direction: int, oldGeographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        switch_value = direction
        if switch_value in (0,):
                return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn() - 1, oldGeographicMapCellPosition.getRow())
        elif switch_value in (1,):
                return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn() + 1, oldGeographicMapCellPosition.getRow())
        elif switch_value in (2,):
                return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn(), oldGeographicMapCellPosition.getRow() - 1)
        elif switch_value in (3,):
                return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn(), oldGeographicMapCellPosition.getRow() + 1)
        else:
                raise Exception("Only Four Directions")
    

    # throws Exception
    def getCellPositionNoThrow(self, direction: int, oldGeographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        switch_value = direction
        if switch_value in (0,):
                if oldGeographicMapCellPosition.getColumn() - 1 >= 0:
                    return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn() - 1, oldGeographicMapCellPosition.getRow())
                else:
                    return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        elif switch_value in (1,):
                if oldGeographicMapCellPosition.getColumn() + 1 < self.getAllBinaryTiledLayer().getColumns():
                    return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn() + 1, oldGeographicMapCellPosition.getRow())
                else:
                    return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        elif switch_value in (2,):
                if oldGeographicMapCellPosition.getRow() - 1 >= 0:
                    return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn(), oldGeographicMapCellPosition.getRow() - 1)
                else:
                    return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        elif switch_value in (3,):
                if oldGeographicMapCellPosition.getRow() + 1 < self.getAllBinaryTiledLayer().getRows():
                    return self.geographicMapCellPositionFactory.getAt(oldGeographicMapCellPosition.getColumn(), oldGeographicMapCellPosition.getRow() + 1)
                else:
                    return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        else:
                return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    # throws Exception
    def isOfFourDirections(self, oldGeographicMapCellPosition: GeographicMapCellPosition, newGeographicMapCellPosition: GeographicMapCellPosition) -> bool:
        for index in range(0, 4):
            if newGeographicMapCellPosition == self.getCellPositionNoThrow(index, oldGeographicMapCellPosition):
                return True
        return False
    

    # throws Exception
    def getCellPositionAtXY(self, x: int, y: int) -> GeographicMapCellPosition:
        allBinaryTiledLayer: AllBinaryTiledLayer = self.getAllBinaryTiledLayer()
        i_column: int = self.mathUtil.abs(x / allBinaryTiledLayer.getCellHeight())
        i_row: int = self.mathUtil.abs(y / allBinaryTiledLayer.getCellWidth())
        return self.geographicMapCellPositionFactory.getAt(i_column, i_row)
    

    def getCellPositionAtXYNoThrow(self, x: int, y: int) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        allBinaryTiledLayer: AllBinaryTiledLayer = self.getAllBinaryTiledLayer()
        i_column: int = self.mathUtil.abs(x / allBinaryTiledLayer.getCellHeight())
        i_row: int = self.mathUtil.abs(y / allBinaryTiledLayer.getCellWidth())
        if allBinaryTiledLayer.getColumns() > i_column and allBinaryTiledLayer.getRows() > i_row:
            try:
                return self.geographicMapCellPositionFactory.getAt(i_column, i_row)
            except Exception as e:
                return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        else:
            return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    # throws Exception
    def isOnMap(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        allBinaryTiledLayer: AllBinaryTiledLayer = self.getAllBinaryTiledLayer()
        i_column: int = geographicMapCellPosition.getColumn()
        i_row: int = geographicMapCellPosition.getRow()
        if allBinaryTiledLayer.getColumns() > i_column and allBinaryTiledLayer.getRows() > i_row:
            return True
        else:
            return False
    

    # throws Exception
    def getCellPositionAtNoThrow(self, x: int, y: int, x2: int, y2: int, geographicMapCellPositionList: BasicArrayList) -> BasicArrayList:
        geographicMapCellPositionList.clear()
        allBinaryTiledLayer: AllBinaryTiledLayer = self.getAllBinaryTiledLayer()
        i_columnMin: int = self.mathUtil.abs(x / allBinaryTiledLayer.getCellHeight())
        i_rowMin: int = self.mathUtil.abs(y / allBinaryTiledLayer.getCellWidth())
        i_columnMax: int = self.mathUtil.abs(x2 / allBinaryTiledLayer.getCellHeight()) + 1
        i_rowMax: int = self.mathUtil.abs(y2 / allBinaryTiledLayer.getCellWidth()) + 1
        for columnIndex in range(i_columnMin, i_columnMax):
            for rowIndex in range(i_rowMin, i_rowMax):
                if allBinaryTiledLayer.getColumns() > columnIndex and allBinaryTiledLayer.getRows() > rowIndex:
                    geographicMapCellPositionList.add(self.geographicMapCellPositionFactory.getAt(columnIndex, rowIndex))
        return geographicMapCellPositionList
    

    # throws Exception
    def getCellPositionsAt(self, layer: Layer, currentCellPositionArray: list[list[GeographicMapCellPosition]], cellPositionArray: list[list[GeographicMapCellPosition]]) -> bool:
        hasChanged: bool = False
        size: int = len(cellPositionArray)
        size2: int = len(cellPositionArray[0])
        xPortion: int = layer.getXP() / (size - 1)
        yPortion: int = layer.getYP() / (size - 1)
        for index in range(0, size):
            for index2 in range(0, size2):
                x: int = xPortion * index
                y: int = yPortion * index
                cellPositionArray[index][index2] = self.getCellPositionAtXY(x, y)
                if currentCellPositionArray[index][index2] != cellPositionArray[index][index2]:
                    hasChanged = True
        return hasChanged
    

    # throws Exception
    def getCellTypeAtXY(self, x: int, y: int) -> GeographicMapCellType:
        cellPosition: GeographicMapCellPosition = self.getCellPositionAtXY(x, y)
        return self.getCellTypeAt(cellPosition)
    

    def getGeographicMapCellPositionFactory(self) -> BasicGeographicMapCellPositionFactory:
        return self.geographicMapCellPositionFactory
    

    def getGeographicMapCellPositionFactoryInterface(self) -> GeographicMapCellPositionFactoryInterface:
        return self.geographicMapCellPositionFactoryInterface
    

    def getGeographicMapCellTypeFactory(self) -> GeographicMapCellTypeFactory:
        return self.geographicMapCellTypeFactory
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.layer.Layer import Layer
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.util.BasicArrayList import BasicArrayList


BasicGeographicMap.NULL_BASIC_GEOGRAPHIC_MAP_ARRAY = [None] * (0)

