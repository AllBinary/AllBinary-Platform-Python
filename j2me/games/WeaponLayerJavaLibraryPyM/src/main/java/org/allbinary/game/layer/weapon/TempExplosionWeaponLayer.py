# Generated Code Do Not Modify
# package org.allbinary.game.layer.weapon

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.layer.weapon.SimpleWeaponLayer import SimpleWeaponLayer


@java_inherited_overloads
class TempExplosionWeaponLayer(SimpleWeaponLayer):
    def _java_defaults(self):
        vars(self).setdefault("weaponProperties", None)
        vars(self).setdefault("timeDelayHelper", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.weaponProperties: WeaponProperties = WeaponProperties(-1, -1, 0, 1000, ((int(0) + 32768) % 65536 - 32768))
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(0)
    

    def __init__(self, name: str, movement: Movement, animationInterface: Animation, rectangle: Rectangle, viewPosition: ViewPositionBase, timeDelay: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.layer.weapon.SimpleWeaponLayer import SimpleWeaponLayer
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.physics.movement.Movement import Movement
        from org.allbinary.view.ViewPositionBase import ViewPositionBase
        super().__init__(name, RemoteInfo.REMOTE_INFO, -1, movement, animationInterface, SimpleWeaponLayer.createDestroyed(), rectangle, viewPosition)
        __class__._init_fields(self)
        self.timeDelayHelper.delay = timeDelay
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        if self.timeDelayHelper.isTime(GameTickTimeDelayHelperFactory.getInstance().startTime):
            self.getCollidableInferface().collide(self, self)
            self.totalDamage = self.getInitDamage() + 1
        java_super_call(super(), "processTick", allBinaryLayerManager)
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
# from org.allbinary.game.multiplayer.layer.RemoteInfo import RemoteInfo
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.physics.movement.Movement import Movement
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.view.ViewPositionBase import ViewPositionBase


