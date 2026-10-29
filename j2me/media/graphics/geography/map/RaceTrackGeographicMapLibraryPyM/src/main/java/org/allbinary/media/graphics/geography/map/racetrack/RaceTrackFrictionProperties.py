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



class RaceTrackFrictionProperties:

    def _init_fields(self) -> None:
        self.ROAD_FRICTION_NOMINATOR: int = None
        self.GROUND_FRICTION_NOMINATOR: int = None
    

    def __init__(self, roadFriction: int, groundFriction: int) -> None:
        self._init_fields()
        self.ROAD_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - roadFriction
        self.GROUND_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - groundFriction
    

    def getRoadFrictionNominator(self) -> int:
        return self.ROAD_FRICTION_NOMINATOR
    

    def getGroundFrictionNominator(self) -> int:
        return self.GROUND_FRICTION_NOMINATOR
from org.allbinary.game.physics.friction.FrictionData import FrictionData


