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

from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackGeographicMapInterfaceFactoryInterface import RaceTrackGeographicMapInterfaceFactoryInterface


# Java interface
class MultiLevelRaceTrackGeographicMapInterfaceFactoryInterface(RaceTrackGeographicMapInterfaceFactoryInterface):
    

    # throws Exception
    def getFirstWaveWithTrack(self, track: int) -> int:
        raise NotImplementedError()
    

    def getTotalTracks(self) -> int:
        raise NotImplementedError()
    

    def getTotalLevels(self) -> int:
        raise NotImplementedError()


