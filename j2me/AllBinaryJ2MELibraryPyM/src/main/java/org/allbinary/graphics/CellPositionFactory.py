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
# package org.allbinary.graphics

from __future__ import annotations



class CellPositionFactory:
    SINGLETON: CellPositionFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.NONE: CellPosition = CellPosition(-1, -1, -1, -1)
        self.cellPositionArray: list[list[CellPosition]] = [[None] * (0) for _ in range(0)]
        self.columns: int = 0
        self.rows: int = 0
    

    @staticmethod
    def getInstance() -> CellPositionFactory:
        return CellPositionFactory.SINGLETON
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self, columns: int, rows: int) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Init: columns: ")
        stringBuffer.appendint(columns)
        stringBuffer.append(" rows: ")
        stringBuffer.appendint(rows)
        self.logUtil.putF(str(stringBuffer), self, commonStrings.INIT)
        self.cellPositionArray = [[None] * (rows) for _ in range(columns)]
        self.columns = columns
        self.rows = rows
        for column in range(0, columns):
            for row in range(0, rows):
                self.createInstance(column, row)
    

    def getInstanceColRow(self, i_column: int, i_row: int) -> CellPosition:
        try:
            return self.cellPositionArray[i_column][i_row]
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(str(StringMaker().append("columns: ").appendint(self.getColumns()).append(" rows: ").appendint(self.getRows()).append(" col: ").appendint(i_column).append(" row: ").appendint(i_row)), self, commonStrings.GET_INSTANCE, e)
            return self.NONE
    

    def createInstance(self, i_column: int, i_row: int) -> CellPosition:
        from org.allbinary.graphics.CellPosition import CellPosition
        cellPositionCanBeNull: CellPosition = self.cellPositionArray[i_column][i_row]
        if cellPositionCanBeNull is None:
            cellPositionCanBeNull = CellPosition(i_column, i_row, self.columns, self.rows)
            self.cellPositionArray[i_column][i_row] = cellPositionCanBeNull
        return cellPositionCanBeNull
    

    def getColumns(self) -> int:
        return self.columns
    

    def getRows(self) -> int:
        return self.rows
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.graphics.CellPosition import CellPosition


CellPositionFactory.SINGLETON = CellPositionFactory()

