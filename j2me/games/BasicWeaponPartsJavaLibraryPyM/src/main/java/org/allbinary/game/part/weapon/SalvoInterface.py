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
# package org.allbinary.game.part.weapon

from __future__ import annotations



# Java interface
class SalvoInterface:
    

    # throws Exception
    def process(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def processScore(self, allbinaryLayerManager: AllBinaryLayerManager, angle: int, otherAngle: int, weaponProperties: WeaponProperties, scoreableInterface: ScoreableInterface) -> None:
        raise NotImplementedError()
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.score.ScoreableInterface import ScoreableInterface
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager


