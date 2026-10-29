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

from org.allbinary.media.graphics.geography.map.racetrack.BaseRaceTrackGeographicMap import BaseRaceTrackGeographicMap


class RaceTrackGeographicMap(BaseRaceTrackGeographicMap):

    def _init_fields(self) -> None:
        self.customMapGenerator: CustomMapGeneratorBase = None
    

    def __init__(self, raceTrackInfo: RaceTrackInfo, raceTrackData: RaceTrackData, tiledLayerFactoryInterface: AllBinaryTiledLayerFactoryInterface, geographicMapCellPositionFactoryInterface: GeographicMapCellPositionFactoryInterface, geographicMapCellPositionBaseFactory: GeographicMapCellPositionBaseFactory, geographicMapCellTypeFactory: GeographicMapCellTypeFactory, customMapGeneratorBaseFactory: CustomMapGeneratorBaseFactory) -> None:
        from org.allbinary.media.graphics.geography.map.racetrack.BasicGeographicMapFactory import BasicGeographicMapFactory
        super().__init__(raceTrackInfo, raceTrackData, tiledLayerFactoryInterface.getInstance(raceTrackInfo, raceTrackData), BasicGeographicMapFactory().getInstance(raceTrackInfo, raceTrackData, tiledLayerFactoryInterface, geographicMapCellPositionFactoryInterface, geographicMapCellTypeFactory), geographicMapCellPositionFactoryInterface, geographicMapCellPositionBaseFactory, geographicMapCellTypeFactory)
        self._init_fields()
        self.customMapGenerator = customMapGeneratorBaseFactory.create(self)
    

    def getCustomMapGenerator(self) -> CustomMapGeneratorBase:
        return self.customMapGenerator
    

    # throws Exception
    def isValid(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        customMapArray: list[list[int]] = self.customMapGenerator.getCustomMapArray()
        if geographicMapCellPosition.getColumn() >= len(customMapArray[0]):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Column: ")
            stringBuffer.appendint(int(geographicMapCellPosition.getColumn()))
            stringBuffer.append(" not in: ")
            stringBuffer.appendint(len(customMapArray[0]))
            self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            if geographicMapCellPosition.getColumn() == len(customMapArray[0]):
                return True
            else:
                return False
        elif geographicMapCellPosition.getRow() > len(customMapArray):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Row: ")
            stringBuffer.appendint(int(geographicMapCellPosition.getRow()))
            stringBuffer.append(" not in: ")
            stringBuffer.appendint(len(customMapArray))
            self.logUtil.putF(str(stringBuffer), self, self.commonStrings.IS_VALID)
            if geographicMapCellPosition.getRow() == len(customMapArray):
                return True
            else:
                return False
        return True
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionBaseFactory import GeographicMapCellPositionBaseFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


