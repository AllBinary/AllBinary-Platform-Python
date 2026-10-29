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



class TopViewCharacterBehavior:
    

    # throws Exception
    def terrainEvent(self, layer: AllBinaryLayer, direction: Direction, x: int, y: int, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellPosition: GeographicMapCellPosition) -> None:
        pass
    

    def terrainMove(self, layer: AllBinaryLayer, geographicMapInterfaceArray: list[BasicGeographicMap], x: int, y: int) -> None:
        pass
    

    def hasSolidBlock(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType]) -> bool:
        size: int = len(geographicMapInterfaceArray)
        basicTopViewGeographicMapCellTypeFactory: BasicTopViewGeographicMapCellTypeFactory = None
        for index in range(0, size):
            basicTopViewGeographicMapCellTypeFactory = geographicMapInterfaceArray[index].getGeographicMapCellTypeFactory()
            if basicTopViewGeographicMapCellTypeFactory.BLOCK_CELL_TYPE.isType(geographicMapCellTypeArray[index]):
                return True
        return False
from org.allbinary.direction.Direction import Direction
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellTypeFactory import BasicTopViewGeographicMapCellTypeFactory


