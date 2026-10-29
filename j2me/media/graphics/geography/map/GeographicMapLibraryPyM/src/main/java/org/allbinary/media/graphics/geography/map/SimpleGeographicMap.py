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



class SimpleGeographicMap:

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.id: int = None
        self.name: str = None
        self.cellTypeIdToGeographicMapCellType: list[int] = None
        self.tiledLayer: AllBinaryTiledLayer = None
        self.foregroundBasicColor: BasicColor = BasicColorFactory.getInstance().NULL_COLOR
        self.backgroundBasicColor: BasicColor = BasicColorFactory.getInstance().NULL_COLOR
        self.geographicMapCellTypeFactory: GeographicMapCellTypeFactory = GeographicMapCellTypeFactory.getInstance()
    

    def __init__(self, id: int, name: str, cellTypeIdToGeographicMapCellType: list[int], tiledLayer: AllBinaryTiledLayer, foregroundBasicColor: BasicColor, backgroundBasicColor: BasicColor) -> None:
        self._init_fields()
        self.id = id
        self.name = name
        self.cellTypeIdToGeographicMapCellType = cellTypeIdToGeographicMapCellType
        self.tiledLayer = tiledLayer
        self.setBackgroundBasicColor(backgroundBasicColor)
        self.setForegroundBasicColor(foregroundBasicColor)
    

    def getId(self) -> int:
        return self.id
    

    def getName(self) -> str:
        return self.name
    

    def reset(self) -> None:
        pass
    

    def getAllBinaryTiledLayer(self) -> AllBinaryTiledLayer:
        return self.tiledLayer
    

    # throws Exception
    def getCellTypeAt(self, cellPosition: GeographicMapCellPosition) -> GeographicMapCellType:
        i_column: int = cellPosition.getColumn()
        i_row: int = cellPosition.getRow()
        cellTypeId: int = self.tiledLayer.getCell(i_column, i_row)
        if cellTypeId < 0:
            cellTypeId = self.tiledLayer.getAnimatedTile(cellTypeId)
        return self.geographicMapCellTypeFactory.get(self.cellTypeIdToGeographicMapCellType[cellTypeId])
    

    def getCellTypeFromMapCellTypeInt(self, cellTypeId: int) -> int:
        return self.cellTypeIdToGeographicMapCellType[cellTypeId]
    

    def getForegroundBasicColor(self) -> BasicColor:
        return self.foregroundBasicColor
    

    def setForegroundBasicColor(self, foregroundBasicColor: BasicColor) -> None:
        self.foregroundBasicColor = foregroundBasicColor
    

    def getBackgroundBasicColor(self) -> BasicColor:
        return self.backgroundBasicColor
    

    def setBackgroundBasicColor(self, backgroundBasicColor: BasicColor) -> None:
        self.backgroundBasicColor = backgroundBasicColor
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


