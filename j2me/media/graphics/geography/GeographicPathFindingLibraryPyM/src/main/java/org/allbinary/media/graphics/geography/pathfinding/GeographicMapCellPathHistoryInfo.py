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
# package org.allbinary.media.graphics.geography.pathfinding

from __future__ import annotations



class GeographicMapCellPathHistoryInfo:

    def _init_fields(self) -> None:
        self.previousGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.previousOnPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.nextUnvisitedOnPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.nextOnPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.nextChosenOnPathGeographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION

    def __init__(self) -> None:
        self._init_fields()
    

    def getPreviousGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.previousGeographicMapCellPosition
    

    def setPreviousGeographicMapCellPosition(self, previousGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.previousGeographicMapCellPosition = previousGeographicMapCellPosition
    

    def getPreviousOnPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.previousOnPathGeographicMapCellPosition
    

    def setPreviousOnPathGeographicMapCellPosition(self, previousOnPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.previousOnPathGeographicMapCellPosition = previousOnPathGeographicMapCellPosition
    

    def getNextUnvisitedOnPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.nextUnvisitedOnPathGeographicMapCellPosition
    

    def setNextUnvisitedOnPathGeographicMapCellPosition(self, nextUnvisitedOnPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.nextUnvisitedOnPathGeographicMapCellPosition = nextUnvisitedOnPathGeographicMapCellPosition
    

    def getNextOnPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.nextOnPathGeographicMapCellPosition
    

    def setNextOnPathGeographicMapCellPosition(self, nextOnPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.nextOnPathGeographicMapCellPosition = nextOnPathGeographicMapCellPosition
    

    def getNextChosenOnPathGeographicMapCellPosition(self) -> GeographicMapCellPosition:
        return self.nextChosenOnPathGeographicMapCellPosition
    

    def setNextChosenOnPathGeographicMapCellPosition(self, nextChosenOnPathGeographicMapCellPosition: GeographicMapCellPosition) -> None:
        self.nextChosenOnPathGeographicMapCellPosition = nextChosenOnPathGeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory


