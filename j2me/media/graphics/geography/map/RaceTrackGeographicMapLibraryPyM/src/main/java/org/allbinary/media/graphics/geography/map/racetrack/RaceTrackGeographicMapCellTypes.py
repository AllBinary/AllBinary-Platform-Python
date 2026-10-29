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



class RaceTrackGeographicMapCellTypes:
    instance: RaceTrackGeographicMapCellTypes = None

    def _init_fields(self) -> None:
        self.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.TOP_LEFT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.TOP_RIGHT_TURN_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.VERTICAL_STRAIGHT_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.START_LINE_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
        self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE: RaceTrackGeographicMapCellType = None
    

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
        self._init_fields()
        self.BOTTOM_LEFT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Bottom Left Turn", 1, 1, 0)
        self.BOTTOM_RIGHT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Bottom Right Turn", 2, 1, 0)
        self.TOP_LEFT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Top Left Turn", 3, 1, 0)
        self.TOP_RIGHT_TURN_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Top Right Turne", 4, 1, 0)
        self.HORIZONTAL_STRAIGHT_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Horizontal Straight", 5, 1, 0)
        self.VERTICAL_STRAIGHT_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Vertical Straight", 6, 1, 0)
        self.START_LINE_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Start Line", 7, 1, 0)
        self.DEFAULT_FINISH_LINE_ROAD_CELL_TYPE = RaceTrackGeographicMapCellType("Finish Line", 8, 1, 0)


RaceTrackGeographicMapCellTypes.instance = RaceTrackGeographicMapCellTypes()

