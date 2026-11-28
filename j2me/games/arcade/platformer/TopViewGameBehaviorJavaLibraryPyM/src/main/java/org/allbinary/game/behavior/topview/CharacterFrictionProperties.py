# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.behavior.topview

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.physics.FrictionProperties import FrictionProperties


@java_inherited_overloads
class CharacterFrictionProperties(FrictionProperties):
    def _java_defaults(self):
        vars(self).setdefault("WATER_FRICTION_NOMINATOR", 0)
        vars(self).setdefault("AIR_FRICTION_NOMINATOR", 0)
        vars(self).setdefault("COLLISION_FRICTION_NOMINATOR", 0)

    def _init_fields(self) -> None:
        if "WATER_FRICTION_NOMINATOR" not in vars(self): self.WATER_FRICTION_NOMINATOR: int = 0
        if "AIR_FRICTION_NOMINATOR" not in vars(self): self.AIR_FRICTION_NOMINATOR: int = 0
        if "COLLISION_FRICTION_NOMINATOR" not in vars(self): self.COLLISION_FRICTION_NOMINATOR: int = 0
    

    def __init__(self, airFriction: int, waterFriction: int, collisionFriction: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.physics.friction.FrictionData import FrictionData
        super().__init__()
        __class__._init_fields(self)
        self.AIR_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - airFriction
        self.COLLISION_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - collisionFriction
        self.WATER_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - waterFriction
    

    def getWATER_FRICTION_NOMINATOR(self) -> int:
        return self.WATER_FRICTION_NOMINATOR
    

    def getAIR_FRICTION_NOMINATOR(self) -> int:
        return self.AIR_FRICTION_NOMINATOR
    

    def getCOLLISION_FRICTION_NOMINATOR(self) -> int:
        return self.COLLISION_FRICTION_NOMINATOR
# from org.allbinary.game.physics.friction.FrictionData import FrictionData


