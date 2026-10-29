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
# package org.allbinary.game.layer.geographic.map

from __future__ import annotations



class LayerPartialCellPositionsUtil:
    instance: LayerPartialCellPositionsUtil = None
    

    # throws Exception
    def getAll(self, geographicMapInterface: BasicGeographicMap, layerInterface: AllBinaryLayer, reusableList: BasicArrayList) -> BasicArrayList:
        reusableList.clear()
        topLeftGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP(), layerInterface.getYP())
        topRightGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP() + layerInterface.getWidth(), layerInterface.getYP())
        bottomLeftGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP(), layerInterface.getYP() + layerInterface.getHeight())
        bottomRightGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP() + layerInterface.getWidth(), layerInterface.getYP() + layerInterface.getHeight())
        if topLeftGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            reusableList.add(topLeftGeographicMapCellPosition)
        if topRightGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and topLeftGeographicMapCellPosition != topRightGeographicMapCellPosition:
            reusableList.add(topRightGeographicMapCellPosition)
        if bottomLeftGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and not reusableList.contains(bottomLeftGeographicMapCellPosition):
            reusableList.add(bottomLeftGeographicMapCellPosition)
        if bottomRightGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and not reusableList.contains(bottomRightGeographicMapCellPosition):
            reusableList.add(bottomRightGeographicMapCellPosition)
        return reusableList
    

    # throws Exception
    def getAllDXY(self, geographicMapInterface: BasicGeographicMap, layerInterface: AllBinaryLayer, dx: int, dy: int, reusableList: BasicArrayList) -> BasicArrayList:
        reusableList.clear()
        topLeftGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP() + dx, layerInterface.getYP() + dy)
        topRightGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP() + layerInterface.getWidth() + dx, layerInterface.getYP() + dy)
        bottomLeftGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP() + dx, layerInterface.getYP() + layerInterface.getHeight() + dy)
        bottomRightGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXYNoThrow(layerInterface.getXP() + layerInterface.getWidth() + dx, layerInterface.getYP() + layerInterface.getHeight() + dy)
        if topLeftGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION:
            reusableList.add(topLeftGeographicMapCellPosition)
        if topRightGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and topLeftGeographicMapCellPosition != topRightGeographicMapCellPosition:
            reusableList.add(topRightGeographicMapCellPosition)
        if bottomLeftGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and not reusableList.contains(bottomLeftGeographicMapCellPosition):
            reusableList.add(bottomLeftGeographicMapCellPosition)
        if bottomRightGeographicMapCellPosition != SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION and not reusableList.contains(bottomRightGeographicMapCellPosition):
            reusableList.add(bottomRightGeographicMapCellPosition)
        return reusableList
    

    @staticmethod
    def getInstance() -> LayerPartialCellPositionsUtil:
        return LayerPartialCellPositionsUtil.instance
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory


LayerPartialCellPositionsUtil.instance = LayerPartialCellPositionsUtil()

