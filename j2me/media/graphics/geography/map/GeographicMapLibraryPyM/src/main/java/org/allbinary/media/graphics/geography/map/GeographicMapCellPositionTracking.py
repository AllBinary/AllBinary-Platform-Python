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



class GeographicMapCellPositionTracking:

    def _init_fields(self) -> None:
        self.currentGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.previousGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.newGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.currentCellType: GeographicMapCellType = GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getCurrentOverCellType(self, geographicMap: BasicGeographicMap) -> GeographicMapCellType:
        geographicMapCellPosition: GeographicMapCellPosition = self.currentGeographicMapCellPosition
        if geographicMapCellPosition != self.previousGeographicMapCellPosition:
            self.currentCellType = geographicMap.getCellTypeAt(geographicMapCellPosition)
        return self.currentCellType
    

    # throws Exception
    def updateStart(self, gameCanvasInterface: AllBinaryGameCanvasInterface, layer: AllBinaryLayer) -> bool:
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        if gameCanvasInterface != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            geographicMapCompositeInterface: GeographicMapCompositeInterface = gameCanvasInterface.getLayerManager()
            geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
            self.newGeographicMapCellPosition = geographicMapInterface.getCellPositionAtXY(layer.getXP() + layer.getHalfWidth(), layer.getYP() + layer.getHalfHeight())
            if self.newGeographicMapCellPosition != self.currentGeographicMapCellPosition:
                self.currentGeographicMapCellPosition = self.newGeographicMapCellPosition
                return True
        return False
    

    def updateEnd(self) -> bool:
        if self.currentGeographicMapCellPosition != self.previousGeographicMapCellPosition:
            self.previousGeographicMapCellPosition = self.currentGeographicMapCellPosition
            return True
        return False
    

    def getPreviousGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.previousGeographicMapCellPosition
    

    def getCurrentGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.currentGeographicMapCellPosition
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvasInterface import AllBinaryGameCanvasInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


