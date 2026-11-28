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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


@java_inherited_overloads
class RaceTrackGeographicMapCellTypeFactory(GeographicMapCellTypeFactory):
    instanceC: RaceTrackGeographicMapCellTypeFactory = None
    def _java_defaults(self):
        vars(self).setdefault("EMPTY_CELL_TYPE", None)
        vars(self).setdefault("EASY_CELL_TYPE", None)
        vars(self).setdefault("BOTTOM_LEFT_TURN_ROAD_CELL_TYPE", None)
        vars(self).setdefault("BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE", None)
        vars(self).setdefault("TOP_LEFT_TURN_ROAD_CELL_TYPE", None)
        vars(self).setdefault("TOP_RIGHT_TURN_ROAD_CELL_TYPE", None)
        vars(self).setdefault("HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE", None)
        vars(self).setdefault("VERTICAL_STRAIGHT_ROAD_CELL_TYPE", None)
        vars(self).setdefault("START_LINE_ROAD_CELL_TYPE", None)
        vars(self).setdefault("DEFAULT_FINISH_LINE_ROAD_CELL_TYPE", None)
        vars(self).setdefault("FINISH_LINE_ROAD_CELL_TYPE", None)

    def _init_fields(self) -> None:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        self.EMPTY_CELL_TYPE: GeographicMapCellType = GeographicMapCellType(0, -1)
        self.EASY_CELL_TYPE: GeographicMapCellType = self.EMPTY_CELL_TYPE
        if "BOTTOM_LEFT_TURN_ROAD_CELL_TYPE" not in vars(self): self.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE" not in vars(self): self.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "TOP_LEFT_TURN_ROAD_CELL_TYPE" not in vars(self): self.TOP_LEFT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "TOP_RIGHT_TURN_ROAD_CELL_TYPE" not in vars(self): self.TOP_RIGHT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE" not in vars(self): self.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "VERTICAL_STRAIGHT_ROAD_CELL_TYPE" not in vars(self): self.VERTICAL_STRAIGHT_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "START_LINE_ROAD_CELL_TYPE" not in vars(self): self.START_LINE_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "DEFAULT_FINISH_LINE_ROAD_CELL_TYPE" not in vars(self): self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.FINISH_LINE_ROAD_CELL_TYPE: GeographicMapCellType = GeographicMapCellType.NULL_GEOGRAPHIC_MAP_CELL_TYPE
    

    @staticmethod
    def getInstance() -> RaceTrackGeographicMapCellTypeFactory:
        return RaceTrackGeographicMapCellTypeFactory.instanceC
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypes import RaceTrackGeographicMapCellTypes
        super().__init__()
        __class__._init_fields(self)
        raceTrackGeographicMapCellTypes: RaceTrackGeographicMapCellTypes = RaceTrackGeographicMapCellTypes.getInstance()
        self.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE
        self.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE
        self.TOP_LEFT_TURN_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.TOP_LEFT_TURN_ROAD_CELL_TYPE
        self.TOP_RIGHT_TURN_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.TOP_RIGHT_TURN_ROAD_CELL_TYPE
        self.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE
        self.VERTICAL_STRAIGHT_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.VERTICAL_STRAIGHT_ROAD_CELL_TYPE
        self.START_LINE_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.START_LINE_ROAD_CELL_TYPE
        self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE = raceTrackGeographicMapCellTypes.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE
    

    def getStartType(self) -> int:
        return self.START_LINE_ROAD_CELL_TYPE.getType()
    

    def getEndType(self) -> int:
        return self.FINISH_LINE_ROAD_CELL_TYPE.getType()
    

    def getEmptyType(self) -> int:
        return self.EMPTY_CELL_TYPE.getType()
    

    def isPath(self, cellType: GeographicMapCellType) -> bool:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType
        if cellType != self.EMPTY_CELL_TYPE and cellType != self.EASY_CELL_TYPE:
            return True
        return False
# from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


def _RaceTrackGeographicMapCellTypeFactory_instanceC() -> object:
    return RaceTrackGeographicMapCellTypeFactory()

lazy_static(RaceTrackGeographicMapCellTypeFactory, "instanceC", _RaceTrackGeographicMapCellTypeFactory_instanceC)

