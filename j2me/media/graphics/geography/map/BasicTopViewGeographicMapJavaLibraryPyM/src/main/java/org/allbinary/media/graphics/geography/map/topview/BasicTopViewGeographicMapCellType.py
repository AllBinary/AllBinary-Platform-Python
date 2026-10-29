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
# package org.allbinary.media.graphics.geography.map.topview

from __future__ import annotations



class BasicTopViewGeographicMapCellType:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = None
        self.cost: int = None
        self.types: list[int] = None
    

    @staticmethod
    def createType(name: str, type_: int, cost: int) -> BasicTopViewGeographicMapCellType:
        types: BasicArrayList = BasicArrayListS(1)
        types.add(type_)
        return BasicTopViewGeographicMapCellType(name, types, cost)
    

    def __init__(self, name: str, types: BasicArrayList, cost: int) -> None:
        self._init_fields()
        size: int = types.size()
        typeArray: list[int] = [0] * (size)
        typeAsInteger: int = None
        type_: int = 0
        for index in range(0, size):
            typeAsInteger = (types.get(index))
            type_ = int(typeAsInteger)
            if GeographicMapCellTypeFactory.getInstance().getGeographicMapCellTypeArray()[type_] is None:
                RaceTrackGeographicMapCellType(name, type_, cost, 0)
            else:
                pass
            typeArray[index] = type_
        self.name = name
        self.cost = cost
        self.types = typeArray
    

    def isType(self, type_: GeographicMapCellType) -> bool:
        return self.hasType(type_.getType())
    

    def hasType(self, type_: int) -> bool:
        size: int = len(self.types)
        for index in range(0, size):
            if self.types[index] == type_:
                return True
        return False
    

    def getTypes(self) -> list[int]:
        return self.types
    

    def toString(self) -> str:
        stringMaker: StringMaker = StringMaker()
        size: int = len(self.types)
        for index in range(0, size):
            stringMaker.appendint(self.types[index]).append(CommonSeps.getInstance().COMMA)
        return str(stringMaker)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListS import BasicArrayListS


