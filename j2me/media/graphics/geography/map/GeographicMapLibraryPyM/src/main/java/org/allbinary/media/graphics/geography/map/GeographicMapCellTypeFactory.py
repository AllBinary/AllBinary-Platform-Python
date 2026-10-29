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



class GeographicMapCellTypeFactory:
    instance: GeographicMapCellTypeFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.geographicMapCellTypeArray: list[GeographicMapCellType] = [None] * (512)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GeographicMapCellTypeFactory:
        return GeographicMapCellTypeFactory.instance
    

    def get(self, type_: int) -> GeographicMapCellType:
        return self.geographicMapCellTypeArray[type_]
    

    def getGeographicMapCellTypeArray(self) -> list[GeographicMapCellType]:
        return self.geographicMapCellTypeArray
    

    def getStartType(self) -> int:
        raise RuntimeError()
    

    def getEndType(self) -> int:
        raise RuntimeError()
    

    def getEmptyType(self) -> int:
        raise RuntimeError()
    

    def isPath(self, cellType: GeographicMapCellType) -> bool:
        raise RuntimeError()
from org.allbinary.logic.communication.log.LogUtil import LogUtil


GeographicMapCellTypeFactory.instance = GeographicMapCellTypeFactory()

