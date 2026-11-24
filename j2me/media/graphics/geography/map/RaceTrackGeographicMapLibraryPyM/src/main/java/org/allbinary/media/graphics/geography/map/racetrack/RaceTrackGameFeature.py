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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.configuration.feature.GameFeature import GameFeature


class RaceTrackGameFeature(GameFeature):
    MINI_MAP: GameFeature = None
    AUTO_FINISH_AI: GameFeature = None
    

    def __init__(self, name: str) -> None:
        super().__init__(name)


def _RaceTrackGameFeature_MINI_MAP() -> object:
    return RaceTrackGameFeature("Mini Map")

lazy_static(RaceTrackGameFeature, "MINI_MAP", _RaceTrackGameFeature_MINI_MAP)

def _RaceTrackGameFeature_AUTO_FINISH_AI() -> object:
    return RaceTrackGameFeature("Auto Finish AI")

lazy_static(RaceTrackGameFeature, "AUTO_FINISH_AI", _RaceTrackGameFeature_AUTO_FINISH_AI)

