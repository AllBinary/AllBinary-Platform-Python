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

from org.allbinary.game.layer.weapon.WeaponLayer import WeaponLayer


class SimpleWeaponLayer(WeaponLayer):
    

    # throws Exception
    @staticmethod
    def createDestroyed() -> Animation:
        return FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().getProcedural(ExplosionResources.getInstance().THIRD_EXPLOSION_RESOURCE).getInstanceAnimation(NullIndexedAnimationFactory.getFactoryInstance().getInstance(0))
    

    def __init__(self, name: str, remoteInfo: RemoteInfo, multiPlayerType: int, movement: Movement, animationInterface: Animation, destroyedAnimationInterface: Animation, rectangle: Rectangle, viewPosition: ViewPositionBase) -> None:
        from org.allbinary.game.layer.weapon.CollidableWeaponBehavior import CollidableWeaponBehavior
        super().__init__(name, remoteInfo, multiPlayerType, movement, animationInterface, destroyedAnimationInterface, rectangle, viewPosition)
        self.setCollidableInferface(CollidableWeaponBehavior(True))
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.animation.NullIndexedAnimationFactory import NullIndexedAnimationFactory
from org.allbinary.game.combat.damage.ExplosionResources import ExplosionResources
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.physics.movement.Movement import Movement
from org.allbinary.view.ViewPositionBase import ViewPositionBase


