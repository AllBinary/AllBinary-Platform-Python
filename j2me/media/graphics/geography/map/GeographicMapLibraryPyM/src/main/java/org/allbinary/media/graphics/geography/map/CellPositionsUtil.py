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



class CellPositionsUtil:
    instance: CellPositionsUtil = None

    def _init_fields(self) -> None:
        self.reusableSingleThreadedSurroundingList: BasicArrayList = BasicArrayListS(8)
        self.surroundArray: list[list[int]] = [[-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1], [1, 0], [-1, 0]]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CellPositionsUtil:
        return CellPositionsUtil.instance
    

    # throws Exception
    def getAll(self, geographicMapInterface: BasicGeographicMap, topRightGeographicMapCellPosition: GeographicMapCellPosition, columns: int, rows: int, reusableList: BasicArrayList) -> BasicArrayList:
        reusableList.clear()
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        lastColumn: int = topRightGeographicMapCellPosition.getColumn() + columns
        lastRow: int = topRightGeographicMapCellPosition.getRow() + rows
        if (columns > 1 and lastColumn > geographicMapInterface.getAllBinaryTiledLayer().getColumns()) or (rows > 1 and lastRow > geographicMapInterface.getAllBinaryTiledLayer().getRows()):
            return reusableList
        for rowIndex in range(0, rows):
            for columnIndex in range(0, columns):
                geographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(topRightGeographicMapCellPosition.getColumn() + columnIndex, topRightGeographicMapCellPosition.getRow() + rowIndex)
                reusableList.add(geographicMapCellPosition)
        return reusableList
    

    # throws Exception
    def getAllSurrounding(self, geographicMapInterface: BasicGeographicMap, occupyList: BasicArrayList, reusableList: BasicArrayList) -> BasicArrayList:
        reusableList.clear()
        for index in range(occupyList.size() - 1, 0 - 1, -1):
            layerGeographicMapCellPosition: GeographicMapCellPosition = occupyList.get(index)
            surroundingGeographicMapCellPositionList: BasicArrayList = self.getAllSurroundingAt(geographicMapInterface, layerGeographicMapCellPosition, self.reusableSingleThreadedSurroundingList)
            for index2 in range(surroundingGeographicMapCellPositionList.size() - 1, 0 - 1, -1):
                geographicMapCellPosition: GeographicMapCellPosition = surroundingGeographicMapCellPositionList.get(index2)
                if not reusableList.contains(geographicMapCellPosition) and not occupyList.contains(geographicMapCellPosition):
                    reusableList.add(geographicMapCellPosition)
        return reusableList
    

    # throws Exception
    def getAllSurroundingAt(self, geographicMapInterface: BasicGeographicMap, layerGeographicMapCellPosition: GeographicMapCellPosition, reusableSurroundingList: BasicArrayList) -> BasicArrayList:
        reusableSurroundingList.clear()
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        row: int = 0
        column: int = 0
        for index in range(0, 8):
            column = layerGeographicMapCellPosition.getColumn() + self.surroundArray[index][0]
            row = layerGeographicMapCellPosition.getRow() + self.surroundArray[index][1]
            if tiledLayer.isOnTileLayer(column, row):
                geographicMapCellPosition: GeographicMapCellPosition = geographicMapCellPositionFactory.getAt(column, row)
                reusableSurroundingList.add(geographicMapCellPosition)
        return reusableSurroundingList
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.util.BasicArrayListS import BasicArrayListS


CellPositionsUtil.instance = CellPositionsUtil()

