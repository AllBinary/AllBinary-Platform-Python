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

from org.allbinary.game.behavior.topview.TopViewGameLayerBehavior import TopViewGameLayerBehavior


class GeographicMapTopViewLayerBehavior(TopViewGameLayerBehavior):
    

    def __init__(self, maxGravityActionIndex: int) -> None:
        super().__init__(maxGravityActionIndex)
    

    # throws Exception
    def getGeographicMapCellPositionIfNotSolidBlockOrOffMapLocation(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer, x: int, y: int) -> GeographicMapCellPosition:
        return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    # throws Exception
    def getGeographicMapCellPositionIfNotSolidBlockOrOffMap(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition, velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> GeographicMapCellPosition:
        return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    # throws Exception
    def getGeographicMapCellPositionFromListIfNotSolidBlockOrOffMap(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPositionList: BasicArrayList, velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> GeographicMapCellPosition:
        return SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
    

    # throws Exception
    def gravity(self, velocityProperties: VelocityProperties, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition) -> None:
        pass
    

    # throws Exception
    def left(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> None:
        pass
    

    # throws Exception
    def move(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer, x: int, y: int) -> bool:
        return False
    

    # throws Exception
    def moveAndLand(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition, velocityProperties: VelocityProperties, layer: AllBinaryLayer, x: int, y: int) -> None:
        pass
    

    # throws Exception
    def right(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], velocityProperties: VelocityProperties, layer: AllBinaryLayer) -> None:
        pass
    

    def hasSolidBlock(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType]) -> bool:
        size: int = len(geographicMapInterfaceArray)
        basicTopViewGeographicMapCellTypeFactory: BasicTopViewGeographicMapCellTypeFactory = None
        for index in range(0, size):
            basicTopViewGeographicMapCellTypeFactory = geographicMapInterfaceArray[index].getGeographicMapCellTypeFactory()
            if basicTopViewGeographicMapCellTypeFactory.BLOCK_CELL_TYPE.isType(geographicMapCellTypeArray[index]):
                return True
        return False
    

    def isOffMap(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType]) -> bool:
        size: int = len(geographicMapInterfaceArray)
        basicTopViewGeographicMapCellTypeFactory: BasicTopViewGeographicMapCellTypeFactory = None
        for index in range(0, size):
            basicTopViewGeographicMapCellTypeFactory = geographicMapInterfaceArray[index].getGeographicMapCellTypeFactory()
            if basicTopViewGeographicMapCellTypeFactory.OFF_MAP_CELL_TYPE.isType(geographicMapCellTypeArray[index]):
                return True
        return False
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellTypeFactory import BasicTopViewGeographicMapCellTypeFactory
from org.allbinary.util.BasicArrayList import BasicArrayList


