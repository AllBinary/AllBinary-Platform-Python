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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


@java_inherited_overloads
class GeologicalGeographicMapCellPosition(GeographicMapCellPosition):
    def _java_defaults(self):
        vars(self).setdefault("geologicalResource", None)

    def _init_fields(self) -> None:
        if "geologicalResource" not in vars(self): self.geologicalResource: GeologicalResource = None
    

    def __init__(self, column: int, row: int, columns: int, rows: int, width: int, height: int, geologicalResource: GeologicalResource) -> None:
        __class__._java_defaults(self)
        super().__init__(column, row, columns, rows, width, height)
        __class__._init_fields(self)
        self.geologicalResource = geologicalResource
    

    def getGeologicalResource(self) -> GeologicalResource:
        return self.geologicalResource


