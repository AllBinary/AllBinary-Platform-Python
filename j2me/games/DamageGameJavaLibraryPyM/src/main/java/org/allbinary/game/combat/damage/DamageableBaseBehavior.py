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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.combat.damage.DamageableInterface import DamageableInterface


class DamageableBaseBehavior(DamageableInterface):
    instance: DamageableBaseBehavior = None
    

    @staticmethod
    def getInstance() -> DamageableBaseBehavior:
        return DamageableBaseBehavior.instance
    

    def getName(self) -> str:
        return __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self))
    

    # throws Exception
    def damage(self, damage: int, damageType: int) -> None:
        pass
    

    # throws Exception
    def getDamage(self, damageType: int) -> int:
        return 6000


def _DamageableBaseBehavior_instance() -> object:
    return DamageableBaseBehavior()

lazy_static(DamageableBaseBehavior, "instance", _DamageableBaseBehavior_instance)

