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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graph.V import V


@java_inherited_overloads
class CellPosition(V):
    def _java_defaults(self):
        vars(self).setdefault("id", 0)
        vars(self).setdefault("column", 0)
        vars(self).setdefault("row", 0)

    def _init_fields(self) -> None:
        if "id" not in vars(self): self.id: int = 0
        if "column" not in vars(self): self.column: int = 0
        if "row" not in vars(self): self.row: int = 0
    

    def __init__(self, column: int, row: int, columns: int, rows: int) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.column = column
        self.row = row
        self.id = (row * columns) + column
    

    def getColumn(self) -> int:
        return self.column
    

    def getRow(self) -> int:
        return self.row
    

    def toString(self) -> str:
        return CellPosition.toStringColRow(self.getColumn(), self.getRow())

    def __str__(self) -> str:
        return self.toString()
    

    @staticmethod
    def toStringCellPosition(basicGeographicMapCellPosition: CellPosition) -> str:
        return CellPosition.toStringColRow(basicGeographicMapCellPosition.getColumn(), basicGeographicMapCellPosition.getRow())
    

    @staticmethod
    def toStringColRow(i_column: int, i_row: int) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer.append(commonSeps.PARENTHESIS_OPEN)
        stringBuffer.appendint(i_column)
        stringBuffer.append(commonSeps.COMMA)
        stringBuffer.appendint(i_row)
        stringBuffer.append(commonSeps.PARENTHESIS_CLOSE)
        return str(stringBuffer)
    

    def getId(self) -> int:
        return self.id
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


