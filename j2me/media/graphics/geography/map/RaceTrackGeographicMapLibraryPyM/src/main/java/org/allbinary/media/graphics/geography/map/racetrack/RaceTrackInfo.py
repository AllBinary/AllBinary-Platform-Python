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



class RaceTrackInfo:

    def _init_fields(self) -> None:
        if "id" not in vars(self): self.id: int = None
        if "name" not in vars(self): self.name: str = None
        if "raceTrackFrictionProperties" not in vars(self): self.raceTrackFrictionProperties: RaceTrackFrictionProperties = None
        if "foregroundBasicColor" not in vars(self): self.foregroundBasicColor: BasicColor = None
        if "backgroundBasicColor" not in vars(self): self.backgroundBasicColor: BasicColor = None
        if "qualifyTime" not in vars(self): self.qualifyTime: int = 0
        if "worstContinuePosition" not in vars(self): self.worstContinuePosition: int = 0
        if "totalLaps" not in vars(self): self.totalLaps: int = 0
    

    def __init__(self, id: int, name: str, raceTrackFrictionProperties: RaceTrackFrictionProperties, foregroundBasicColor: BasicColor, backgroundBasicColor: BasicColor, qualifyTime: int, worstContinuePosition: int, totalLaps: int) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        __class__._init_fields(self)
        self.id = id
        self.name = name
        self.raceTrackFrictionProperties = raceTrackFrictionProperties
        self.backgroundBasicColor = backgroundBasicColor
        self.foregroundBasicColor = foregroundBasicColor
        self.qualifyTime = qualifyTime
        self.worstContinuePosition = worstContinuePosition
        self.totalLaps = totalLaps
    

    def getId(self) -> int:
        return self.id
    

    def setId(self, id: int) -> None:
        self.id = id
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getQualifyTime(self) -> int:
        return self.qualifyTime
    

    def setQualifyTime(self, qualifyTime: int) -> None:
        self.qualifyTime = qualifyTime
    

    def getWorstContinuePosition(self) -> int:
        return self.worstContinuePosition
    

    def setWorstContinuePosition(self, worstContinuePosition: int) -> None:
        self.worstContinuePosition = worstContinuePosition
    

    def getTotalLaps(self) -> int:
        return self.totalLaps
    

    def setTotalLaps(self, totalLaps: int) -> None:
        self.totalLaps = totalLaps
    

    def getForegroundBasicColor(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return self.foregroundBasicColor
    

    def setForegroundBasicColor(self, foregroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.foregroundBasicColor = foregroundBasicColor
    

    def getBackgroundBasicColor(self) -> BasicColor:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        return self.backgroundBasicColor
    

    def setBackgroundBasicColor(self, backgroundBasicColor: BasicColor) -> None:
        from org.allbinary.graphics.color.BasicColor import BasicColor
        self.backgroundBasicColor = backgroundBasicColor
    

    def getRaceTrackFrictionProperties(self) -> RaceTrackFrictionProperties:
        return self.raceTrackFrictionProperties
    

    def setRaceTrackFrictionProperties(self, raceTrackFrictionProperties: RaceTrackFrictionProperties) -> None:
        self.raceTrackFrictionProperties = raceTrackFrictionProperties
# from org.allbinary.graphics.color.BasicColor import BasicColor


