# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.behavior.topview

from __future__ import annotations

from org.allbinary.game.behavior.topview.TopViewCharacterBehavior import TopViewCharacterBehavior


class NonPlayerTopViewCharacterBehavior(TopViewCharacterBehavior):

    def _init_fields(self) -> None:
        self.geographicMapBehavior: MultiGeographicMapBehavior = MultiGeographicMapBehavior()
        self.CLIFF: BasicTerrainInfo = BasicTerrainInfo(AngleFactory.getInstance().DOWN)

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def terrainEvent(self, layer: AllBinaryLayer, direction: Direction, x: int, y: int, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition) -> None:
        maxColumns: int = geographicMapInterfaceArray[0].getAllBinaryTiledLayer().getColumns()
        if geographicMapCellPosition.getColumn() > 0 and geographicMapCellPosition.getColumn() < maxColumns:
            nextTerrainGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
            geographicMapCellPositionFactory: BasicGeographicMapCellPositionFactory = geographicMapInterfaceArray[0].getGeographicMapCellPositionFactory()
            if direction == DirectionFactory.getInstance().LEFT:
                nextTerrainGeographicMapCellPosition = geographicMapCellPositionFactory.getAt(geographicMapCellPosition.getColumn() - 1, geographicMapCellPosition.getRow())
            elif direction == DirectionFactory.getInstance().RIGHT:
                nextTerrainGeographicMapCellPosition = geographicMapCellPositionFactory.getAt(geographicMapCellPosition.getColumn() + 1, geographicMapCellPosition.getRow())
            self.geographicMapBehavior.getCellTypeAt(geographicMapInterfaceArray, geographicMapCellTypeArray, nextTerrainGeographicMapCellPosition)
            hasSolidBlock: bool = self.hasSolidBlock(geographicMapInterfaceArray, geographicMapCellTypeArray)
            if not hasSolidBlock:
                terrainEvent: TerrainEvent = TerrainEventCircularStaticPool.getInstance().getNext(self.CLIFF)
                TerrainEventHandler.getInstance(layer).fireEvent(terrainEvent)
    

    def terrainMove(self, layer: AllBinaryLayer, geographicMapInterfaceArray: list[BasicGeographicMap], x: int, y: int) -> None:
        layer.moveDXY(x, y)
from org.allbinary.media.graphics.geography.map.MultiGeographicMapBehavior import MultiGeographicMapBehavior
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.terrain.BasicTerrainInfo import BasicTerrainInfo
from org.allbinary.game.terrain.TerrainEvent import TerrainEvent
from org.allbinary.game.terrain.TerrainEventCircularStaticPool import TerrainEventCircularStaticPool
from org.allbinary.game.terrain.TerrainEventHandler import TerrainEventHandler
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory


