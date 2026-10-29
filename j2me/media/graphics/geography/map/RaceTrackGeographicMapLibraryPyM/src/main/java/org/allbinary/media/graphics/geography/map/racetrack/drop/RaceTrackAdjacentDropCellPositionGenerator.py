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


class RaceTrackAdjacentDropCellPositionGenerator(RaceTrackDropCellPositionGenerator):
    SINGLETON: RaceTrackAdjacentDropCellPositionGenerator = None

    def _init_fields(self) -> None:
        self.layerCoveringCellPositionsUtil: LayerCoveringCellPositionsUtil = LayerCoveringCellPositionsUtil.getInstance()
        self.groupCommonFactory: GroupCommonFactory = GroupCommonFactory.getInstance()
        self.surroundingCellPositions: list[GeographicMapCellPosition] = [None] * (4)
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.geographicMapDirectionUtil: GeographicMapDirectionUtil = GeographicMapDirectionUtil.getInstance()
    

    @staticmethod
    def getInstance() -> DropCellPositionGeneratorInterface:
        return RaceTrackAdjacentDropCellPositionGenerator.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def getFirstNonRoadAdjacentCellPosition(self, column: int, row: int) -> GeographicMapCellPosition:
        nonRoadGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = self.raceTrackGeographicMap.getGeographicMapCellPositionFactory()
        self.surroundingCellPositions[0] = geographicMapCellPositionFactory.getAt(column, row - 1)
        self.surroundingCellPositions[1] = geographicMapCellPositionFactory.getAt(column, row + 1)
        self.surroundingCellPositions[2] = geographicMapCellPositionFactory.getAt(column - 1, row)
        self.surroundingCellPositions[3] = geographicMapCellPositionFactory.getAt(column + 1, row)
        baseRaceTrackGeographicMap: BaseRaceTrackGeographicMap = self.raceTrackGeographicMap
        raceTrackGeographicMapCellTypeFactory: RaceTrackGeographicMapCellTypeFactory = baseRaceTrackGeographicMap.getGeographicMapCellTypeFactory()
        geographicMapCellPosition: GeographicMapCellPosition = None
        raceTrackGeographicMapCellType: RaceTrackGeographicMapCellType = None
        index = len(self.surroundingCellPositions)
        while (index := index - 1) >= 0:
            geographicMapCellPosition = self.surroundingCellPositions[index]
            raceTrackGeographicMapCellType = self.raceTrackGeographicMap.getCellTypeAt(geographicMapCellPosition)
            if not raceTrackGeographicMapCellTypeFactory.isPath(raceTrackGeographicMapCellType):
                nonRoadGeographicMapCellPosition = geographicMapCellPosition
                break
        return nonRoadGeographicMapCellPosition
    

    # throws Exception
    def update(self, allBinaryGameLayerManager: AllBinaryGameLayerManager, geographicMapInterface: BasicGeographicMap) -> None:
        self.hashtable.put(AllBinaryGameLayerManager.ID, allBinaryGameLayerManager)
        super().update(allBinaryGameLayerManager, geographicMapInterface)
    

    # throws Exception
    def drop(self, allBinaryLayerManager: AllBinaryLayerManager, index: int) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.drop.RaceTrackAdjacentDropLayerFactory import RaceTrackAdjacentDropLayerFactory
        geographicMapCellPosition: GeographicMapCellPosition = self.list_.get(index)
        randomGeographicMapCellPosition: GeographicMapCellPosition = self.getFirstNonRoadAdjacentCellPosition(geographicMapCellPosition.getColumn(), geographicMapCellPosition.getRow())
        if randomGeographicMapCellPosition is None:
            return
        dropCellPositionHistory: DropCellPositionHistory = DropCellPositionHistory.getInstance()
        if not dropCellPositionHistory.isCellPositionWithDrop(geographicMapCellPosition):
            direction: Direction = self.geographicMapDirectionUtil.getDirectionFromCellPositionToAdjacentCellPosition(randomGeographicMapCellPosition, geographicMapCellPosition)
            objectCanBeNull: object = self.hashtable.get(self.groupCommonFactory.ID)
            if objectCanBeNull is not None:
                pass
            else:
                self.hashtable.put(self.groupCommonFactory.ID, BasicGroupFactory.getInstance().NONE_ARRAY)
            self.hashtable.put(DirectionFactory.getInstance().NAME, direction)
            point: GPoint = randomGeographicMapCellPosition.getPoint()
            x: int = point.getX()
            y: int = point.getY()
            z: int = point.getZ()
            layerInterface: AllBinaryLayer = RaceTrackAdjacentDropLayerFactory.getInstance().getRandomInstance().getNextInstance(self.hashtable, x, y, z)
            baseRaceTrackGeographicMap: BaseRaceTrackGeographicMap = self.raceTrackGeographicMap
            list_: BasicArrayList = self.layerCoveringCellPositionsUtil.getAll(baseRaceTrackGeographicMap, randomGeographicMapCellPosition, layerInterface, BasicArrayListD())
            if dropCellPositionHistory.anyCellPositionWithDrop(list_):
                return
            geographicMapCellType: GeographicMapCellType = None
            index2 = list_.size()
            while (index2 := index2 - 1) >= 0:
                geographicMapCellType = self.raceTrackGeographicMap.getCellTypeAt(list_.get(index2))
                if self.raceTrackGeographicMapCellTypeFactory.isPath(geographicMapCellType):
                    return
            dropCellPositionHistory.addAll(list_, layerInterface)
            allBinaryLayerManager.append(layerInterface)
from org.allbinary.game.identification.GroupCommonFactory import GroupCommonFactory
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.geographic.map.LayerCoveringCellPositionsUtil import LayerCoveringCellPositionsUtil
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.GeographicMapDirectionUtil import GeographicMapDirectionUtil
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionGeneratorInterface import DropCellPositionGeneratorInterface
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory
from org.allbinary.media.graphics.geography.map.racetrack.BaseRaceTrackGeographicMap import BaseRaceTrackGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypeFactory import RaceTrackGeographicMapCellTypeFactory
from org.allbinary.util.ABHashtable import ABHashtable


RaceTrackAdjacentDropCellPositionGenerator.SINGLETON = RaceTrackAdjacentDropCellPositionGenerator()

