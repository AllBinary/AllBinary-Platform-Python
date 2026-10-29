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
# package org.allbinary.media.graphics.geography.map.racetrack

from __future__ import annotations



class RaceTrackData:

    def _init_fields(self) -> None:
        self.tileSetImage: Image = NullImage.NULL_IMAGE
        self.miniTileSetImage: Image = NullImage.NULL_IMAGE
        self.cellWidth: int = 0
        self.cellHeight: int = 0
        self.miniCellWidth: int = 0
        self.miniCellHeight: int = 0
        self.mapArray: list[list[int]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY
        self.cellTypeIdToGeographicMapCellTypeArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
        self.NO_OVER_PASSES_ARRAY: list[CellPosition] = [None] * (0)
        self.overPassGeographicMapCellPositionArray: list[CellPosition] = self.NO_OVER_PASSES_ARRAY
        self.id: int = None
    

    def __init__(self, id: int, cellWidth: int, cellHeight: int, miniCellWidth: int, miniCellHeight: int, cellTypeIdToGeographicMapCellTypeArray: list[int], mapArray: list[list[int]]) -> None:
        self._init_fields()
        self.id = id
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.miniCellWidth = miniCellWidth
        self.miniCellHeight = miniCellHeight
        self.mapArray = mapArray
        self.cellTypeIdToGeographicMapCellTypeArray = cellTypeIdToGeographicMapCellTypeArray
    

    def setMapArray(self, mapArray: list[list[int]]) -> None:
        self.mapArray = mapArray
    

    def getMapArray(self) -> list[list[int]]:
        return self.mapArray
    

    def setCellTypeIdToGeographicMapCellTypeArray(self, cellTypeIdToGeographicMapCellTypeArray: list[int]) -> None:
        self.cellTypeIdToGeographicMapCellTypeArray = cellTypeIdToGeographicMapCellTypeArray
    

    def getCellTypeIdToGeographicMapCellTypeArray(self) -> list[int]:
        return self.cellTypeIdToGeographicMapCellTypeArray
    

    def setCellWidth(self, cellWidth: int) -> None:
        self.cellWidth = cellWidth
    

    def getCellWidth(self) -> int:
        return self.cellWidth
    

    def setCellHeight(self, cellHeight: int) -> None:
        self.cellHeight = cellHeight
    

    def getCellHeight(self) -> int:
        return self.cellHeight
    

    def getOverPassGeographicMapCellPositionArray(self) -> list[CellPosition]:
        return self.overPassGeographicMapCellPositionArray
    

    def setOverPassGeographicMapCellPositionArray(self, overPassGeographicMapCellPositionArray: list[CellPosition]) -> None:
        self.overPassGeographicMapCellPositionArray = overPassGeographicMapCellPositionArray
    

    def getTileSetImage(self) -> Image:
        return self.tileSetImage
    

    def setTileSetImage(self, tileSetImage: Image) -> None:
        self.tileSetImage = tileSetImage
    

    def getMiniTileSetImage(self) -> Image:
        return self.miniTileSetImage
    

    def setMiniTileSetImage(self, miniTileSetImage: Image) -> None:
        self.miniTileSetImage = miniTileSetImage
    

    def getMiniCellWidth(self) -> int:
        return self.miniCellWidth
    

    def setMiniCellWidth(self, miniCellWidth: int) -> None:
        self.miniCellWidth = miniCellWidth
    

    def getMiniCellHeight(self) -> int:
        return self.miniCellHeight
    

    def setMiniCellHeight(self, miniCellHeight: int) -> None:
        self.miniCellHeight = miniCellHeight
    

    def setId(self, id: int) -> None:
        self.id = id
    

    def getId(self) -> int:
        return self.id
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
from org.allbinary.graphics.CellPosition import CellPosition
from org.allbinary.logic.NullUtil import NullUtil


