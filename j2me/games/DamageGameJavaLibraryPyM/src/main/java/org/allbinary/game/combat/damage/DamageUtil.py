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



class DamageUtil:
    instance: DamageUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.COLLIDE: str = "collide"
    

    @staticmethod
    def getInstance() -> DamageUtil:
        return DamageUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def process(self, damageableInterface: DamageableInterface, damageableInterface2: DamageableInterface) -> None:
        damageableInterface.damage(damageableInterface2.getDamage(0), 0)
    

    # throws Exception
    def debugDamage(self, collidableInterfaceCompositeInterface1: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = collidableInterfaceCompositeInterface
        damage: int = collidableDestroyableDamageableLayer.getDamage(0)
        if damage > 20000:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Collision ")
            stringBuffer.append(str(collidableInterfaceCompositeInterface1))
            stringBuffer.append(" with: ")
            stringBuffer.append(str(collidableInterfaceCompositeInterface))
            stringBuffer.append(" damage: ")
            stringBuffer.appendint(damage)
            self.logUtil.putF(str(stringBuffer), collidableInterfaceCompositeInterface1, self.COLLIDE)
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


DamageUtil.instance = DamageUtil()

