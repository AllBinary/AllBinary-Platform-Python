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
# package org.allbinary.game.layer.weapon

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.special.CollidableDestroyableDamageableBehavior import CollidableDestroyableDamageableBehavior


class CollidableWeaponBehavior(CollidableDestroyableDamageableBehavior):
    NULL_COLLIDABLE_WEAPON_BEHAVIOR: object = None

    def _init_fields(self) -> None:
        from org.allbinary.game.collision.CollisionHelper import CollisionHelper
        self.collided: bool = False
        self.collisionHelper: CollisionHelper = None
    

    @staticmethod
    def getNullInstance() -> CollidableWeaponBehavior:
        from org.allbinary.logic.NullUtil import NullUtil
        if CollidableWeaponBehavior.NULL_COLLIDABLE_WEAPON_BEHAVIOR == NullUtil.getInstance().NULL_OBJECT:
            CollidableWeaponBehavior.NULL_COLLIDABLE_WEAPON_BEHAVIOR = CollidableWeaponBehavior(False)
        return CollidableWeaponBehavior.NULL_COLLIDABLE_WEAPON_BEHAVIOR
    

    def __init__(self, collidable: bool) -> None:
        from org.allbinary.game.collision.CollidableHelperFactory import CollidableHelperFactory
        super().__init__(collidable)
        self._init_fields()
        self.setCollided(False)
        self.setCollidable(True)
        self.collisionHelper = CollidableHelperFactory.getInstance()
    

    def init(self, sourceLayerInterface: AllBinaryLayer) -> None:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        self.setCollided(False)
        self.collisionHelper.setOwnerLayerInterface(sourceLayerInterface)
    

    def isCollision(self, ownerLayer: CollidableCompositeLayer, collisionLayer: CollidableCompositeLayer) -> bool:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        if self.collisionHelper.isCollidable(collisionLayer):
            if ownerLayer.getGroupInterface()[0] != collisionLayer.getGroupInterface()[0]:
                return super().isCollision(ownerLayer, collisionLayer)
        return False
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collisionLayer: CollidableCompositeLayer) -> None:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        super().collide(ownerLayer, collisionLayer)
        self.collided = True
    

    def isCollisionInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> bool:
        from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        if self.collisionHelper.isCollidable(collidableInterfaceCompositeInterface):
            layerInterface: AllBinaryLayer = collidableInterfaceCompositeInterface
            if ownerLayer.getGroupInterface()[0] != layerInterface.getGroupInterface()[0]:
                if self.layerCollisionUtil.isCollision(ownerLayer, layerInterface):
                    return True
        return False
    

    # throws Exception
    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> None:
        from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
        from org.allbinary.game.combat.damage.DamageableInterface import DamageableInterface
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        ownerDamageableInterface: DamageableInterface = ownerLayer
        damageableInterface: DamageableInterface = collidableInterfaceCompositeInterface
        self.damageUtil.process(ownerDamageableInterface, damageableInterface)
        self.collided = True
    

    def getCollisionTypeWith(self, layerInterface: AllBinaryLayer) -> CollisionType:
        from org.allbinary.game.collision.CollisionType import CollisionType
        from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        return CollisionTypeFactory.getInstance().COLLISION
    

    def isCollided(self) -> bool:
        return self.collided
    

    def setCollided(self, collided: bool) -> None:
        self.collided = collided
# from org.allbinary.game.collision.CollidableHelperFactory import CollidableHelperFactory
# from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
# from org.allbinary.game.collision.CollisionHelper import CollisionHelper
# from org.allbinary.game.collision.CollisionType import CollisionType
# from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
# from org.allbinary.game.combat.damage.DamageableInterface import DamageableInterface
# from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.NullUtil import NullUtil


def _CollidableWeaponBehavior_NULL_COLLIDABLE_WEAPON_BEHAVIOR() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(CollidableWeaponBehavior, "NULL_COLLIDABLE_WEAPON_BEHAVIOR", _CollidableWeaponBehavior_NULL_COLLIDABLE_WEAPON_BEHAVIOR)

