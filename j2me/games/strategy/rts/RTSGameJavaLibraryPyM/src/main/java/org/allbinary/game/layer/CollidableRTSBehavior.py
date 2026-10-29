# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.layer.special.CollidableDestroyableDamageableBehavior import CollidableDestroyableDamageableBehavior


class CollidableRTSBehavior(CollidableDestroyableDamageableBehavior):
    

    def __init__(self, collidable: bool) -> None:
        super().__init__(collidable)
    

    def isCollision(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> bool:
        collisionTypeFactory: CollisionTypeFactory = CollisionTypeFactory.getInstance()
        collisionType: CollisionType = collidableInterfaceCompositeInterface.getCollidableInferface().getCollisionTypeWith(ownerLayer)
        if collisionType == collisionTypeFactory.PICKUP:
            pass
        elif collisionType == collisionTypeFactory.COLLISION:
            return super().isCollision(ownerLayer, collidableInterfaceCompositeInterface)
        else:
            if collidableInterfaceCompositeInterface.getX2() <= ownerLayer.getXP() or collidableInterfaceCompositeInterface.getY2() <= ownerLayer.getYP() or collidableInterfaceCompositeInterface.getYP() >= ownerLayer.getY2() or collidableInterfaceCompositeInterface.getXP() >= ownerLayer.getX2():
                return False
            else:
                return True
        return False
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        collisionTypeFactory: CollisionTypeFactory = CollisionTypeFactory.getInstance()
        collisionType: CollisionType = collidableInterfaceCompositeInterface.getCollidableInferface().getCollisionTypeWith(ownerLayer)
        if collisionType == collisionTypeFactory.PICKUP:
            pass
        elif collisionType == collisionTypeFactory.COLLISION:
            super().collide(ownerLayer, collidableInterfaceCompositeInterface)
        else:
            self.collideNone(ownerLayer, collidableInterfaceCompositeInterface)
    

    # throws Exception
    def collideNone(self, ownerLayer: CollidableCompositeLayer, collidableInterface: CollidableCompositeLayer) -> None:
        pass
from org.allbinary.game.collision.CollisionType import CollisionType
from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory


