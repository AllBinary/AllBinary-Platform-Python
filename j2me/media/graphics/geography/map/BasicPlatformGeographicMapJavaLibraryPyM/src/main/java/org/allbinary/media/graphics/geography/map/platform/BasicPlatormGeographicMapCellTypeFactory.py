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

from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


@java_inherited_overloads
class BasicPlatormGeographicMapCellTypeFactory(GeographicMapCellTypeFactory):
    def _java_defaults(self):
        vars(self).setdefault("enumerationUtil", None)
        vars(self).setdefault("BLOCK_CELL_TYPE", None)
        vars(self).setdefault("JUMP_THRU_CELL_TYPE", None)
        vars(self).setdefault("LADDER_CELL_TYPE", None)
        vars(self).setdefault("maxTileId", 0)

    def _init_fields(self) -> None:
        from org.allbinary.util.EnumerationUtil import EnumerationUtil
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()
        if "BLOCK_CELL_TYPE" not in vars(self): self.BLOCK_CELL_TYPE: BasicPlatormGeographicMapCellType = None
        if "JUMP_THRU_CELL_TYPE" not in vars(self): self.JUMP_THRU_CELL_TYPE: BasicPlatormGeographicMapCellType = None
        if "LADDER_CELL_TYPE" not in vars(self): self.LADDER_CELL_TYPE: BasicPlatormGeographicMapCellType = None
        if "maxTileId" not in vars(self): self.maxTileId: int = 0
    

    def __init__(self, tileTypeToTileIdsMap: ABHashtable[object, object], maxTileId: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.graphics.geography.map.platform.BasicPlatormGeographicMapCellType import BasicPlatormGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.platform.BasicPlatormGeographicMapCellType import BasicPlatormGeographicMapCellType
        from java.util.Enumeration import Enumeration
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        from org.allbinary.util.ABHashtable import ABHashtable
        from org.allbinary.util.BasicArrayList import BasicArrayList
        super().__init__()
        __class__._init_fields(self)
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
            if java_equals(key, PLATFORM):
                BLOCK_CELL_TYPE = basicPlatormGeographicMapCellType
            if java_equals(key, JUMP_TRHU):
                JUMP_THRU_CELL_TYPE = basicPlatormGeographicMapCellType
            if java_equals(key, LADDER):
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
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        if cellType.getType() == 0:
            return True
        return False
# from java.util.Enumeration import Enumeration
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.EnumerationUtil import EnumerationUtil


