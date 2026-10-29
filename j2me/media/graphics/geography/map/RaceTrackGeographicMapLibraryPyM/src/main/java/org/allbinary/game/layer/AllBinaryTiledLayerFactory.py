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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.racetrack.AllBinaryTiledLayerFactoryInterface import AllBinaryTiledLayerFactoryInterface


class AllBinaryTiledLayerFactory(AllBinaryTiledLayerFactoryInterface):
    

    # throws Exception
    def getInstance(self, raceTrackInfo: RaceTrackInfo, raceTrackData: RaceTrackData) -> AllBinaryTiledLayer:
        from org.allbinary.game.layer.AllBinaryJ2METiledLayer import AllBinaryJ2METiledLayer
        allbinaryTiledLayer: AllBinaryTiledLayer = None
        tiledLayer: TiledLayer = TiledLayerFactory().getInstance(raceTrackData)
        allbinaryTiledLayer = AllBinaryJ2METiledLayer(raceTrackData.getId(), tiledLayer, raceTrackData.getMapArray(), int(BasicColorFactory.getInstance().RED))
        allbinaryTiledLayer.setCells(raceTrackData.getMapArray())
        return allbinaryTiledLayer
    

    # throws Exception
    def getMiniInstance(self, raceTrackData: RaceTrackData) -> AllBinaryTiledLayer:
        from org.allbinary.game.layer.AllBinaryJ2METiledLayer import AllBinaryJ2METiledLayer
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        tiledLayer: TiledLayer = TiledLayerFactory().getMiniInstance(raceTrackData)
        allbinaryTiledLayer: AllBinaryTiledLayer = AllBinaryJ2METiledLayer(smallIntegerSingletonFactory.getAt(int(raceTrackData.getId()) + 100 + 1), tiledLayer, raceTrackData.getMapArray(), int(BasicColorFactory.getInstance().RED))
        allbinaryTiledLayer.setCells(raceTrackData.getMapArray())
        return allbinaryTiledLayer
# from javax.microedition.lcdui.game.TiledLayer import TiledLayer
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackData import RaceTrackData
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackInfo import RaceTrackInfo
from org.allbinary.media.graphics.geography.map.racetrack.TiledLayerFactory import TiledLayerFactory


