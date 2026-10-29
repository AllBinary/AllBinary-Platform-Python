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

from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapCellTypeFactory import RaceTrackGeographicMapCellTypeFactory


class CloseLoopRaceTrackGeographicMapCellTypeFactory(RaceTrackGeographicMapCellTypeFactory):
    instanceC: CloseLoopRaceTrackGeographicMapCellTypeFactory = None
    

    @staticmethod
    def getInstance() -> CloseLoopRaceTrackGeographicMapCellTypeFactory:
        return CloseLoopRaceTrackGeographicMapCellTypeFactory.instanceC
    

    def __init__(self) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.EmptyRaceRaceTrackGeographicMapCellTypeFactory import EmptyRaceRaceTrackGeographicMapCellTypeFactory
        super().__init__()
        self.EMPTY_CELL_TYPE = EmptyRaceRaceTrackGeographicMapCellTypeFactory.getInstance().EMPTY_CELL_TYPE
        self.EASY_CELL_TYPE = self.EMPTY_CELL_TYPE
        self.FINISH_LINE_ROAD_CELL_TYPE = self.START_LINE_ROAD_CELL_TYPE


CloseLoopRaceTrackGeographicMapCellTypeFactory.instanceC = CloseLoopRaceTrackGeographicMapCellTypeFactory()

