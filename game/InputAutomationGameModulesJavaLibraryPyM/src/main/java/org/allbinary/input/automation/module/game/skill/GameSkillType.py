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


GameSkillType.MANA = GameSkillType("Mana")

GameSkillType.REPLENISH = GameSkillType("Replenish")

GameSkillType.TIMED = GameSkillType("Timed")

GameSkillType.ATTACK = GameSkillType("Attack")

GameSkillType.TRANSPORT = GameSkillType("Transport")

