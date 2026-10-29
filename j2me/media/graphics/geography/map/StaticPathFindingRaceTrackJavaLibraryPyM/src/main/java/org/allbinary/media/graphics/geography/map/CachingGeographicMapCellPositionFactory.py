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

from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory


class CachingGeographicMapCellPositionFactory(BasicGeographicMapCellPositionFactory):
    

    def __init__(self, geographicMapInterface: BasicGeographicMap) -> None:
        super().__init__(geographicMapInterface)
    

    # throws Exception
    def createInstance(self, i_column: int, i_row: int, width: int, height: int) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactory import GeographicMapCellPositionFactory
        hashtable: ABHashtable[object, object] = GeographicMapCellPositionFactory.getHashtable()
        cellPositionKey: str = CellPosition.toStringColRow(i_column, i_row)
        cellPositionCanBeNull: object = hashtable.get(cellPositionKey)
        if cellPositionCanBeNull is None:
            cellPositionCanBeNull = self.geographicMapCellPositionFactoryInterface.getInstance(self.geographicMapInterface, i_column, i_row, self.getColumns(), self.getRows(), width, height)
            self.geographicMapCellPositionArray[i_row][i_column] = cellPositionCanBeNull
            hashtable.put(cellPositionKey, cellPositionCanBeNull)
        return cellPositionCanBeNull
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.util.ABHashtable import ABHashtable


