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
        if "ROAD_FRICTION_NOMINATOR" not in vars(self): self.ROAD_FRICTION_NOMINATOR: int = 0
        if "GROUND_FRICTION_NOMINATOR" not in vars(self): self.GROUND_FRICTION_NOMINATOR: int = 0
    

    def __init__(self, roadFriction: int, groundFriction: int) -> None:
        from org.allbinary.game.physics.friction.FrictionData import FrictionData
        __class__._init_fields(self)
        self.ROAD_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - roadFriction
        self.GROUND_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - groundFriction
    

    def getRoadFrictionNominator(self) -> int:
        return self.ROAD_FRICTION_NOMINATOR
    

    def getGroundFrictionNominator(self) -> int:
        return self.GROUND_FRICTION_NOMINATOR
# from org.allbinary.game.physics.friction.FrictionData import FrictionData


