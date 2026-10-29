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

from org.allbinary.game.physics.FrictionProperties import FrictionProperties


class CharacterFrictionProperties(FrictionProperties):

    def _init_fields(self) -> None:
        self.WATER_FRICTION_NOMINATOR: int = None
        self.AIR_FRICTION_NOMINATOR: int = None
        self.COLLISION_FRICTION_NOMINATOR: int = None
    

    def __init__(self, airFriction: int, waterFriction: int, collisionFriction: int) -> None:
        super().__init__()
        self._init_fields()
        self.AIR_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - airFriction
        self.COLLISION_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - collisionFriction
        self.WATER_FRICTION_NOMINATOR = FrictionData.getFrictionDenominator() - waterFriction
    

    def getWATER_FRICTION_NOMINATOR(self) -> int:
        return self.WATER_FRICTION_NOMINATOR
    

    def getAIR_FRICTION_NOMINATOR(self) -> int:
        return self.AIR_FRICTION_NOMINATOR
    

    def getCOLLISION_FRICTION_NOMINATOR(self) -> int:
        return self.COLLISION_FRICTION_NOMINATOR
from org.allbinary.game.physics.friction.FrictionData import FrictionData


