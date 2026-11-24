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


class RaceTrackRoadsGeographicMapCellHistoryFactory:
    geographicMapCellHistory: GeographicMapCellHistory = None
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> GeographicMapCellHistory:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        return RaceTrackRoadsGeographicMapCellHistoryFactory.geographicMapCellHistory
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory


def _RaceTrackRoadsGeographicMapCellHistoryFactory_geographicMapCellHistory() -> object:
    from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
    return GeographicMapCellHistory()

lazy_static(RaceTrackRoadsGeographicMapCellHistoryFactory, "geographicMapCellHistory", _RaceTrackRoadsGeographicMapCellHistoryFactory_geographicMapCellHistory)

