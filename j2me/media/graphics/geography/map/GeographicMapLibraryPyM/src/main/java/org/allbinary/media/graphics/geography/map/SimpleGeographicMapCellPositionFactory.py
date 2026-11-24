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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface


class SimpleGeographicMapCellPositionFactory(GeographicMapCellPositionFactoryInterface):
    NULL_GEOGRAPHIC_MAP_CELL_POSITION: GeographicMapCellPosition = None
    

    def getInstance(self, geographicMapInterface: BasicGeographicMap, i_column: int, i_row: int, columns: int, rows: int, width: int, height: int) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        return GeographicMapCellPosition(i_column, i_row, columns, rows, width, height)


def _SimpleGeographicMapCellPositionFactory_NULL_GEOGRAPHIC_MAP_CELL_POSITION() -> object:
    from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
    return GeographicMapCellPosition(-1, -1, -1, -1, -1, -1)

lazy_static(SimpleGeographicMapCellPositionFactory, "NULL_GEOGRAPHIC_MAP_CELL_POSITION", _SimpleGeographicMapCellPositionFactory_NULL_GEOGRAPHIC_MAP_CELL_POSITION)

