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



class TiledLayerFactory:
    

    def getInstance(self, raceTrackData: RaceTrackData) -> TiledLayer:
        mapArray: list[list[int]] = raceTrackData.getMapArray()
        return TiledLayer(len(mapArray[0]), len(mapArray), raceTrackData.getTileSetImage(), raceTrackData.getCellWidth(), raceTrackData.getCellHeight())
    

    def getMiniInstance(self, raceTrackData: RaceTrackData) -> TiledLayer:
        mapArray: list[list[int]] = raceTrackData.getMapArray()
        return TiledLayer(len(mapArray[0]), len(mapArray), raceTrackData.getMiniTileSetImage(), raceTrackData.getMiniCellWidth(), raceTrackData.getMiniCellHeight())
# from javax.microedition.lcdui.game.TiledLayer import TiledLayer


