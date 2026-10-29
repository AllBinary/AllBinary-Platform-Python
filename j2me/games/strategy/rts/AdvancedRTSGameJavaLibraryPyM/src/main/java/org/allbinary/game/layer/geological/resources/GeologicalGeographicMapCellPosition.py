# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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

from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


class GeologicalGeographicMapCellPosition(GeographicMapCellPosition):

    def _init_fields(self) -> None:
        self.geologicalResource: GeologicalResource = None
    

    def __init__(self, column: int, row: int, columns: int, rows: int, width: int, height: int, geologicalResource: GeologicalResource) -> None:
        super().__init__(column, row, columns, rows, width, height)
        self._init_fields()
        self.geologicalResource = geologicalResource
    

    def getGeologicalResource(self) -> GeologicalResource:
        return self.geologicalResource


