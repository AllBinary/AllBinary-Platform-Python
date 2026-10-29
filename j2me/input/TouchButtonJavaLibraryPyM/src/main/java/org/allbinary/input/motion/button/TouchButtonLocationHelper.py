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
# package org.allbinary.input.motion.button

from __future__ import annotations

import math


class TouchButtonLocationHelper:

    def _init_fields(self) -> None:
        self.totalColumns: int = None
        self.totalRows: int = None
        self.columnsRemainder: int = None
        self.rowsRemainder: int = None
        self.columnsRemainderHalf: int = None
        self.rowsRemainderHalf: int = None
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        self._init_fields()
        buttonSize: int = CommonButtons.getInstance().STANDARD_BUTTON_SIZE
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.totalColumns = int(math.floor(float(displayInfo.getLastWidth()) / float(buttonSize) + 0.5))
        self.totalRows = int(math.floor(float(displayInfo.getLastHeight()) / float(buttonSize) + 0.5))
        self.columnsRemainder = displayInfo.getLastWidth() % buttonSize
        self.columnsRemainderHalf = (self.columnsRemainder >> 1)
        self.rowsRemainder = displayInfo.getLastHeight() % buttonSize
        self.rowsRemainderHalf = (self.rowsRemainder >> 1)
    

    def getTotalColumns(self) -> int:
        return self.totalColumns
    

    def getTotalRows(self) -> int:
        return self.totalRows
    

    def getColumnsRemainder(self) -> int:
        return self.columnsRemainder
    

    def getRowsRemainder(self) -> int:
        return self.rowsRemainder
    

    def getColumnsRemainderHalf(self) -> int:
        return self.columnsRemainderHalf
    

    def getRowsRemainderHalf(self) -> int:
        return self.rowsRemainderHalf
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("totalColumns: ")
        stringBuffer.appendint(self.totalColumns)
        stringBuffer.append(" totalRows: ")
        stringBuffer.appendint(self.totalRows)
        stringBuffer.append(" columnsRemainder: ")
        stringBuffer.appendint(self.columnsRemainder)
        stringBuffer.append(" rowsRemainder: ")
        stringBuffer.appendint(self.rowsRemainder)
        stringBuffer.append(" columnsRemainderHalf: ")
        stringBuffer.appendint(self.columnsRemainderHalf)
        stringBuffer.append(" rowsRemainderHalf: ")
        stringBuffer.appendint(self.rowsRemainderHalf)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.logic.string.StringMaker import StringMaker


