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



class LayerCoveringCellPositionsUtil:
    instance: LayerCoveringCellPositionsUtil = None

    def _init_fields(self) -> None:
        self.cellPositionsUtil: CellPositionsUtil = CellPositionsUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LayerCoveringCellPositionsUtil:
        return LayerCoveringCellPositionsUtil.instance
    

    # throws Exception
    def getAllXY(self, geographicMapInterface: BasicGeographicMap, layerInterface: AllBinaryLayer, x: int, y: int, reusableList: BasicArrayList) -> BasicArrayList:
        topLeftGeographicMapCellPosition: GeographicMapCellPosition = geographicMapInterface.getCellPositionAtXY(x, y)
        return self.getAll(geographicMapInterface, topLeftGeographicMapCellPosition, layerInterface, reusableList)
    

    # throws Exception
    def getAll(self, geographicMapInterface: BasicGeographicMap, topLeftGeographicMapCellPosition: GeographicMapCellPosition, layerInterface: AllBinaryLayer, reusableList: BasicArrayList) -> BasicArrayList:
        reusableList.clear()
        columns: int = layerInterface.getWidth() / geographicMapInterface.getAllBinaryTiledLayer().getCellWidth()
        rows: int = layerInterface.getHeight() / geographicMapInterface.getAllBinaryTiledLayer().getCellHeight()
        if columns == 0:
            columns = 1
        if rows == 0:
            rows = 1
        return self.cellPositionsUtil.getAll(geographicMapInterface, topLeftGeographicMapCellPosition, columns, rows, reusableList)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.CellPositionsUtil import CellPositionsUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


LayerCoveringCellPositionsUtil.instance = LayerCoveringCellPositionsUtil()

