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



class Aggression:

    def _init_fields(self) -> None:
        self.ram: int = SmallIntegerSingletonFactory.getInstance().getAt(0)
        self.projectile: int = SmallIntegerSingletonFactory.getInstance().getAt(0)
        self.drops: int = SmallIntegerSingletonFactory.getInstance().getAt(0)
    

    def __init__(self, ram: int, projectile: int, drops: int) -> None:
        self._init_fields()
        self.setRam(ram)
        self.setProjectile(projectile)
        self.setDrops(drops)
    

    def getRam(self) -> int:
        return self.ram
    

    def setRam(self, ram: int) -> None:
        self.ram = ram
    

    def getProjectile(self) -> int:
        return self.projectile
    

    def setProjectile(self, projectile: int) -> None:
        self.projectile = projectile
    

    def getDrops(self) -> int:
        return self.drops
    

    def setDrops(self, drops: int) -> None:
        self.drops = drops
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory


