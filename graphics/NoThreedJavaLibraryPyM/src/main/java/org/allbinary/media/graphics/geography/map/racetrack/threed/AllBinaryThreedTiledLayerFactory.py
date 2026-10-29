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
# package org.allbinary.media.graphics.geography.map.racetrack.threed

from __future__ import annotations



class AllBinaryThreedTiledLayerFactory:
    instance: AllBinaryThreedTiledLayerFactory = None
    

    @staticmethod
    def getInstance() -> AllBinaryThreedTiledLayerFactory:
        return AllBinaryThreedTiledLayerFactory.instance
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, raceTrackInfo: RaceTrackInfo, raceTrackData: RaceTrackData) -> AllBinaryTiledLayer:
        raise Exception("No Threed")
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackData import RaceTrackData
from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackInfo import RaceTrackInfo


AllBinaryThreedTiledLayerFactory.instance = AllBinaryThreedTiledLayerFactory()

