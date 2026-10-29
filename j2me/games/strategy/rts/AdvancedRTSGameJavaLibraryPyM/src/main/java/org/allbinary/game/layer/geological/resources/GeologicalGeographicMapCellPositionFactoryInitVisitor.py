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

from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInitVisitorInterface import GeographicMapCellPositionFactoryInitVisitorInterface


class GeologicalGeographicMapCellPositionFactoryInitVisitor(GeographicMapCellPositionFactoryInitVisitorInterface):
    

    # throws Exception
    def visit(self, tiledLayer: AllBinaryTiledLayer, cellPosition: GeographicMapCellPosition) -> None:
        geologicalGeographicMapCellPosition: GeologicalGeographicMapCellPosition = (cellPosition)
        geologicalGeographicMapCellPosition.getGeologicalResource().init()
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


