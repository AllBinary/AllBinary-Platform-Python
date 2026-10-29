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

from org.allbinary.game.layer.RTSInterface import RTSInterface


class HealthTechnology(RTSInterface):

    def _init_fields(self) -> None:
        self.level: int = 0
        self.maxLevel: int = None
    

    def __init__(self, maxLevel: int) -> None:
        self._init_fields()
        self.maxLevel = maxLevel
    

    def isCompleted(self) -> bool:
        return False
    

    def getPercentComplete(self) -> int:
        return 0
    

    def getLevel(self) -> int:
        return self.level
    

    def getMaxLevel(self) -> int:
        return self.maxLevel
    

    def getCost(self) -> int:
        return 0
    

    def downgrade(self) -> None:
        pass
    

    def getDowngradeCost(self) -> int:
        return 0
    

    def isDowngradeable(self) -> bool:
        return False
    

    def getUpgradeCost(self) -> int:
        return (self.getLevel() * self.getLevel()) * 1000
    

    def isUpgradeable(self) -> bool:
        if self.getLevel() < self.getMaxLevel():
            return True
        else:
            return False
    

    def upgrade(self) -> None:
        from org.allbinary.game.rts.technology.UnitTechnologySingletonFactory import UnitTechnologySingletonFactory
        self.level += 1
        unitTechnologySingletonFactory: UnitTechnologySingletonFactory = UnitTechnologySingletonFactory.getInstance()
        unitTechnologySingletonFactory.setHealth(unitTechnologySingletonFactory.getHealth() + (self.getLevel() * 100))
    

    def isSelfUpgradeable(self) -> bool:
        return False


