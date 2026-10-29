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
# package org.allbinary.media.graphics.geography.map.racetrack

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


class RaceTrackGeographicMapCellType(GeographicMapCellType):

    def _init_fields(self) -> None:
        self.name: str = None
        self.travelCost: int = None
    

    def __init__(self, name: str, type_: int, travelCost: int, reset: int) -> None:
        super().__init__(type_, reset)
        self._init_fields()
        self.name = name
        self.travelCost = travelCost
    

    def getTravelCost(self) -> int:
        return self.travelCost
from org.allbinary.string.CommonStrings import CommonStrings


