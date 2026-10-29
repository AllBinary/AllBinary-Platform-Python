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
# package org.allbinary.game.combat.weapon

from __future__ import annotations



class SimpleWeaponProperties:

    def _init_fields(self) -> None:
        self.damage: int = 0
        self.dissipation: int = 0
        self.range: int = 0

    def __init__(self) -> None:
        self._init_fields()
    

    def set(self, simpleWeaponProperties: SimpleWeaponProperties) -> None:
        self.setDamage(simpleWeaponProperties.getDamage())
        self.setDissipation(simpleWeaponProperties.getDissipation())
        self.setRange(simpleWeaponProperties.getRange())
    

    def setDamage(self, damage: int) -> None:
        self.damage = damage
    

    def getDamage(self) -> int:
        return self.damage
    

    def setDissipation(self, dissipation: int) -> None:
        self.dissipation = dissipation
    

    def getDissipation(self) -> int:
        return self.dissipation
    

    def getRange(self) -> int:
        return self.range
    

    def setRange(self, range: int) -> None:
        self.range = range


