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


class DamageWeaponLayer(WeaponLayer):
    

    def __init__(self, name: str, remoteInfo: RemoteInfo, movement: Movement, animationInterface: Animation, destroyedAnimationInterface: Animation, rectangle: Rectangle, viewPosition: ViewPositionBase, username: str, actorSessionId: int, id: int, multiPlayerType: int) -> None:
        from org.allbinary.game.layer.weapon.CollidableDamageWeaponBehavior import CollidableDamageWeaponBehavior
        super().__init__(name, remoteInfo, multiPlayerType, movement, animationInterface, destroyedAnimationInterface, rectangle, viewPosition)
        self.setCollidableInferface(CollidableDamageWeaponBehavior(True))
from org.allbinary.animation.Animation import Animation
from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.physics.movement.Movement import Movement
from org.allbinary.view.ViewPositionBase import ViewPositionBase


