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

from org.allbinary.game.combat.weapon.SimpleWeaponProperties import SimpleWeaponProperties


class WeaponProperties(SimpleWeaponProperties):
    NULL_WEAPON_PROPERTIES: WeaponProperties = None
    messageSent: bool = False
    DAMAGE: str = "Damage: "
    RANGE: str = "Range: "
    RELOAD: str = "Reload: "

    def _init_fields(self) -> None:
        self.reloadTime: int = 0
        self.targetingTime: int = 0
        self.speed: BasicDecimal = BasicDecimal.ZERO_BIGDECIMAL
        self.MAX: int = 10240
        self.ZERO: int = 0
    

    def __init__(self, reloadTime: int, targetingTime: int, speed: int, damage: int, dissipation: int) -> None:
        super().__init__()
        self._init_fields()
        if speed < self.MAX and speed != 0 and not WeaponProperties.messageSent:
            MESSAGE: str = "Danger Danger Danger: Speed probably to slow if using 1 degree calculations as velocity for a single axis could be below 1024: "
            commonStrings: CommonStrings = CommonStrings.getInstance()
            PreLogUtil.put(str(StringMaker().append(MESSAGE).appendlong(speed)), self, commonStrings.CONSTRUCTOR)
            WeaponProperties.messageSent = True
        self.setReloadTime(reloadTime)
        self.setTargetingTime(targetingTime)
        self.setDamage(damage)
        self.setDissipation(dissipation)
        self.setSpeed(BasicDecimal(speed))
        if dissipation != self.ZERO:
            unscaledDamage: int = self.speed.getUnscaled() * damage
            scaledDissipation: int = dissipation * self.speed.getScaledFactorValue()
            value: int = (int(unscaledDamage / scaledDissipation))
            self.setRange(int((value * 9) / 10))
    

    def setReloadTime(self, reloadTime: int) -> None:
        self.reloadTime = reloadTime
    

    def getReloadTime(self) -> int:
        return self.reloadTime
    

    def setTargetingTime(self, targetingTime: int) -> None:
        self.targetingTime = targetingTime
    

    def getTargetingTime(self) -> int:
        return self.targetingTime
    

    def getSpeed(self) -> BasicDecimal:
        return self.speed
    

    def setSpeed(self, speed: BasicDecimal) -> None:
        self.speed = speed
    

    def getDamageI(self, range: int) -> int:
        return self.getDamage() - ((self.getDissipation() * range) / self.speed.getScaled())
    

    def toStringArray(self) -> list[str]:
        index: int = 0
        stringArray: list[str] = [None] * (3)
        stringBuffer: StringMaker = StringMaker()
        stringArray[((index := index + 1) - 1)] = str(stringBuffer.append(WeaponProperties.DAMAGE).appendint(int(self.getDamage())))
        stringBuffer.delete(0, stringBuffer.length())
        stringArray[((index := index + 1) - 1)] = str(stringBuffer.append(WeaponProperties.RANGE).appendint(int(self.getRange())))
        stringBuffer.delete(0, stringBuffer.length())
        stringArray[((index := index + 1) - 1)] = str(stringBuffer.append(WeaponProperties.RELOAD).appendlong(self.getReloadTime()))
        return stringArray
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(WeaponProperties.DAMAGE).appendint(int(self.getDamage()))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(WeaponProperties.RANGE).appendint(int(self.getRange()))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(WeaponProperties.RELOAD).appendlong(self.getReloadTime())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.math.BasicDecimal import BasicDecimal
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


WeaponProperties.NULL_WEAPON_PROPERTIES = WeaponProperties(0, 0, 0, 0, ((int(0) + 32768) % 65536 - 32768))

