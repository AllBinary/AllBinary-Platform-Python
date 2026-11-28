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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.physics.FrictionProperties import FrictionProperties


@java_inherited_overloads
class VehicleFrictionProperties(FrictionProperties):
    def _java_defaults(self):
        vars(self).setdefault("TIRE_FRICTION_NOMINATOR", 0)
        vars(self).setdefault("BRAKE_FRICTION_NOMINATOR", 0)
        vars(self).setdefault("AIR_FRICTION_NOMINATOR", 0)
        vars(self).setdefault("CRASH_FRICTION_NOMINATOR", 0)

    def _init_fields(self) -> None:
        if "TIRE_FRICTION_NOMINATOR" not in vars(self): self.TIRE_FRICTION_NOMINATOR: int = 0
        if "BRAKE_FRICTION_NOMINATOR" not in vars(self): self.BRAKE_FRICTION_NOMINATOR: int = 0
        if "AIR_FRICTION_NOMINATOR" not in vars(self): self.AIR_FRICTION_NOMINATOR: int = 0
        if "CRASH_FRICTION_NOMINATOR" not in vars(self): self.CRASH_FRICTION_NOMINATOR: int = 0
    

    def __init__(self, tireFriction: int, brakeFriction: int, airFriction: int, crashFriction: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.physics.friction.FrictionData import FrictionData
        super().__init__()
        __class__._init_fields(self)
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
# from org.allbinary.game.physics.friction.FrictionData import FrictionData


