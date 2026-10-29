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
# package org.allbinary.media.graphics.geography.map.racetrack.drop

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.racetrack.drop.RaceTrackDropCellPositionGenerator import RaceTrackDropCellPositionGenerator


class RaceTrackRandomDropCellPositionGenerator(RaceTrackDropCellPositionGenerator):
    SINGLETON: RaceTrackRandomDropCellPositionGenerator = None

    def _init_fields(self) -> None:
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
        self.cellsPerRowOrColumn: int = 3
        self.totalCells: int = self.cellsPerRowOrColumn * self.cellsPerRowOrColumn
        self.rowArray: list[int] = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        self.columnArray: list[int] = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        self.cellWidth: int = 0
        self.cellHeight: int = 0
    

    @staticmethod
    def getInstance() -> RaceTrackRandomDropCellPositionGenerator:
        return RaceTrackRandomDropCellPositionGenerator.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def update(self, allBinaryGameLayerManager: AllBinaryGameLayerManager, geographicMapInterface: BasicGeographicMap) -> None:
        super().update(allBinaryGameLayerManager, geographicMapInterface)
        tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        self.cellWidth = tiledLayer.getCellWidth() / self.cellsPerRowOrColumn
        self.cellHeight = tiledLayer.getCellHeight() / self.cellsPerRowOrColumn
    

    # throws Exception
    def drop(self, allBinaryLayerManager: AllBinaryLayerManager, index: int) -> None:
        geographicMapCellPosition: GeographicMapCellPosition = self.list_.get(index)
        point: GPoint = geographicMapCellPosition.getPoint()
        randomCell: int = self.myRandomFactory.getAbsoluteNextInt(self.totalCells)
        row: int = self.rowArray[randomCell]
        column: int = self.columnArray[randomCell]
        x: int = point.getX() + (row * self.cellWidth)
        y: int = point.getY() + (column * self.cellHeight)
        pickedUpLayerInterfaceFactory: PickedUpLayerInterfaceFactoryInterface = DropLayerFactory.getInstance().getRandomInstance()
        tiledLayer: AllBinaryTiledLayer = self.raceTrackGeographicMap.getAllBinaryTiledLayer()
        pickupLayer: RaceTrackPickupLayer = PickupLayerCircularStaticPool.getInstance().getInstanceXYZ(pickedUpLayerInterfaceFactory, x, y, tiledLayer.getZP() + 3)
        pickupLayer.setTiledLayer(tiledLayer)
        allBinaryLayerManager.append(pickupLayer)
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.layer.drop.DropLayerFactory import DropLayerFactory
from org.allbinary.game.layer.pickup.PickupLayerCircularStaticPool import PickupLayerCircularStaticPool
from org.allbinary.game.layer.pickup.RaceTrackPickupLayer import RaceTrackPickupLayer
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


RaceTrackRandomDropCellPositionGenerator.SINGLETON = RaceTrackRandomDropCellPositionGenerator()

