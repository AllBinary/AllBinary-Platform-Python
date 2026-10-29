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

from org.allbinary.game.layer.special.CollidableDestroyableDamageableBehavior import CollidableDestroyableDamageableBehavior


class CollidableCharacterBehavior(CollidableDestroyableDamageableBehavior):
    

    def __init__(self, collidable: bool) -> None:
        super().__init__(collidable)
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        collisionTypeFactory: CollisionTypeFactory = CollisionTypeFactory.getInstance()
        collisionType: CollisionType = collidableInterfaceCompositeInterface.getCollidableInferface().getCollisionTypeWith(ownerLayer)
        if collisionType == collisionTypeFactory.PICKUP:
            collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = ownerLayer
            collidableDestroyableDamageableLayer.getPickupBehavior().doPickupLayer(collidableInterfaceCompositeInterface)
        else:
            super().collide(ownerLayer, collidableInterfaceCompositeInterface)
    

    # throws Exception
    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
from org.allbinary.game.collision.CollisionType import CollisionType
from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.game.layer.pickup.PickedUpLayerInterface import PickedUpLayerInterface
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil


