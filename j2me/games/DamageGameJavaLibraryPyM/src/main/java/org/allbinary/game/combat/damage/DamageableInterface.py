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
# package org.allbinary.game.combat.damage

from __future__ import annotations

from org.allbinary.layer.NamedInterface import NamedInterface


# Java interface
class DamageableInterface(NamedInterface):
    

    # throws Exception
    def damage(self, damage: int, damageType: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def getDamage(self, damageType: int) -> int:
        raise NotImplementedError()


