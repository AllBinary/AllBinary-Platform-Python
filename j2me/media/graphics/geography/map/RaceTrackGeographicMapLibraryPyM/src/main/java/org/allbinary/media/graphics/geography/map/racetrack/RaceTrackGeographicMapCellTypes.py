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

from java.lang.JavaRuntimeStatic import lazy_static


class RaceTrackGeographicMapCellTypes:
    instance: RaceTrackGeographicMapCellTypes = None

    def _init_fields(self) -> None:
        if "BOTTOM_LEFT_TURN_ROAD_CELL_TYPE" not in vars(self): self.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE" not in vars(self): self.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "TOP_LEFT_TURN_ROAD_CELL_TYPE" not in vars(self): self.TOP_LEFT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "TOP_RIGHT_TURN_ROAD_CELL_TYPE" not in vars(self): self.TOP_RIGHT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE" not in vars(self): self.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "VERTICAL_STRAIGHT_ROAD_CELL_TYPE" not in vars(self): self.VERTICAL_STRAIGHT_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "START_LINE_ROAD_CELL_TYPE" not in vars(self): self.START_LINE_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        if "DEFAULT_FINISH_LINE_ROAD_CELL_TYPE" not in vars(self): self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
    

    @staticmethod
    def getInstance() -> RaceTrackGeographicMapCellTypes:
        return RaceTrackGeographicMapCellTypes.instance
    

    def __init__(self) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellType import RaceTrackGeographicMapCellType
        __class__._init_fields(self)
        self.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Bottom Left Turn", 1, 1, 0)
        self.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Bottom Right Turn", 2, 1, 0)
        self.TOP_LEFT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Top Left Turn", 3, 1, 0)
        self.TOP_RIGHT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Top Right Turne", 4, 1, 0)
        self.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Horizontal Straight", 5, 1, 0)
        self.VERTICAL_STRAIGHT_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Vertical Straight", 6, 1, 0)
        self.START_LINE_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Start Line", 7, 1, 0)
        self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Finish Line", 8, 1, 0)


def _RaceTrackGeographicMapCellTypes_instance() -> object:
    return RaceTrackGeographicMapCellTypes()

lazy_static(RaceTrackGeographicMapCellTypes, "instance", _RaceTrackGeographicMapCellTypes_instance)

