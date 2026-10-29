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

from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


class SimpleGeographicMapCellPositionFactory(GeographicMapCellPositionFactoryInterface):
    NULL_GEOGRAPHIC_MAP_CELL_POSITION: GeographicMapCellPosition = GeographicMapCellPosition(-1, -1, -1, -1, -1, -1)
    

    def getInstance(self, geographicMapInterface: BasicGeographicMap, i_column: int, i_row: int, columns: int, rows: int, width: int, height: int) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        return GeographicMapCellPosition(i_column, i_row, columns, rows, width, height)


