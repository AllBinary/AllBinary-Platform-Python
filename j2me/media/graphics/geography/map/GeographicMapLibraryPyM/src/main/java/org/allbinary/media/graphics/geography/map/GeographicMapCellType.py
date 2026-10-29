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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations



class GeographicMapCellType:
    NULL_GEOGRAPHIC_MAP_CELL_TYPE_ARRAY: list[GeographicMapCellType] = None
    NULL_GEOGRAPHIC_MAP_CELL_TYPE: GeographicMapCellType = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.type_: int = None
    

    def __init__(self, type_: int, reset: int) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
        self._init_fields()
        self.type_ = type_
        if type_ != -2147483648:
            geographicMapCellTypeFactory: GeographicMapCellTypeFactory = GeographicMapCellTypeFactory.getInstance()
            geographicMapCellTypeArray: list[GeographicMapCellType] = geographicMapCellTypeFactory.getGeographicMapCellTypeArray()
            if geographicMapCellTypeArray[type_] is None or reset == 1:
                geographicMapCellTypeArray[type_] = self
            else:
                if reset != -1:
                    raise RuntimeError()
    

    def getType(self) -> int:
        return self.type_
    

    def toString(self) -> str:
        return str(SmallIntegerSingletonFactory.getInstance().getAt(self.type_))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE_ARRAY = [None] * (0)

GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE = GeographicMapCellType(-2147483648, 0)

