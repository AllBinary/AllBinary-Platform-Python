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

from java.lang.JavaRuntimeStatic import lazy_static


class AllBinaryThreedTiledLayerFactory:
    instance: AllBinaryThreedTiledLayerFactory = None
    

    @staticmethod
    def getInstance_j0() -> AllBinaryThreedTiledLayerFactory:
        return AllBinaryThreedTiledLayerFactory.instance
    

    # throws Exception
    def getInstance_j2(self, raceTrackInfo: RaceTrackInfo, raceTrackData: RaceTrackData) -> AllBinaryTiledLayer:
        from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackData import RaceTrackData
        from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackInfo import RaceTrackInfo
        raise Exception("No Threed")

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
# from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackData import RaceTrackData
# from org.allbinary.media.graphics.geography.map.racetrack.RaceTrackInfo import RaceTrackInfo


def _AllBinaryThreedTiledLayerFactory_instance() -> object:
    return AllBinaryThreedTiledLayerFactory()

lazy_static(AllBinaryThreedTiledLayerFactory, "instance", _AllBinaryThreedTiledLayerFactory_instance)

