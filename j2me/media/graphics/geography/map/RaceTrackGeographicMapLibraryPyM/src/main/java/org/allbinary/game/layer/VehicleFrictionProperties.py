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

from org.allbinary.game.physics.FrictionProperties import FrictionProperties


class VehicleFrictionProperties(FrictionProperties):

    def _init_fields(self) -> None:
        self.TIRE_FRICTION_NOMINATOR: int = None
        self.BRAKE_FRICTION_NOMINATOR: int = None
        self.AIR_FRICTION_NOMINATOR: int = None
        self.CRASH_FRICTION_NOMINATOR: int = None
    

    def __init__(self, tireFriction: int, brakeFriction: int, airFriction: int, crashFriction: int) -> None:
        super().__init__()
        self._init_fields()
        self.TIRE_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - tireFriction
        self.BRAKE_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - brakeFriction
        self.AIR_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - airFriction
        self.CRASH_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - crashFriction
    

    def getTireFrictionNominator(self) -> int:
        return self.TIRE_FRICTION_NOMINATOR
    

    def getBrakeFrictionNominator(self) -> int:
        return self.BRAKE_FRICTION_NOMINATOR
    

    def getAirFrictionNominator(self) -> int:
        return self.AIR_FRICTION_NOMINATOR
    

    def getCrashFrictionNominator(self) -> int:
        return self.CRASH_FRICTION_NOMINATOR
from org.allbinary.game.physics.friction.FrictionData import FrictionData


