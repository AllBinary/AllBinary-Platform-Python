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
# package org.allbinary.media.graphics.geography.map.platform

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


class BasicPlatormGeographicMapCellTypeFactory(GeographicMapCellTypeFactory):

    def _init_fields(self) -> None:
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        self.BLOCK_CELL_TYPE: BasicPlatormGeographicMapCellType = None
        self.JUMP_THRU_CELL_TYPE: BasicPlatormGeographicMapCellType = None
        self.LADDER_CELL_TYPE: BasicPlatormGeographicMapCellType = None
        self.maxTileId: int = None
    

    def __init__(self, tileTypeToTileIdsMap: ABHashtable[object, object], maxTileId: int) -> None:
        from org.allbinary.media.graphics.geography.map.platform.BasicPlatormGeographicMapCellType import BasicPlatormGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.platform.BasicPlatormGeographicMapCellType import BasicPlatormGeographicMapCellType
        super().__init__()
        self._init_fields()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(commonStrings.START, self, commonStrings.INIT)
        self.maxTileId = maxTileId
        GeographicMapCellType(0, 0)
        BLOCK_CELL_TYPE: BasicPlatormGeographicMapCellType = BasicPlatormGeographicMapCellType.createType(1)
        JUMP_THRU_CELL_TYPE: BasicPlatormGeographicMapCellType = BLOCK_CELL_TYPE
        LADDER_CELL_TYPE: BasicPlatormGeographicMapCellType = BLOCK_CELL_TYPE
        PLATFORM: str = "Platform"
        JUMP_TRHU: str = "JumpThru"
        LADDER: str = "Ladder"
        enumeration: Enumeration = tileTypeToTileIdsMap.keys()
        idsWithTypeList: BasicArrayList = None
        key: str = None
        basicPlatormGeographicMapCellType: BasicPlatormGeographicMapCellType = None
        while self.enumerationUtil.hasMoreElements(enumeration):
            key = self.enumerationUtil.nextElement(enumeration)
            self.logUtil.putF(key, self, commonStrings.INIT)
            idsWithTypeList = tileTypeToTileIdsMap.get(key)
            basicPlatormGeographicMapCellType = BasicPlatormGeographicMapCellType(idsWithTypeList)
            if (key == PLATFORM):
                BLOCK_CELL_TYPE = basicPlatormGeographicMapCellType
            if (key == JUMP_TRHU):
                JUMP_THRU_CELL_TYPE = basicPlatormGeographicMapCellType
            if (key == LADDER):
                LADDER_CELL_TYPE = basicPlatormGeographicMapCellType
        self.BLOCK_CELL_TYPE = BLOCK_CELL_TYPE
        self.JUMP_THRU_CELL_TYPE = JUMP_THRU_CELL_TYPE
        self.LADDER_CELL_TYPE = LADDER_CELL_TYPE
        GeographicMapCellType(self.maxTileId - 1, 0)
        GeographicMapCellType(self.maxTileId - 2, 0)
    

    def getStartType(self) -> int:
        return self.maxTileId - 1
    

    def getEndType(self) -> int:
        return self.maxTileId - 2
    

    def getEmptyType(self) -> int:
        return 0
    

    def isPath(self, cellType: GeographicMapCellType) -> bool:
        if cellType.getType() == 0:
            return True
        return False
# from java.util.Enumeration import Enumeration
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.EnumerationUtil import EnumerationUtil


