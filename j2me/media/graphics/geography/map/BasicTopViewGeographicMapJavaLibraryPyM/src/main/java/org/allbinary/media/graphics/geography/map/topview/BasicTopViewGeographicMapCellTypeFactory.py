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
# package org.allbinary.media.graphics.geography.map.topview

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


@java_inherited_overloads
class BasicTopViewGeographicMapCellTypeFactory(GeographicMapCellTypeFactory):
    def _java_defaults(self):
        vars(self).setdefault("BLOCK_CELL_TYPE", None)
        vars(self).setdefault("OFF_MAP_CELL_TYPE", None)
        vars(self).setdefault("FLOOR_CELL_TYPE", None)
        vars(self).setdefault("DOOR_CELL_TYPE", None)
        vars(self).setdefault("STAIRS_UP_CELL_TYPE", None)
        vars(self).setdefault("STAIRS_DOWN_CELL_TYPE", None)
        vars(self).setdefault("OTHER_CELL_TYPE", None)
        vars(self).setdefault("maxTileId", 0)

    def _init_fields(self) -> None:
        if "BLOCK_CELL_TYPE" not in vars(self): self.BLOCK_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "OFF_MAP_CELL_TYPE" not in vars(self): self.OFF_MAP_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "FLOOR_CELL_TYPE" not in vars(self): self.FLOOR_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "DOOR_CELL_TYPE" not in vars(self): self.DOOR_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "STAIRS_UP_CELL_TYPE" not in vars(self): self.STAIRS_UP_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "STAIRS_DOWN_CELL_TYPE" not in vars(self): self.STAIRS_DOWN_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "OTHER_CELL_TYPE" not in vars(self): self.OTHER_CELL_TYPE: BasicTopViewGeographicMapCellType = None
        if "maxTileId" not in vars(self): self.maxTileId: int = 0
    

    def __init__(self, tileTypeToTileIdsMap: ABHashtable[object, object], maxTileId: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapStrings import BasicTopViewGeographicMapStrings
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.topview.BasicTopViewGeographicMapCellType import BasicTopViewGeographicMapCellType
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.util.ABHashtable import ABHashtable
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.HashtableUtil import HashtableUtil
        super().__init__()
        __class__._init_fields(self)
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.maxTileId = maxTileId
        basicTopViewGeographicMapStrings: BasicTopViewGeographicMapStrings = BasicTopViewGeographicMapStrings.getInstance()
        geographicMapCellTypeFactory: GeographicMapCellTypeFactory = GeographicMapCellTypeFactory.getInstance()
        geographicMapCellTypeArray: list[GeographicMapCellType] = geographicMapCellTypeFactory.getGeographicMapCellTypeArray()
        type_: int = 0
        if geographicMapCellTypeArray[type_] is None:
            RaceTrackGeographicMapCellType(CommonStrings.getInstance().UNKNOWN, type_, 999, 0)
        else:
            pass
        BLOCK_CELL_TYPE: BasicTopViewGeographicMapCellType = BasicTopViewGeographicMapCellType.createType(basicTopViewGeographicMapStrings.DEFAULT, 1, 1)
        OFF_MAP_CELL_TYPE: BasicTopViewGeographicMapCellType = BLOCK_CELL_TYPE
        FLOOR_CELL_TYPE: BasicTopViewGeographicMapCellType = BLOCK_CELL_TYPE
        DOOR_CELL_TYPE: BasicTopViewGeographicMapCellType = BLOCK_CELL_TYPE
        STAIRS_UP_CELL_TYPE: BasicTopViewGeographicMapCellType = BLOCK_CELL_TYPE
        STAIRS_DOWN_CELL_TYPE: BasicTopViewGeographicMapCellType = BLOCK_CELL_TYPE
        OTHER_CELL_TYPE: BasicTopViewGeographicMapCellType = BLOCK_CELL_TYPE
        keyArray: list[object] = HashtableUtil.getInstance().getKeysAsArray(tileTypeToTileIdsMap)
        size: int = len(keyArray)
        idsWithTypeList: BasicArrayList = None
        key: str = None
        basicPlatormGeographicMapCellType: BasicTopViewGeographicMapCellType = None
        for index in range(0, size):
            key = keyArray[index]
            idsWithTypeList = tileTypeToTileIdsMap.get(key)
            if java_equals(key, basicTopViewGeographicMapStrings.WALL):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.WALL, idsWithTypeList, 1000)
                BLOCK_CELL_TYPE = basicPlatormGeographicMapCellType
            elif java_equals(key, basicTopViewGeographicMapStrings.OFF_MAP):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.OFF_MAP, idsWithTypeList, 1001)
                OFF_MAP_CELL_TYPE = basicPlatormGeographicMapCellType
            elif java_equals(key, basicTopViewGeographicMapStrings.FLOOR):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.FLOOR, idsWithTypeList, 1)
                FLOOR_CELL_TYPE = basicPlatormGeographicMapCellType
            elif java_equals(key, basicTopViewGeographicMapStrings.DOOR):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.DOOR, idsWithTypeList, 1)
                DOOR_CELL_TYPE = basicPlatormGeographicMapCellType
            elif java_equals(key, basicTopViewGeographicMapStrings.STAIRS_UP):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.STAIRS_UP, idsWithTypeList, 1)
                STAIRS_UP_CELL_TYPE = basicPlatormGeographicMapCellType
            elif java_equals(key, basicTopViewGeographicMapStrings.STAIRS_DOWN):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.STAIRS_DOWN, idsWithTypeList, 1)
                STAIRS_DOWN_CELL_TYPE = basicPlatormGeographicMapCellType
            elif java_equals(key, basicTopViewGeographicMapStrings.OTHER):
                basicPlatormGeographicMapCellType = BasicTopViewGeographicMapCellType(basicTopViewGeographicMapStrings.OTHER, idsWithTypeList, 1)
                OTHER_CELL_TYPE = basicPlatormGeographicMapCellType
        self.BLOCK_CELL_TYPE = BLOCK_CELL_TYPE
        self.OFF_MAP_CELL_TYPE = OFF_MAP_CELL_TYPE
        self.FLOOR_CELL_TYPE = FLOOR_CELL_TYPE
        self.DOOR_CELL_TYPE = DOOR_CELL_TYPE
        self.STAIRS_UP_CELL_TYPE = STAIRS_UP_CELL_TYPE
        self.STAIRS_DOWN_CELL_TYPE = STAIRS_DOWN_CELL_TYPE
        self.OTHER_CELL_TYPE = OTHER_CELL_TYPE
        type_ = self.maxTileId - 1
        if geographicMapCellTypeArray[type_] is None:
            RaceTrackGeographicMapCellType(commonStrings.START, type_, 1, 0)
        else:
            pass
        type_ = self.maxTileId - 2
        if geographicMapCellTypeArray[type_] is None:
            RaceTrackGeographicMapCellType(commonStrings.START, type_, 1, 0)
        else:
            pass
    

    def getStartType(self) -> int:
        return self.maxTileId - 1
    

    def getEndType(self) -> int:
        return self.maxTileId - 2
    

    def getEmptyType(self) -> int:
        return self.FLOOR_CELL_TYPE.getTypes()[0]
    

    def isPath(self, cellType: GeographicMapCellType) -> bool:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        if self.FLOOR_CELL_TYPE.isType(cellType):
            return True
        return False
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        return str(StringMaker().append("key: WALL/BLOCK_CELL_TYPE: ").append(str(self.BLOCK_CELL_TYPE)).append("key: FLOOR_CELL_TYPE: ").append(str(self.FLOOR_CELL_TYPE)).append("key: OTHER_CELL_TYPE: ").append(str(self.OTHER_CELL_TYPE)).append("key: OFF_MAP_CELL_TYPE: ").append(str(self.OFF_MAP_CELL_TYPE)).append("key: DOOR_CELL_TYPE: ").append(str(self.DOOR_CELL_TYPE)).append("key: STAIRS_DOWN_CELL_TYPE: ").append(str(self.STAIRS_DOWN_CELL_TYPE)).append("key: STAIRS_UP_CELL_TYPE: ").append(str(self.STAIRS_UP_CELL_TYPE)))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
# from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.HashtableUtil import HashtableUtil


