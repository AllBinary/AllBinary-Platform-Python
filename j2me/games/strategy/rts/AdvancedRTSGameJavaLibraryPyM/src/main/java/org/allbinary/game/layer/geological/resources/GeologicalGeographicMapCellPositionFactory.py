# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.game.layer.geological.resources

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface


class GeologicalGeographicMapCellPositionFactory(GeographicMapCellPositionFactoryInterface):

    def _init_fields(self) -> None:
        self.resourcePerMapCellType: list[int] = None
    

    def __init__(self, resourcePerMapCellType: list[int]) -> None:
        self._init_fields()
        self.resourcePerMapCellType = resourcePerMapCellType
    

    # throws Exception
    def getInstance(self, geographicMapInterface: BasicGeographicMap, i_column: int, i_row: int, columns: int, rows: int, width: int, height: int) -> GeographicMapCellPosition:
        from org.allbinary.game.layer.geological.resources.GeologicalGeographicMapCellPosition import GeologicalGeographicMapCellPosition
        from org.allbinary.game.layer.geological.resources.GeologicalResource import GeologicalResource
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        resources: int = self.resourcePerMapCellType[tiledLayer.getCell(i_column, i_row)] + MyRandomFactory.getInstance().getAbsoluteNextInt(1000)
        return GeologicalGeographicMapCellPosition(i_column, i_row, columns, rows, width, height, GeologicalResource(resources))
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


