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
# package org.allbinary.media.graphics.geography.map.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class GeographicMapCellPositionEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.geographicMapCellPosition: CellPosition = CellPositionFactory.getInstance().NONE
    

    def __init__(self, anyType: object, geographicMapCellPosition: CellPosition) -> None:
        super().__init__(anyType)
        self._init_fields()
        self.geographicMapCellPosition = geographicMapCellPosition
    

    def init(self, anyType: object) -> None:
        self.setSource(anyType)
    

    def setGeographicMapCellPosition(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.geographicMapCellPosition = geographicMapCellPosition
    

    def getGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.geographicMapCellPosition
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("CellPositionEvent: ")
        stringBuffer.append("\nGeographicMapCellPosition: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.getGeographicMapCellPosition()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.graphics.CellPositionFactory import CellPositionFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


