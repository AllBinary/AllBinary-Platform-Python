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
# package org.allbinary.media.graphics.geography.map.platform

from __future__ import annotations



class BasicPlatormGeographicMapCellType:

    def _init_fields(self) -> None:
        self.types: list[int] = None
    

    @staticmethod
    def createType(type_: int) -> BasicPlatormGeographicMapCellType:
        types: BasicArrayList = BasicArrayListS(1)
        types.add(SmallIntegerSingletonFactory.getInstance().getAt(type_))
        basicPlatormGeographicMapCellType: BasicPlatormGeographicMapCellType = BasicPlatormGeographicMapCellType(types)
        return basicPlatormGeographicMapCellType
    

    def __init__(self, types: BasicArrayList) -> None:
        self._init_fields()
        size: int = types.size()
        typeArray: list[int] = [0] * (size)
        typeAsInteger: int = None
        type_: int = 0
        for index in range(0, size):
            typeAsInteger = (types.get(index))
            type_ = int(typeAsInteger)
            GeographicMapCellType(type_, 0)
            typeArray[index] = type_
        self.types = typeArray
    

    def isType(self, type_: GeographicMapCellType) -> bool:
        return self.hasType(type_.getType())
    

    def hasType(self, type_: int) -> bool:
        size: int = len(self.types)
        for index in range(0, size):
            if self.types[index] == type_:
                return True
        return False
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListS import BasicArrayListS


