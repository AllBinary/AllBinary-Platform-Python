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

from org.allbinary.media.graphics.geography.map.GeographicMapCellHistoryProgressBase import GeographicMapCellHistoryProgressBase


class GeographicMapCellHistoryProgress(GeographicMapCellHistoryProgressBase):

    def _init_fields(self) -> None:
        self.totalVisitedArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
        self.geographicMapCellHistoryArray: list[GeographicMapCellHistory] = GeographicMapCellHistory.NULL_GEOGRPAHIC_MAP_HISTORY_ARRAY
    

    def __init__(self, geographicMapCellHistoryArray: list[GeographicMapCellHistory]) -> None:
        super().__init__()
        self._init_fields()
        self.geographicMapCellHistoryArray = geographicMapCellHistoryArray
        self.init()
    

    def init(self) -> None:
        self.totalVisitedArray = [0] * (len(self.geographicMapCellHistoryArray))
    

    def isAnyProgress(self) -> bool:
        isProgressing: bool = False
        size: int = len(self.geographicMapCellHistoryArray)
        currentTotalVisited: int = 0
        totalVisited: int = 0
        for index in range(0, size):
            totalVisited = self.geographicMapCellHistoryArray[index].getTotalVisited()
            currentTotalVisited = self.totalVisitedArray[index]
            if currentTotalVisited < totalVisited:
                isProgressing = True
                self.totalVisitedArray[index] = totalVisited
        return isProgressing
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory


