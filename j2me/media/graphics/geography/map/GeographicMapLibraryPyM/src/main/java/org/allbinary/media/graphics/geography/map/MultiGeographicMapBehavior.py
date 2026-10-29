# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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



class MultiGeographicMapBehavior:
    

    # throws Exception
    def getCellTypeAt(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition) -> list[GeographicMapCellType]:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        size: int = len(geographicMapInterfaceArray)
        cellType: GeographicMapCellType = GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE
        index = size
        while (index := index - 1) >= 0:
            cellType = geographicMapInterfaceArray[index].getCellTypeAt(geographicMapCellPosition)
            geographicMapCellTypeArray[index] = cellType
        return geographicMapCellTypeArray


