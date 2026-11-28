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
# package org.allbinary.game.ag.layer.weapon.mine

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.layer.weapon.SimpleWeaponLayer import SimpleWeaponLayer


@java_inherited_overloads
class MineLayer(SimpleWeaponLayer):
    NAME: str = "MineLayer"
    def _java_defaults(self):
        vars(self).setdefault("viewPositionEventHandler", None)

    def _init_fields(self) -> None:
        from org.allbinary.view.event.ViewPositionEventHandler import ViewPositionEventHandler
        self.viewPositionEventHandler: ViewPositionEventHandler = ViewPositionEventHandler.getInstance()
    

    def __init__(self, viewPosition: ViewPositionBase) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.ag.layer.weapon.mine.MineWeaponResources import MineWeaponResources
        from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
        from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.physics.movement.NoMovementFactory import NoMovementFactory
        from org.allbinary.view.ViewPositionBase import ViewPositionBase
        super().__init__(MineLayer.NAME, RemoteInfo.REMOTE_INFO, -1, NoMovementFactory.getInstance().getMovmentInstance(), FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(MineWeaponResources.getInstance().RESOURCE).getInstance(0), SimpleWeaponLayer.createDestroyed(), Rectangle(PointFactory.getInstance().ZERO_ZERO, 10, 10), viewPosition)
        __class__._init_fields(self)
    

    def initXYZ(self, x: int, y: int, z: int) -> None:
        from org.allbinary.ag.weapon.media.audio.DropWeaponSound import DropWeaponSound
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
        self.setPosition(x + 5, y + 5, z)
        self.viewPositionEventHandler.addListener(self)
        SecondaryPlayerQueueFactory.getInstance().add(DropWeaponSound.getInstance())
    

    def damage(self, damage: int, damageType: int) -> None:
        self.totalDamage = self.getInitDamage() + 1
    

    def getDamage(self, damageType: int) -> int:
        java_super_call(super(), "getDamage", damageType)
        return self.getInitDamage()
    

    def setDestroyed(self, destroyed: bool) -> None:
        java_super_call(super(), "setDestroyed", destroyed)
        if java_predicate(self, "isDestroyed"):
            self.viewPositionEventHandler.removeListener(self)
# from org.allbinary.ag.weapon.media.audio.DropWeaponSound import DropWeaponSound
# from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
# from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.media.audio.SecondaryPlayerQueueFactory import SecondaryPlayerQueueFactory
# from org.allbinary.physics.movement.NoMovementFactory import NoMovementFactory
# from org.allbinary.view.ViewPositionBase import ViewPositionBase
# from org.allbinary.view.event.ViewPositionEventHandler import ViewPositionEventHandler


