# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager


class FakeLayerManager(AllBinaryGameLayerManager, GeographicMapCompositeInterface):

    def _init_fields(self) -> None:
        self.geographicMapInterfaceArray: list[BasicGeographicMap] = BasicGeographicMap.NULL_BASIC_GEOGRAPHIC_MAP_ARRAY
        self.geographicMapCellTypeArray: list[GeographicMapCellType] = GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE_ARRAY
    

    def __init__(self, gameInfo: GameInfo) -> None:
        super().__init__(BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE, gameInfo)
        self._init_fields()
    

    def getGeographicMapInterface(self) -> list[BasicGeographicMap]:
        return self.geographicMapInterfaceArray
    

    def setGeographicMapInterface(self, geographicMapInterfaceArray: list[BasicGeographicMap]) -> None:
        self.geographicMapInterfaceArray = geographicMapInterfaceArray
        self.geographicMapCellTypeArray = [None] * (len(self.geographicMapInterfaceArray))
    

    def geographicMapCellTypeArray(self) -> list[GeographicMapCellType]:
        return self.geographicMapCellTypeArray
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


