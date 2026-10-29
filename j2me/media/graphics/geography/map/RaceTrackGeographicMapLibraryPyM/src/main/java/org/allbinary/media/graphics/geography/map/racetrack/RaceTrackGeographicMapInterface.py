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

from org.allbinary.media.graphics.geography.map.GeographicMapInterface import GeographicMapInterface


# Java interface
class RaceTrackGeographicMapInterface(GeographicMapInterface):
    

    def getRaceTrackInfo(self) -> RaceTrackInfo:
        raise NotImplementedError()
    

    def setRaceTrackInfo(self, aRaceTrackInfo: RaceTrackInfo) -> None:
        raise NotImplementedError()
    

    def getRaceTrackData(self) -> RaceTrackData:
        raise NotImplementedError()
    

    def setRaceTrackData(self, raceTrackData: RaceTrackData) -> None:
        raise NotImplementedError()


