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
# package org.allbinary.game.rts.technology

from __future__ import annotations



class UnitTechnologySingletonFactory:
    instance: UnitTechnologySingletonFactory = None

    def _init_fields(self) -> None:
        self.damage: int = 0
        self.health: int = 0
        self.reload: int = 0
        self.repair: int = 0
        self.speed: int = 0
    

    @staticmethod
    def getInstance() -> UnitTechnologySingletonFactory:
        return UnitTechnologySingletonFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self) -> None:
        self.setDamage(0)
        self.setHealth(0)
        self.setReload(0)
        self.setRepair(0)
        self.setSpeed(0)
    

    def getDamage(self) -> int:
        return self.damage
    

    def setDamage(self, damage: int) -> None:
        self.damage = damage
    

    def getHealth(self) -> int:
        return self.health
    

    def setHealth(self, health: int) -> None:
        self.health = health
    

    def getReload(self) -> int:
        return self.reload
    

    def setReload(self, reload: int) -> None:
        self.reload = reload
    

    def getRepair(self) -> int:
        return self.repair
    

    def setRepair(self, repair: int) -> None:
        self.repair = repair
    

    def getSpeed(self) -> int:
        return self.speed
    

    def setSpeed(self, speed: int) -> None:
        self.speed = speed


UnitTechnologySingletonFactory.instance = UnitTechnologySingletonFactory()

