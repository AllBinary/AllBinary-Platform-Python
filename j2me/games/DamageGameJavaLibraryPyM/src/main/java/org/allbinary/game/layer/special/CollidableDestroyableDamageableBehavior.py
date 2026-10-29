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
# package org.allbinary.game.layer.special

from __future__ import annotations

from org.allbinary.game.collision.CollidableBaseBehavior import CollidableBaseBehavior


class CollidableDestroyableDamageableBehavior(CollidableBaseBehavior):

    def _init_fields(self) -> None:
        self.damageUtil: DamageUtil = DamageUtil.getInstance()
    

    def __init__(self, collidable: bool) -> None:
        super().__init__(collidable)
        self._init_fields()
    

    def isCollision(self, ownerLayer: CollidableCompositeLayer, collisionLayer: CollidableCompositeLayer) -> bool:
        if ownerLayer.getGroupInterface()[0] != collisionLayer.getGroupInterface()[0]:
            return super().isCollision(ownerLayer, collisionLayer)
        return False
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        ownerCollidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = ownerLayer
        collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = collidableInterfaceCompositeInterface
        ownerCollidableDestroyableDamageableLayer.damage(collidableDestroyableDamageableLayer.getDamage(0), 0)
    

    def isCollisionInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> bool:
        ForcedLogUtil.log("No Longer Used", self)
        return False
    

    # throws Exception
    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> None:
        ForcedLogUtil.log("No Longer Used", self)
from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
from org.allbinary.game.combat.damage.DamageUtil import DamageUtil
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil


