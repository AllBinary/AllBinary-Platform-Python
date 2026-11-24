# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.GeographicMapCellPositionAreaInterface import GeographicMapCellPositionAreaInterface


class GeographicMapCellPositionAreaBase(GeographicMapCellPositionAreaInterface):
    NULL_GEOGRPAHIC_MAP_POSITION_AREA_BASE: GeographicMapCellPositionAreaBase = None
    

    def getNextSurroundingGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise RuntimeError()
    

    def getOccupyingGeographicMapCellPositionList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    def getSurroundingGeographicMapCellPositionList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise RuntimeError()
    

    # throws Exception
    def update(self, geographicMapInterface: BasicGeographicMap) -> None:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        raise RuntimeError()
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _GeographicMapCellPositionAreaBase_NULL_GEOGRPAHIC_MAP_POSITION_AREA_BASE() -> object:
    return GeographicMapCellPositionAreaBase()

lazy_static(GeographicMapCellPositionAreaBase, "NULL_GEOGRPAHIC_MAP_POSITION_AREA_BASE", _GeographicMapCellPositionAreaBase_NULL_GEOGRPAHIC_MAP_POSITION_AREA_BASE)

