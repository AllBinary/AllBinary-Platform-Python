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
# package org.allbinary.game.combat

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class CombatBaseBehavior:
    NULL_COMBAT_BEHAVIOR: CombatBaseBehavior = None

    def _init_fields(self) -> None:
        from org.allbinary.game.combat.damage.DamageableBaseBehavior import DamageableBaseBehavior
        from org.allbinary.game.combat.destroy.DestroyableBaseBehavior import DestroyableBaseBehavior
        self.damageableBaseBehavior: DamageableBaseBehavior = None
        self.destroyableBaseBehavior: DestroyableBaseBehavior = None
        self.readyForExplosion: bool = False
    

    def __init__(self, damageableBaseBehavior: DamageableBaseBehavior, destroyableBaseBehavior: DestroyableBaseBehavior) -> None:
        from org.allbinary.game.combat.damage.DamageableBaseBehavior import DamageableBaseBehavior
        from org.allbinary.game.combat.destroy.DestroyableBaseBehavior import DestroyableBaseBehavior
        self._init_fields()
        self.damageableBaseBehavior = damageableBaseBehavior
        self.destroyableBaseBehavior = destroyableBaseBehavior
    

    def getDamageableBaseBehavior(self) -> DamageableBaseBehavior:
        from org.allbinary.game.combat.damage.DamageableBaseBehavior import DamageableBaseBehavior
        return self.damageableBaseBehavior
    

    def getDestroyableBaseBehavior(self) -> DestroyableBaseBehavior:
        from org.allbinary.game.combat.destroy.DestroyableBaseBehavior import DestroyableBaseBehavior
        return self.destroyableBaseBehavior
    

    def isReadyForExplosion(self) -> bool:
        return self.readyForExplosion
    

    def setReadyForExplosion(self, readyForExplosion: bool) -> None:
        self.readyForExplosion = readyForExplosion
# from org.allbinary.game.combat.damage.DamageableBaseBehavior import DamageableBaseBehavior
# from org.allbinary.game.combat.destroy.DestroyableBaseBehavior import DestroyableBaseBehavior


def _CombatBaseBehavior_NULL_COMBAT_BEHAVIOR() -> object:
    from org.allbinary.game.combat.damage.DamageableBaseBehavior import DamageableBaseBehavior
    from org.allbinary.game.combat.destroy.DestroyableBaseBehavior import DestroyableBaseBehavior
    return CombatBaseBehavior(DamageableBaseBehavior.getInstance(), DestroyableBaseBehavior.getInstance())

lazy_static(CombatBaseBehavior, "NULL_COMBAT_BEHAVIOR", _CombatBaseBehavior_NULL_COMBAT_BEHAVIOR)

