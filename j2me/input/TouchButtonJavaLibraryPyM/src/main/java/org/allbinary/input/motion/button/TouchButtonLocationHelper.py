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
from java.lang.JavaRuntimeStatic import java_divide


class TouchButtonLocationHelper:

    def _init_fields(self) -> None:
        if "totalColumns" not in vars(self): self.totalColumns: int = 0
        if "totalRows" not in vars(self): self.totalRows: int = 0
        if "columnsRemainder" not in vars(self): self.columnsRemainder: int = 0
        if "rowsRemainder" not in vars(self): self.rowsRemainder: int = 0
        if "columnsRemainderHalf" not in vars(self): self.columnsRemainderHalf: int = 0
        if "rowsRemainderHalf" not in vars(self): self.rowsRemainderHalf: int = 0
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
        __class__._init_fields(self)
        buttonSize: int = CommonButtons.getInstance().STANDARD_BUTTON_SIZE
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.totalColumns = int(math.floor(float(displayInfo.getLastWidth()) / float(buttonSize) + 0.5))
        self.totalRows = int(math.floor(float(displayInfo.getLastHeight()) / float(buttonSize) + 0.5))
        self.columnsRemainder = displayInfo.getLastWidth() % buttonSize
        self.columnsRemainderHalf = (int(self.columnsRemainder) >> (int(1) & 31))
        self.rowsRemainder = displayInfo.getLastHeight() % buttonSize
        self.rowsRemainderHalf = (int(self.rowsRemainder) >> (int(1) & 31))
    

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
        from org.allbinary.logic.string.StringMaker import StringMaker
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
# from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
# from org.allbinary.logic.string.StringMaker import StringMaker


