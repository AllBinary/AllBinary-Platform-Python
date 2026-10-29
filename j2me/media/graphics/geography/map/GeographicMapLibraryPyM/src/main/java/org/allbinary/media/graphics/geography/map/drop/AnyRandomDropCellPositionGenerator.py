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
# package org.allbinary.media.graphics.geography.map.drop

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.drop.BaseDropCellPositionGenerator import BaseDropCellPositionGenerator


class AnyRandomDropCellPositionGenerator(BaseDropCellPositionGenerator):

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListD()
        self.geographicMapInterface: object = NullUtil.getInstance().NULL_OBJECT

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def update(self, allBinaryGameLayerManager: AllBinaryGameLayerManager, geographicMapInterface: BasicGeographicMap) -> None:
        self.geographicMapInterface = geographicMapInterface
        basicGeographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterface.getGeographicMapCellPositionFactory()
        randomFactory: MyRandomFactory = MyRandomFactory.getInstance()
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        total: int = tiledLayer.getColumns() * tiledLayer.getRows()
        randomColumn: int = 0
        randomRow: int = 0
        geographicMapCellPosition: GeographicMapCellPosition = None
        index = total
        while (index := index - 1) >= 0:
            randomColumn = randomFactory.getAbsoluteNextInt(tiledLayer.getColumns())
            randomRow = randomFactory.getAbsoluteNextInt(tiledLayer.getRows())
            geographicMapCellPosition = basicGeographicMapCellPositionFactory.getAt(randomColumn, randomRow)
            if self.isDropAllowedAt(geographicMapCellPosition):
                self.list_.add(geographicMapCellPosition)
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        pass
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap


