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

from org.allbinary.game.configuration.feature.GameFeature import GameFeature


class RaceTrackGameFeature(GameFeature):
    MINI_MAP: GameFeature = None
    AUTO_FINISH_AI: GameFeature = None
    

    def __init__(self, name: str) -> None:
        super().__init__(name)


RaceTrackGameFeature.MINI_MAP = RaceTrackGameFeature("Mini Map")

RaceTrackGameFeature.AUTO_FINISH_AI = RaceTrackGameFeature("Auto Finish AI")

