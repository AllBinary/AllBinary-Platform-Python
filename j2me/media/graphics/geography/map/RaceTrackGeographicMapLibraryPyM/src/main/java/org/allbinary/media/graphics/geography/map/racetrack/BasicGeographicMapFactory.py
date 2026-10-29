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



class BasicGeographicMapFactory:
    

    # throws Exception
    def getInstance(self, raceTrackInfo: RaceTrackInfo, raceTrackData: RaceTrackData, tiledLayerFactoryInterface: AllBinaryTiledLayerFactoryInterface, geographicMapCellPositionFactoryInterface: GeographicMapCellPositionFactoryInterface, geographicMapCellTypeFactory: GeographicMapCellTypeFactory) -> BasicGeographicMap:
        return BasicGeographicMap(SmallIntegerSingletonFactory.getInstance().getAt(int(raceTrackInfo.getId()) + 100 + 1), raceTrackInfo.getName(), raceTrackData.getCellTypeIdToGeographicMapCellTypeArray(), tiledLayerFactoryInterface.getMiniInstance(raceTrackData), BasicColorFactory.getInstance().CLEAR_COLOR, BasicColorFactory.getInstance().CLEAR_COLOR, geographicMapCellPositionFactoryInterface, GeographicMapCellPositionBaseFactory(), geographicMapCellTypeFactory)
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionBaseFactory import GeographicMapCellPositionBaseFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionFactoryInterface import GeographicMapCellPositionFactoryInterface
from org.allbinary.media.graphics.geography.map.GeographicMapCellTypeFactory import GeographicMapCellTypeFactory


