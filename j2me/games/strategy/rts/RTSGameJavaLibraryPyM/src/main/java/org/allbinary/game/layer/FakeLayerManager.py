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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager


@java_inherited_overloads
class FakeLayerManager(*java_bases(AllBinaryGameLayerManager, GeographicMapCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("geographicMapInterfaceArray", None)
        vars(self).setdefault("cachedGeographicMapCellTypes", None)

    def _init_fields(self) -> None:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        self.geographicMapInterfaceArray: list[BasicGeographicMap] = BasicGeographicMap.NULL_BASIC_GEOGRAPHIC_MAP_ARRAY
        self.cachedGeographicMapCellTypes: list[GeographicMapCellType] = GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE_ARRAY
    

    def __init__(self, gameInfo: GameInfo) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.GameInfo import GameInfo
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        super().__init__(BasicColorFactory.getInstance().BLACK, BasicColorFactory.getInstance().WHITE, gameInfo)
        __class__._init_fields(self)
    

    def getGeographicMapInterface(self) -> list[BasicGeographicMap]:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        return self.geographicMapInterfaceArray
    

    def setGeographicMapInterface(self, geographicMapInterfaceArray: list[BasicGeographicMap]) -> None:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        self.geographicMapInterfaceArray = geographicMapInterfaceArray
        self.cachedGeographicMapCellTypes = [None] * (len(self.geographicMapInterfaceArray))
    

    def geographicMapCellTypeArray(self) -> list[GeographicMapCellType]:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        return self.cachedGeographicMapCellTypes
# from org.allbinary.game.GameInfo import GameInfo
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


