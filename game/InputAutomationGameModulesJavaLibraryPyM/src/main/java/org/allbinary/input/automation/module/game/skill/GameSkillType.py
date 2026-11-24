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
# package org.allbinary.input.automation.module.game.skill

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameSkillType:
    MANA: GameSkillType = None
    REPLENISH: GameSkillType = None
    TIMED: GameSkillType = None
    ATTACK: GameSkillType = None
    TRANSPORT: GameSkillType = None

    def _init_fields(self) -> None:
        self.SPELL_GAME_SKILL_TYPE: str = "SpellGameSkillType: "
        self.name: str = None
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.setName(name)
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def toString(self) -> str:
        return self.SPELL_GAME_SKILL_TYPE + self.getName()

    def __str__(self) -> str:
        return self.toString()


def _GameSkillType_MANA() -> object:
    return GameSkillType("Mana")

lazy_static(GameSkillType, "MANA", _GameSkillType_MANA)

def _GameSkillType_REPLENISH() -> object:
    return GameSkillType("Replenish")

lazy_static(GameSkillType, "REPLENISH", _GameSkillType_REPLENISH)

def _GameSkillType_TIMED() -> object:
    return GameSkillType("Timed")

lazy_static(GameSkillType, "TIMED", _GameSkillType_TIMED)

def _GameSkillType_ATTACK() -> object:
    return GameSkillType("Attack")

lazy_static(GameSkillType, "ATTACK", _GameSkillType_ATTACK)

def _GameSkillType_TRANSPORT() -> object:
    return GameSkillType("Transport")

lazy_static(GameSkillType, "TRANSPORT", _GameSkillType_TRANSPORT)

