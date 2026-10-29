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
# package org.allbinary.game.health

from __future__ import annotations

from org.allbinary.game.health.HealthInterface import HealthInterface


class Health(HealthInterface):
    NULL_HEALTH: Health = None
    NAME: str = "Health Resource"
    HEALTH_LABEL: str = "Health: "
    MAX_HEALTH_LABEL: str = " Max: "

    def _init_fields(self) -> None:
        self.health: int = 0
        self.maxHealth: int = 0
        self.healthListenerInterface: HealthListenerInterface = NullHealthListener.NULL_HEALTH_LISTENER
    

    def __init__(self, maxHealth: int) -> None:
        self._init_fields()
        self.setMaxHealth(maxHealth)
        self.setHealth(maxHealth)
    

    def heal(self, ahealth: int) -> None:
        newHealth: int = self.getHealth() + ahealth
        if newHealth > self.getMaxHealth():
            self.setHealth(self.getMaxHealth())
        else:
            self.setHealth(newHealth)
    

    def healMax(self) -> None:
        self.setHealth(self.getMaxHealth())
    

    def isDamaged(self) -> bool:
        if self.getHealth() != self.getMaxHealth():
            return True
        else:
            return False
    

    def damage(self, ahealth: int) -> None:
        if ahealth < 0:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("******* Trying to heal when damaging. Damage: ")
            stringBuffer.appendint(ahealth)
            stringBuffer.append(CommonSeps.getInstance().SPACE)
            stringBuffer.append(str(self))
            ForcedLogUtil.log(str(stringBuffer), self)
            return
        health: int = self.getHealth() - ahealth
        self.setHealth(health)
    

    def isAlive(self) -> bool:
        if self.getHealth() <= 0:
            return False
        else:
            return True
    

    def getMaxHealth(self) -> int:
        return self.maxHealth
    

    def setMaxHealth(self, maxHealth: int) -> None:
        self.maxHealth = maxHealth
    

    def setHealth(self, health: int) -> None:
        if health > self.getMaxHealth():
            self.health = self.getMaxHealth()
        elif health < 0:
            self.health = 0
        else:
            self.health = health
        if self.healthListenerInterface is not None:
            self.healthListenerInterface.onHealthChange()
    

    def getHealth(self) -> int:
        return self.health
    

    def addListener(self, healthGraphic: HealthListenerInterface) -> None:
        self.healthListenerInterface = healthGraphic
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(Health.HEALTH_LABEL)
        stringBuffer.appendint(self.health)
        stringBuffer.append(Health.MAX_HEALTH_LABEL)
        stringBuffer.appendint(self.maxHealth)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.game.health.NullHealthListener import NullHealthListener


Health.NULL_HEALTH = Health(0)

