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



class BasicGeographicMapCellPositionFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.geographicMapCellPositionArray: list[list[GeographicMapCellPosition]] = None
        self.geographicMapInterface: BasicGeographicMap = None
        self.geographicMapCellPositionFactoryInterface: GeographicMapCellPositionFactoryInterface = None
        self.columns: int = None
        self.rows: int = None
        self.tiledLayer: AllBinaryTiledLayer = None
    

    def __init__(self, geographicMapInterface: BasicGeographicMap) -> None:
        self._init_fields()
        self.geographicMapInterface = geographicMapInterface
        self.geographicMapCellPositionFactoryInterface = self.geographicMapInterface.getGeographicMapCellPositionFactoryInterface()
        self.tiledLayer = self.geographicMapInterface.getAllBinaryTiledLayer()
        self.columns = self.tiledLayer.getColumns()
        self.rows = self.tiledLayer.getRows()
        self.geographicMapCellPositionArray = [[None] * (self.columns) for _ in range(self.rows)]
        self.init()
    

    # throws Exception
    def init(self) -> None:
        tiledLayer: AllBinaryTiledLayer = self.tiledLayer
        columns: int = self.getColumns()
        rows: int = self.getRows()
        width: int = tiledLayer.getCellWidth()
        height: int = tiledLayer.getCellHeight()
        for column in range(0, columns):
            for row in range(0, rows):
                self.createInstance(column, row, width, height)
    

    # throws Exception
    def visit(self, geographicMapCelPositionFactoryInitVisitorInterface: GeographicMapCellPositionFactoryInitVisitorInterface) -> None:
        tiledLayer: AllBinaryTiledLayer = self.tiledLayer
        columns: int = self.getColumns()
        rows: int = self.getRows()
        try:
            cellPosition: GeographicMapCellPosition = None
            for column in range(0, columns):
                for row in range(0, rows):
                    cellPosition = self.getAt(column, row)
                    geographicMapCelPositionFactoryInitVisitorInterface.visit(tiledLayer, cellPosition)
        except Exception as e:
            commonSeps: CommonSeps = CommonSeps.getInstance()
            self.logUtil.put(str(StringMaker().append(commonSeps.BRACKET_OPEN).appendint(rows).append(commonSeps.BRACKET_CLOSE).append(commonSeps.BRACKET_OPEN).appendint(columns).append(commonSeps.BRACKET_CLOSE)), self, "visit", e)
            raise e
    

    # throws Exception
    def getAt(self, i_column: int, i_row: int) -> GeographicMapCellPosition:
        return self.geographicMapCellPositionArray[i_row][i_column]
    

    # throws Exception
    def getInstance(self, anotherMapGeographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        return self.getAt(anotherMapGeographicMapCellPosition.getColumn(), anotherMapGeographicMapCellPosition.getRow())
    

    # throws Exception
    def createInstance(self, i_column: int, i_row: int, width: int, height: int) -> GeographicMapCellPosition:
        cellPositionCanBeNull: object = self.geographicMapCellPositionArray[i_row][i_column]
        if cellPositionCanBeNull is None:
            cellPositionCanBeNull = self.geographicMapCellPositionFactoryInterface.getInstance(self.geographicMapInterface, i_column, i_row, self.columns, self.rows, width, height)
            self.geographicMapCellPositionArray[i_row][i_column] = cellPositionCanBeNull
        return cellPositionCanBeNull
    

    def getColumns(self) -> int:
        return self.columns
    

    def getRows(self) -> int:
        return self.rows
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


