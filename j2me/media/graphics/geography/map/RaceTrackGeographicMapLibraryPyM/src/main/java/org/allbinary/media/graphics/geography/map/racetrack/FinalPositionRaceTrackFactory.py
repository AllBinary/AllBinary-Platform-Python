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

import threading


class FinalPositionRaceTrackFactory:
    FIRST_POSITION: int = 1
    index: int = None
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> int:
        with FinalPositionRaceTrackFactory._lock:
            return FinalPositionRaceTrackFactory._getInstance_unlocked()

    @staticmethod
    def _getInstance_unlocked() -> int:
        return ((setattr(FinalPositionRaceTrackFactory, "index", FinalPositionRaceTrackFactory.index + 1) or FinalPositionRaceTrackFactory.index) - 1)
    

    @staticmethod
    def reset() -> None:
        with FinalPositionRaceTrackFactory._lock:
            return FinalPositionRaceTrackFactory._reset_unlocked()

    @staticmethod
    def _reset_unlocked() -> None:
        FinalPositionRaceTrackFactory.index = FinalPositionRaceTrackFactory.FIRST_POSITION


FinalPositionRaceTrackFactory.index = FinalPositionRaceTrackFactory.FIRST_POSITION

