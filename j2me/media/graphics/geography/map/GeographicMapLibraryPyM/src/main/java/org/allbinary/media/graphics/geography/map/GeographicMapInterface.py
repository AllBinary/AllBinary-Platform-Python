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



# Java interface
class GeographicMapInterface:
    

    def getId(self) -> int:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def reset(self) -> None:
        raise NotImplementedError()
    

    def getAllBinaryTiledLayer(self) -> AllBinaryTiledLayer:
        raise NotImplementedError()
    

    # throws Exception
    def getCellPositionsAt(self, layer: Layer, currentCellPositionArray: list[list[GeographicMapCellPosition]], cellPositionArray: list[list[GeographicMapCellPosition]]) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def getCellPositionAtXY(self, x: int, y: int) -> GeographicMapCellPosition:
        raise NotImplementedError()
    

    # throws Exception
    def getCellPositionAtXYNoThrow(self, x: int, y: int) -> GeographicMapCellPosition:
        raise NotImplementedError()
    

    def getCellTypeFromMapCellTypeInt(self, cellTypeId: int) -> int:
        raise NotImplementedError()
    

    # throws Exception
    def getCellTypeAtXY(self, x: int, y: int) -> GeographicMapCellType:
        raise NotImplementedError()
    

    # throws Exception
    def getCellTypeAt(self, geographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellType:
        raise NotImplementedError()
    

    def getGeographicMapCellPositionFactory(self) -> BasicGeographicMapCellPositionFactory:
        raise NotImplementedError()
    

    def getGeographicMapCellPositionFactoryInterface(self) -> GeographicMapCellPositionFactoryInterface:
        raise NotImplementedError()
    

    def getForegroundBasicColor(self) -> BasicColor:
        raise NotImplementedError()
    

    def getBackgroundBasicColor(self) -> BasicColor:
        raise NotImplementedError()
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.layer.Layer import Layer


